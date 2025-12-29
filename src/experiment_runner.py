import os
import json
import time
import math
from typing import List, Dict, Any
from tqdm import tqdm
from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt
import pandas as pd
from src.data_generator import StoryGenerator

# Configuration
MODEL_NAME = "gpt-4o"
API_KEY = os.environ.get("OPENAI_API_KEY")
RESULTS_DIR = "results"
RAW_DATA_FILE = os.path.join(RESULTS_DIR, "raw_data.jsonl")

client = OpenAI(api_key=API_KEY)

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
def get_model_response(system_prompt: str, user_prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API Error: {e}")
        raise

def batch_questions(questions: List[Dict], batch_size: int = 10) -> List[List[Dict]]:
    """Splits questions into batches."""
    for i in range(0, len(questions), batch_size):
        yield questions[i:i + batch_size]

def run_experiment():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    # Define experiment parameters
    # N values: focusing on the range where we expect dropoff
    n_values = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100]
    repeats_per_n = 3 # Number of stories per N
    questions_per_story = 20 # Sample subset of questions to ask
    
    generator = StoryGenerator()
    
    results = []
    
    # Check if we already have results to resume? (Skipping for now for simplicity, just appending)
    
    print(f"Starting experiment with model: {MODEL_NAME}")
    print(f"N values: {n_values}")
    
    for n in tqdm(n_values, desc="N-values"):
        for r in range(repeats_per_n):
            # Generate story
            story_data = generator.generate_story(n)
            story_text = story_data['story']
            all_questions = story_data['questions']
            
            # Sample questions
            import random
            # If we have fewer questions than target, take all
            if len(all_questions) > questions_per_story:
                selected_questions = random.sample(all_questions, questions_per_story)
            else:
                selected_questions = all_questions
                
            # Process in batches
            question_batches = list(batch_questions(selected_questions, batch_size=10))
            
            for batch_idx, batch in enumerate(question_batches):
                # Construct Prompt
                q_text = "\n".join([f"Q{i+1}: {q['question']}" for i, q in enumerate(batch)])
                
                system_prompt = "You are a precise reading comprehension assistant. You will be given a story and a list of numbered questions. Return a JSON object where keys are the question numbers (e.g., 'Q1') and values are the short, exact answers from the text."
                user_prompt = f"Story:\n{story_text}\n\nQuestions:\n{q_text}\n\nProvide the answers in JSON format."
                
                try:
                    response_json_str = get_model_response(system_prompt, user_prompt)
                    response_data = json.loads(response_json_str)
                    
                    # Evaluate
                    for i, q in enumerate(batch):
                        q_id = f"Q{i+1}"
                        model_answer = response_data.get(q_id, "").strip()
                        ground_truth = q['answer'].strip()
                        
                        # Soft matching: check if ground truth is in model answer (case insensitive)
                        is_correct = ground_truth.lower() in model_answer.lower()
                        
                        result_entry = {
                            "n_characters": n,
                            "story_id": f"{n}_{r}",
                            "question_type": q['type'],
                            "question": q['question'],
                            "ground_truth": ground_truth,
                            "model_answer": model_answer,
                            "is_correct": is_correct,
                            "model": MODEL_NAME
                        }
                        
                        results.append(result_entry)
                        
                        # Save incrementally
                        with open(RAW_DATA_FILE, "a") as f:
                            f.write(json.dumps(result_entry) + "\n")
                            
                except Exception as e:
                    print(f"Error processing batch {batch_idx} for N={n}: {e}")
                    # Log error entry
                    error_entry = {
                        "n_characters": n,
                        "error": str(e),
                        "batch_idx": batch_idx
                    }
                    with open(os.path.join(RESULTS_DIR, "errors.jsonl"), "a") as f:
                        f.write(json.dumps(error_entry) + "\n")

    print("Experiment completed.")

if __name__ == "__main__":
    run_experiment()
