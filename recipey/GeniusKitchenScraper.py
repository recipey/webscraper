import urllib2
from bs4 import BeautifulSoup
from bs4 import Tag

def scrape(url):
    d = {}
    
    recipe_page = urllib2.urlopen(url);
    soup = BeautifulSoup(recipe_page, 'html.parser')

    name_box = soup.find('h1', attrs={})

    name = name_box.text.strip()
##        print name
    d["name"] = name

    stars_div = soup.find('span', attrs={'class': 'gk-rating-percent'})

    if stars_div != None:
        stars_div = stars_div.find('span')
        stars = "{:.2f}".format(float(stars_div.text))

        d["rating"] = stars
##            print stars

    ingredients_div = soup.find('ul', attrs={'class': 'ingredient-list'})

    ingredients = []

    for ingredient in ingredients_div:
        if isinstance(ingredient, Tag):
            try:
                qty = ingredient.find('span', attrs={'class': 'qty'}).text.encode('utf8','ignore')
                food = ingredient.find('span', attrs={'class': 'food'}).text.encode('utf8','ignore')
                food_link = ingredient.find('span', attrs={'class': 'food'}).find('a', href=True)

                if food_link != None:
                    food_link = food_link["href"]

                ingredients.append((' '.join(qty.split()) + " " + ' '.join(food.split()), food_link))
            except AttributeError:
                pass

    d["ingredients"] = ingredients
##        print

    directions_div = soup.find('ol')

    count = 1;

    directions = []

    for direction in directions_div.findAll('li'):
        if direction.string == None or direction.string.strip() == "":
            continue;
        s = direction.string

        directions.append(s)
##            print str(count) + ". " + s
        count+=1

    d["directions"] = directions

    total_time = soup.find('td', attrs={'class': 'time'}).find('h6').nextSibling

    d["total_time"] = ' '.join(total_time.string.split())
##        print ' '.join(total_time.string.split())

    return d
