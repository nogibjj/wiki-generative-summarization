install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py --line-length 79

lint:
	pylint --disable=R,C,broad-except,bare-except,consider-using-f-string wiki_summarizer.py

test:
	python -m pytest -vv test_wiki_summarizer.py

all: install format lint test