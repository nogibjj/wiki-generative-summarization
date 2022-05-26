install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py --line-length 79

lint:
	flake8 *.py

all: install format lint