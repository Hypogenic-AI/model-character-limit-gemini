# Research Plan: How many characters can a model keep track of?

## Research Question
What is the effective capacity limit of Large Language Models (LLMs) for tracking distinct character identities and their attributes within a single narrative context? Specifically, at what number of active characters ($N$) does retrieval accuracy for specific attributes significantly degrade?

## Background and Motivation
While LLMs have large context windows (128k+ tokens), "effective" context length is often shorter. "Lost in the Middle" phenomena and attention dispersion suggest that models may struggle to maintain distinct representations for many entities simultaneously.
Real-world narratives like *War and Peace* involve hundreds of characters. Understanding if models can actually track these, or if they rely on local context (heuristic matching), is crucial for applications in long-form creative writing, game mastering, and complex legal/financial analysis involving multiple parties.

## Hypothesis Decomposition
1.  **Capacity Limit:** There exists a threshold $N$ where accuracy drops non-linearly, indicating a saturation of the model's "entity working memory".
2.  **Attribute Binding:** Models will struggle more with binding specific attributes to specific characters (e.g., "Who has the red hat?") than simply recalling presence.
3.  **Interference:** As $N$ increases, "cross-talk" errors (attributing Bob's job to Alice) will increase.

## Proposed Methodology

### Approach
We will use a **Controlled Synthetic Narrative** approach.
We will generate stories about a "Gathering" where $N$ characters are introduced with specific attributes (e.g., Profession, Location, Item).
The narrative will interleave information to prevent simple local-context retrieval.

### Experimental Steps
1.  **Data Generation:**
    - Create a pool of distinct names and attributes.
    - For $N \in \{5, 10, 20, 30, 50, 100\}$:
        - Generate a story where $N$ characters are introduced.
        - Assign 2-3 key attributes to each (e.g., "Alice is a Doctor", "Bob is a Builder").
        - Shuffle the order of introduction and attribute revelation to ensure distribution across context.
2.  **Experiment Execution:**
    - Feed the story to the LLM.
    - Ask a set of probes: "What is [Name]'s profession?" or "Who is the [Profession]?".
    - Models to test: High-performance model (e.g., GPT-4o or Gemini 1.5 Pro via OpenRouter) to find the state-of-the-art limit.
3.  **Evaluation:**
    - Exact Match (EM) or semantic equivalence for the attribute.

### Baselines
- **Random Baseline:** $1/N$ or $1/|Attributes|$.
- **Majority Class:** (If attributes are uneven, though we will balance them).

### Evaluation Metrics
- **Attribute Retrieval Accuracy:** $\%$ of correctly recalled attributes.
- **Hallucination Rate:** $\%$ of answers that are not in the story at all.
- **Misattribution Rate:** $\%$ of answers that are correct for *another* character.

### Statistical Analysis Plan
- Plot Accuracy vs. $N$.
- Fit a logistic regression or simple threshold curve to find the "knee" of the curve.

## Expected Outcomes
We expect high accuracy for $N < 20$, with a gradual decline. A sharp drop-off might indicate a specific attention head capacity limit or mechanism failure.

## Timeline and Milestones
- **Phase 2 (Setup):** 10 min. Env setup, API key check.
- **Phase 3 (Impl):** 40 min. Generator script, OpenAI/OpenRouter client wrapper.
- **Phase 4 (Exp):** 40 min. Run sweeps for different $N$.
- **Phase 5 (Analysis):** 30 min. Graphs, error analysis.
- **Phase 6 (Docs):** 20 min. Final report.

## Potential Challenges
- **Context Length:** $N=100$ might generate very long prompts. We need to ensure we fit within the context window (128k is plenty, but cost is a factor).
- **Prompt Sensitivity:** The model might refuse to read a boring list. We need to frame it as a story.
- **Cost:** Many characters * many queries = many tokens. We will limit the number of runs per $N$ (e.g., 5-10 stories per $N$).

## Success Criteria
- A clear plot showing Accuracy vs. Number of Characters.
- Identification of a specific range where performance degrades.
