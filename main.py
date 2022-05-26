import requests
from bs4 import BeautifulSoup
import click
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def truncate_summary(input_text, min_length, max_length, model, tokenizer):
    inputs = tokenizer(
        input_text, return_tensors="pt", max_length=1024, truncation=True
    )
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
    # Get article from Wiki
    page = requests.get(wiki_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract body text
    bodytext = soup.find_all("p")
    bodytext = [i.text for i in bodytext]
    article_text = " ".join(bodytext)
    return article_text


if __name__ == "__main__":
    summarize()
