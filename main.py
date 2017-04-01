import urllib.request
from bs4 import BeautifulSoup
import db
import re

def xstr(s):
    if s is None:
        return ''
    return str(s)

# Retrieve the first main site.
opener = urllib.request.FancyURLopener({})
url = "http://www.janlinders.nl/ons-assortiment.html"
f = opener.open(url)
content = f.read()

# Parse the html code.
soup = BeautifulSoup(content, "html.parser")

# Get all links that contain products.
catalog_subnav = soup.find("div", {"id": "catalog_subnav"})
catalogs = catalog_subnav.findAll("li")
links = []
for i in range(0, len(catalogs)):
    for link in catalogs[i].findAll("a", href=True):
        links.append(str.format("http://www.janlinders.nl/" + link['href']))

# Database reference.
db = db.Database()

for j in range(0, len(links)):
    # Print progress.
    percentage = round(j / len(links) * 100, 2)
    print(str(percentage) + "%")

    # Retrieve the first main site.
    opener = urllib.request.FancyURLopener({})
    f = opener.open(links[j])
    content = f.read()

    # Parse the html code.
    soup = BeautifulSoup(content, "html.parser")

    # Find all elements.
    mydivs = soup.findAll("div", {"class": "item_container"})

    # Get the details for each element.
    for i in range(0, len(mydivs)):
        # Get the group name.
        group = soup.find("h1").string

        # Get the name.
        name = mydivs[i].findAll(['title', 'a'])[1].get('title').rstrip()

        # Get the brand.
        brand = xstr(mydivs[i].find('span', {"class": "teaser"}).string).rstrip()

        # Get the weight.
        weight = mydivs[i].find('span', {"class": "inhoud"}).string.rstrip()

        # Get the price.
        pricebig = mydivs[i].find("span", {"class": "big"}).string
        if re.match("^\d+\.\d+$", pricebig):
            matches = re.split("\.", pricebig)
            pricesmall = int(matches[1])
            pricebig = int(matches[0])
        else:
            pricebig = int(pricebig)
            pricesmall = int(mydivs[i].find("span", {"class": "small"}).string)
        price = round(pricebig + (pricesmall / 100), 2)

        print(name, price, group)

        query = "INSERT INTO products (name, price, brand, weight, `group`) VALUES ('" + name + "', " + str(price) + ", '" + brand + "', '" + weight + "', '"+group+"')"
        db.insert(query)
