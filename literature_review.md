# Literature Review: Entity Tracking and Character Capacity in LLMs

## Research Area Overview
Large Language Models (LLMs) have demonstrated impressive capabilities in generating fluent text, but their ability to maintain internal consistency regarding entities (characters, objects, locations) over long narratives remains a significant challenge. This research area focuses on quantifying this "entity tracking" capacity and understanding the mechanisms—such as tokenization, attention span, and training data composition—that influence it. Recent work suggests that while models can handle short-term coherence, they struggle with "high information coverage" tasks where the state of multiple entities must be tracked simultaneously over extended contexts.

## Key Papers

### 1. Entity Tracking in Language Models (Kim & Schuster, 2023)
- **Key Contribution**: Investigated the capability of LLMs to track the state of entities (e.g., location, status) as text unfolds.
- **Methodology**: Compared models pretrained on text only vs. text + code.
- **Key Findings**: Models pretrained on large amounts of code (like GPT-3.5) exhibit significantly stronger entity tracking abilities than text-only models. Smaller models can learn this via fine-tuning.
- **Relevance**: Establishes a baseline for *why* some models might be better (code structure logic).

### 2. Code Pretraining Improves Entity Tracking Abilities of Language Models (2024)
- **Key Contribution**: Systematically validates the hypothesis from Kim & Schuster (2023).
- **Key Findings**: Confirms that the logical structure inherent in code (variables, state changes) transfers to narrative entity tracking.

### 3. SCORE: Story Coherence and Retrieval Enhancement (Yi et al., 2025)
- **Key Contribution**: Proposes the SCORE framework to fix narrative inconsistencies.
- **Methodology**: Integrates dynamic state tracking and context-aware summarization with Retrieval-Augmented Generation (RAG).
- **Relevance**: Provides a method *to fix* the problem, implying the core model's native capacity is insufficient for long, complex stories without external aids.

### 4. ETHIC: Evaluating Long-Context Tasks with High Information Coverage (Lee et al., 2024)
- **Key Contribution**: Introduces the ETHIC benchmark.
- **Key Findings**: Existing benchmarks often require only retrieving a small piece of info ("needle in a haystack"). ETHIC requires understanding the *whole* context. Current LLMs degrade significantly on these tasks.
- **Relevance**: Suggests that "character tracking" is a "high information coverage" task—you can't just find one mention; you need the whole history.

### 5. Evaluating Character Understanding via Character Profiling (Yuan et al., 2024)
- **Key Contribution**: Proposes the **CroSS** dataset and a character profiling task.
- **Methodology**: asks models to summarize character traits from fictional works.
- **Relevance**: Directly relates to "how many characters" by testing the depth of understanding for specific characters.

## Common Methodologies
- **State Tracking Tasks**: monitoring an entity's property (e.g., location) step-by-step.
- **Question Answering**: Asking questions that require aggregating info about a character from multiple points in the text.
- **Summary Generation**: Generating profiles or summaries to test holistic understanding.

## Standard Baselines
- **GPT-3.5/4**: The standard for high performance.
- **Llama 2/3**: Common open-source baselines.
- **RAG-augmented models**: Using retrieval to "cheat" the context window limit.

## Datasets in the Literature
- **BookSum**: Often used for long-form narrative understanding.
- **NarrativeQA**: Question answering on stories.
- **CroSS**: Specifically for character profiling.
- **Simulacra/LifeState-Bench**: For lifelong/long-term tracking.

## Gaps and Opportunities
- **Quantification of "Capacity"**: Most papers say "it helps" or "it fails". Few rigorously define "Model X can track N active entities before performance drops by Y%".
- **Interference Effects**: How does adding more characters specifically degrade performance? (Linear vs. Exponential decay).

## Recommendations for Our Experiment
- **Focus**: We should try to find the "N" (number of characters) breakpoint.
- **Method**: Procedurally generate stories or use a dataset with many characters (like plays or complex novels) and probe the model on attributes of increasingly many characters.
- **Metric**: Accuracy of retrieving/stating the current state of the $N$-th character.
