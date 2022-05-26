import requests
from bs4 import BeautifulSoup
import click
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def truncate_summary(input_text, min_length, max_length, model, tokenizer):
    """
    It takes in a text, a minimum length, a maximum length, a model, and a tokenizer, and returns a summary

    :param input_text: The text you want to summarize
    :param min_length: The minimum length of the summary
    :param max_length: The maximum length of the summary
    :param model: The model to use for summarization
    :param tokenizer: The tokenizer to use
    :return: The summary of the text.
    """
    inputs = tokenizer(
        input_text, return_tensors="pt", max_length=1024, truncation=True
    )
    # Generating the summary.
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        length_penalty=1.0,
        num_beams=4,
        early_stopping=True,
    )
    return tokenizer.decode(outputs[0])


@click.command()
@click.option(
    "--url", type=str, default="https://en.wikipedia.org/wiki/Dimensionality_reduction"
)
def summarize(url):
    """
    It takes a URL, downloads the article text, and generates a summary

    :param url: The URL of the article you want to summarize
    """
    # Load model & tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    # Set desired target min and max length for summary (not strict bounds)
    min_length = 50
    max_length = 200
    # Generate summary
    article_text = get_article_text(url)
    summary = truncate_summary(article_text, min_length, max_length, model, tokenizer)
    # Clean up output formatting
    summary = summary.split("</s>")[-2].split("<s>")[-1].strip()

    print("Length of the input document: {}".format(len(article_text.split(" "))))
    print("Length of the summary: {}".format(len(summary.split(" "))))
    print("Summary: ")
    print(summary)


def get_article_text(wiki_url):
    """
    It takes a Wikipedia URL and returns the text of the article

    :param wiki_url: The URL of the Wikipedia article you want to scrape
    :return: A string of the article text
    """
    # Get article from Wiki
    page = requests.get(wiki_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract body text
    bodytext = soup.find_all("p")
    bodytext = [i.text for i in bodytext]
    article_text = " ".join(bodytext)
    return article_text


# It's a Python idiom that allows you to run a script directly from the command line.
if __name__ == "__main__":
    summarize()
