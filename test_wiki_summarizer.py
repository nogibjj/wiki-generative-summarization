from wiki_summarizer import get_article_text, summarize
from click.testing import CliRunner


def test_get_article_text():
    article_txt = get_article_text(
        "https://en.wikipedia.org/wiki/Principal_component_analysis"
    )
    assert article_txt.__contains__(
        "The principal components of a collection "
        "of points in a real coordinate "
    )
    assert len(article_txt) > 50000


def test_summarize():
    runner = CliRunner()
    result = runner.invoke(
        summarize,
        ["https://en.wikipedia.org/wiki/Principal_component_analysis"],
    )
    assert len(result.output) == 159
