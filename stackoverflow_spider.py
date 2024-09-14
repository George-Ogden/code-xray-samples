import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://stackoverflow.com/questions/tagged/python",
    ]

    def parse(self, response):
        # Extract question titles
        for question in response.css("div.question-summary"):
            yield {
                "title": question.css("h3 a::text").get(),
                "url": question.css("h3 a::attr(href)").get(),
                "tags": question.css(".tags a::text").getall(),
                "votes": question.css(".vote-count-post::text").get(),
            }

        # Follow pagination links
        next_page = response.css("a[rel='next']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
