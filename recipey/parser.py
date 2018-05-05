import GeniusKitchenScraper as gks
import os
import json
import urllib

path = "C:/Python27/recipey/GeniusKitchen/"

for file in os.listdir(path):

    try:
        recipe = (gks.scrape("file:///" + path + file.replace(' ', "%20")))
    except:
        print "Could not parse %s", file

    with open('recipes-GeniusKitchen', 'a+') as f:
        f.write(json.dumps(recipe) + ",")
print 'Saved file %s' % 'recipes-GeniusKitchen'
