from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
import numpy as np
import requests
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


# Get article from Wiki
url = 'https://en.wikipedia.org/wiki/Dimensionality_reduction'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract body text
bodytext = soup.find_all('p')
bodytext = [i.text for i in bodytext]
article_text = ' '.join(bodytext)

# Load model & tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")


def truncate_summary(input_text,min_length,max_length):
    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=max_length, min_length=min_length, length_penalty=1.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0])


# Set desired target min and max length for summary (note: these do not act as strict bounds)
min_length = 50
max_length = 200
# Generate summary
summary = truncate_summary(article_text,min_length,max_length)
# Clean up output formatting
summary = summary.split('</s>')[-2].split('<s>')[-1].strip()

print('Length of the source document: {}'.format(len(article_text.split(' '))))
print('Length of the summary: {}'.format(len(summary.split(' '))))
print('Summary: ')
print(summary)