# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT committed to git due to size. Follow the download instructions below.

## Dataset 1: NarrativeQA

### Overview
- **Source**: HuggingFace (`narrativeqa`)
- **Task**: Reading comprehension on long narratives (books, movie scripts).
- **Format**: Contains full texts (Gutenberg) or summaries, questions, and answers.
- **Size**: ~32k examples.

### Download Instructions
```python
from datasets import load_dataset
dataset = load_dataset("narrativeqa")
dataset.save_to_disk("datasets/narrativeqa")
```

### Loading
```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/narrativeqa")
```

### Sample Data (Truncated)
See `datasets/samples/narrativeqa.json`.
The dataset contains a `document` field with the full text or summary, and a `question` field. This is ideal for testing if a model can track a character mentions throughout a long document to answer specific questions.

## Dataset 2: BookSum

### Overview
- **Source**: HuggingFace (`kmfoda/booksum`)
- **Task**: Long-form narrative summarization.
- **Format**: Chapter, paragraph, and book-level summaries aligned with source text.
- **Size**: ~9.6k training examples.

### Download Instructions
```python
from datasets import load_dataset
dataset = load_dataset("kmfoda/booksum")
dataset.save_to_disk("datasets/booksum")
```

### Loading
```python
from datasets import load_from_disk
dataset = load_from_disk("datasets/booksum")
```

### Sample Data (Truncated)
See `datasets/samples/booksum.json`.
Useful for generating character profiles or testing if a model can summarize the arc of a specific character across chapters.

## Notes
- **Git**: Data files are excluded via `.gitignore`.
- **Usage**: Use `load_from_disk` for faster access after initial download.
