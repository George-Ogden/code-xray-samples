import pytest
from scrapy.http import HtmlResponse

from stackoverflow_spider import StackOverflowSpider


@pytest.fixture
def spider():
    return StackOverflowSpider()


def test_parse(spider):
    body = """
    <html>
        <body>
            <div class="question-summary">
                <h3><a href="/questions/12345/scrapy-example">How to use Scrapy?</a></h3>
                <div class="tags">
                    <a href="/questions/tagged/python">python</a>
                    <a href="/questions/tagged/scrapy">scrapy</a>
                </div>
                <div class="votes">
                    <span class="vote-count-post">42</span>
                </div>
            </div>
            <a rel="next" href="/questions/tagged/python?page=2"></a>
        </body>
    </html>
    """
    response = HtmlResponse(
        url="https://stackoverflow.com/questions/tagged/python", body=body, encoding="utf-8"
    )

    # Parse the mocked response
    result = list(spider.parse(response))

    # Assert that the spider correctly extracts data
    assert len(result) == 2
    assert result[0]["title"] == "How to use Scrapy?"
    assert result[0]["url"] == "/questions/12345/scrapy-example"
    assert result[0]["tags"] == ["python", "scrapy"]
    assert result[0]["votes"] == "42"

    # Assert that pagination is correctly followed
    assert result[1].url == "/questions/tagged/python?page=2"
