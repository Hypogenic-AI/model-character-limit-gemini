# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project "How many characters can a model keep track of?".

## Papers
Total papers downloaded: 6

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Entity Tracking in Language Models | Kim & Schuster | 2023 | papers/2305.02363... | Code pretraining helps entity tracking. |
| Code Pretraining Improves... | | 2024 | papers/2405.21068... | Validation of the above. |
| SCORE: Story Coherence... | Yi et al. | 2025 | papers/2503.23512... | Framework for fixing coherence. |
| ETHIC: Evaluating LLMs... | Lee et al. | 2024 | papers/2410.16848... | Benchmark for long-context coverage. |
| Evaluating Character Understanding... | Yuan et al. | 2024 | papers/2404.12726... | Character profiling task. |
| If an LLM Were a Character... | | 2025 | papers/2503.23514... | Lifelong learning/simulacra. |

See `papers/README.md` for details.

## Datasets
Total datasets downloaded: 2

| Name | Source | Size | Task | Location |
|------|--------|------|------|----------|
| NarrativeQA | HuggingFace | 32k | Reading Comprehension | `datasets/narrativeqa/` |
| BookSum | HuggingFace | 9.6k | Summarization | `datasets/booksum/` |

See `datasets/README.md` for details.

## Code Repositories
Total repositories cloned: 2

| Name | URL | Purpose | Location |
|------|-----|---------|----------|
| Entity Tracking | github.com/najoungkim... | Data gen & eval | `code/entity-tracking/` |
| ETHIC | github.com/dmis-lab/ETHIC | Long-context benchmark | `code/ETHIC/` |

See `code/README.md` for details.

## Resource Gathering Notes

### Search Strategy
Focused on recent (2023-2025) papers regarding "entity tracking", "character coherence", and "long-context understanding". Used Google Search to identify key papers and then downloaded them via arXiv.

### Selection Criteria
Selected papers that specifically address the *capacity* or *mechanism* of tracking entities, rather than just general long-context performance. Datasets were chosen for their focus on long narratives (books).

### Recommendations for Experiment Design

1.  **Primary Dataset**: Use **BookSum** or **NarrativeQA** texts.
2.  **Method**: Adapt the **Entity Tracking** code (Kim & Schuster) to generate synthetic probes on the real texts from BookSum. For example, inject questions about the state of the Nth character after X tokens.
3.  **Baseline**: Compare a standard model (e.g., Llama-3-8B) against a code-heavy model or a long-context fine-tuned model.
4.  **Metric**: Accuracy of state retrieval vs. Number of Active Characters vs. Context Length.
