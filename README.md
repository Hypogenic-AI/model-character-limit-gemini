# Model Character Tracking Capacity

## Overview
This project investigates the capacity of Large Language Models (LLMs) to track multiple character identities and attributes within a single narrative. We tested GPT-4o's ability to recall specific attributes (Profession, Location, Drink) for up to 75 distinct characters introduced in a synthetic story.

## Key Findings
- **Capacity > 75 Characters:** GPT-4o achieved **100% accuracy** on all tests up to 75 characters.
- **Robustness:** The model successfully handled shuffled narratives and random attribute queries without confusion.
- **Implication:** Current SOTA models have a very strong "entity working memory" for dense contexts.

## File Structure
- `src/data_generator.py`: Generates synthetic stories with N characters.
- `src/experiment_runner.py`: Runs the experiment using OpenAI API.
- `src/analysis.py`: Analyzes results and generates plots.
- `results/`: Contains raw logs, metrics, and plots.
- `REPORT.md`: Detailed research report.

## Reproduction
1. Install dependencies:
   ```bash
   uv sync
   ```
2. Run experiment:
   ```bash
   python -m src.experiment_runner
   ```
3. Analyze results:
   ```bash
   python -m src.analysis
   ```

## Resources
See `resources.md` for related papers and datasets used in background research.
