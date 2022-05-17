from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
import numpy as np
import requests
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer