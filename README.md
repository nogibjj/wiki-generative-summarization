# wiki-generative-summarization

[![Wiki Generative Summarization CLI Tool](https://github.com/nogibjj/wiki-generative-summarization/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/wiki-generative-summarization/actions/workflows/main.yml)

CLI tool that uses a pre-trained model to generate summary for a Wikipedia article. 
We will use the open source Hugging Face library to load and use a transformer model.

[Huggingface Reference](https://huggingface.co/docs/transformers/task_summary#summarization)
## Overview

 1. Retrieve Wikipedia document to summarize
 2. Load the model & associated tokenizer
 3. Generate and return the summary

## Usage

```
python3 main.py --url "https://en.wikipedia.org/wiki/Construct_validity"
```

Example output
```
Length of the input document: 1788
Length of the summary: 68
Summary: 
Construct validity is the accumulation of evidence to support the interpretation of what a measure reflects. 
Modern validity theory defines construct validity as the overarching concern of validity research, subsuming
all other types of validity evidence. Construct validity examines the question: Does the measure behave like 
the theory says a measure of that construct should behave? construct validity is essential to the perceived overall 
validity of the test.
```

## Development 

Creating virtual environment:

 1. `python3 -m venv venv`
 2. (On Unix or MacOS) `source venv/bin/activate`

Contributing guidelines:

Run `make all` before pushing code.
