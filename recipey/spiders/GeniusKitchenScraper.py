import urllib2
from bs4 import BeautifulSoup

class GeniusKitchenScraper:
    def parse(url):
        recipe_page = urllib2.urlopen(url);
        soup = BeautifulSoup(page, 'html.parser')

        name_box = soup.find('h1', attrs={})

        name = name_box.text.strip()
        print name

        stars_div = soup.find('div', attrs={'class': 'rating-stars'})

        stars = "{:.2f}".format(float(stars_div["data-ratingstars"]))

        print stars

        ingredients_div = soup.findAll('span', attrs={'class': 'recipe-ingred_txt added'})

        for ingredient in ingredients_div:
            print ingredient.string

        print

        directions_div = soup.findAll('span', attrs={'class': 'recipe-directions__list--item'})

        count = 1;

        for direction in directions_div:
            if direction.string == None:
                continue;
            s = direction.string
            print str(count) + ". " + s
            count+=1

        prep_time = soup.find('time', attrs={'itemprop': 'prepTime'})

        print prep_time["datetime"].split("T")[1]

        cook_time = soup.find('time', attrs={'itemprop': 'cookTime'})

        print cook_time["datetime"].split("T")[1]

        total_time = soup.find('time', attrs={'itemprop': 'totalTime'})

        print total_time["datetime"].split("T")[1]
