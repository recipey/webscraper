import scrapy

class RecipeSpider(scrapy.Spider):
    name = "recipe_spider"
    USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    DOWNLOAD_DELAY = 1

    def start_requests(self):
            urls = [
                'http://www.geniuskitchen.com/recipe/beer-bread-73440'
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
