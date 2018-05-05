import scrapy
from urllib.request import urlopen
from bs4 import BeautifulSoup

class RecipeSpider(scrapy.Spider):
    name = "recipe_spider"
    USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    download_delay = 1

    forbidden_refs = ['google', 'twitter', 'facebook']

    def start_requests(self):
        urls = [
            'https://www.thekitchn.com/shrimp-scampi-recipe-257176',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # recipe_page = urlopen(response.url);

        soup = BeautifulSoup(response.body, 'html.parser')

        ingredients = soup.find('div', attrs={'class': 'PostRecipeIngredientGroup'})

        if ingredients is not None:
            page = soup.find('h1', attrs={}).text.strip()

            filename = 'recipe-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

        next_pages = soup.findAll('a', href=True);
        for next_page in next_pages:
            if next_page is not None:
                if 'https://www.thekitchn.com/' in next_page['href'] and not any(ref in next_page['href'] for ref in self.forbidden_refs):
                    yield scrapy.Request(url=next_page['href'], callback=self.parse)
