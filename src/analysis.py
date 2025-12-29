import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

RESULTS_FILE = "results/raw_data.jsonl"
PLOTS_DIR = "results/plots"

def analyze_results():
    if not os.path.exists(RESULTS_FILE):
        print(f"No results file found at {RESULTS_FILE}")
        return

    os.makedirs(PLOTS_DIR, exist_ok=True)

    data = []
    with open(RESULTS_FILE, 'r') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    
    df = pd.DataFrame(data)
    
    print(f"Loaded {len(df)} records.")
    
    # 1. Overall Accuracy vs N
    accuracy_by_n = df.groupby('n_characters')['is_correct'].mean().reset_index()
    print("\nAccuracy by N characters:")
    print(accuracy_by_n)
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='n_characters', y='is_correct', marker='o', errorbar=('ci', 95))
    plt.title(f'Character Attribute Tracking Accuracy vs. Number of Characters\nModel: {df["model"].iloc[0] if not df.empty else "Unknown"}')
    plt.xlabel('Number of Characters (N)')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1.05)
    plt.grid(True)
    plt.savefig(f"{PLOTS_DIR}/accuracy_vs_n.png")
    plt.close()
    
    # 2. Accuracy by Question Type
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='n_characters', y='is_correct', hue='question_type', marker='o', errorbar=None)
    plt.title('Accuracy vs. N by Attribute Type')
    plt.xlabel('Number of Characters')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1.05)
    plt.grid(True)
    plt.legend(title='Question Type')
    plt.savefig(f"{PLOTS_DIR}/accuracy_by_type.png")
    plt.close()
    
    # 3. Position Analysis (if we had position info, but we shuffled, so maybe not relevant unless we tracked it)
    # However, we can look at "Hallucinations". 
    # Let's see how many wrong answers were names of other characters vs random text.
    # This is harder to automate perfectly without the char list, but we can look at answer length or simple stats.
    
    # Save metrics
    metrics = {
        "overall_accuracy": df['is_correct'].mean(),
        "accuracy_by_n": accuracy_by_n.to_dict(orient='records'),
        "accuracy_by_type": df.groupby('question_type')['is_correct'].mean().to_dict()
    }
    
    with open("results/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"\nAnalysis complete. Plots saved to {PLOTS_DIR}")

if __name__ == "__main__":
    analyze_results()
