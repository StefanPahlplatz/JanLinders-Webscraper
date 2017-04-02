import urllib.request
from bs4 import BeautifulSoup
import db
import re
import progressbar as p
import time


# Replace null string with ''.
def xstr(s):
    if s is None:
        return ''
    return str(s)


# Download a page and parse it with BeautifulSoup
def download_url(url):
    # Retrieve the first main site.
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    return BeautifulSoup(content, "html.parser")


print("""
   ___             _     _           _                 _    _      _                                        
  |_  |           | |   (_)         | |               | |  | |    | |                                       
    | | __ _ _ __ | |    _ _ __   __| | ___ _ __ ___  | |  | | ___| |__  ___  ___ _ __ __ _ _ __   ___ _ __ 
    | |/ _` | '_ \| |   | | '_ \ / _` |/ _ \ '__/ __| | |/\| |/ _ \ '_ \/ __|/ __| '__/ _` | '_ \ / _ \ '__|
/\__/ / (_| | | | | |___| | | | | (_| |  __/ |  \__ \ \  /\  /  __/ |_) \__ \ (__| | | (_| | |_) |  __/ |   
\____/ \__,_|_| |_\_____/_|_| |_|\__,_|\___|_|  |___/  \/  \/ \___|_.__/|___/\___|_|  \__,_| .__/ \___|_|   
                                                                                           | |              
                                                                                           |_|              """)
# Start timer.
start = time.time()

# Get the main page.
soup = download_url("http://www.janlinders.nl/ons-assortiment.html")

# Get all container that has all group links.
catalog_subnav = soup.find("div", {"id": "catalog_subnav"})
catalogs = catalog_subnav.findAll("li")

# Get all group links.
links = []
for i in range(0, len(catalogs)):
    for link in catalogs[i].findAll("a", href=True):
        links.append(str.format("http://www.janlinders.nl/" + link['href']))

# Database instance.
db = db.Database()

for j in range(0, len(links)):
    # Print progress.
    p.Progressbar.print_progress(j, len(links), prefix="Progress:", suffix="Complete", bar_length=50)

    # Download the current page.
    soup = download_url(links[j])

    # Find all products on the page.
    mydivs = soup.findAll("div", {"class": "item_container"})

    # Get the details for each product.
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
            # Format of the string is something like "15.24"
            matches = re.split("\.", pricebig)
            pricesmall = int(matches[1])
            pricebig = int(matches[0])
        else:
            # Price is split up in two elements.
            pricebig = int(pricebig)
            pricesmall = int(mydivs[i].find("span", {"class": "small"}).string)

        price = round(pricebig + (pricesmall / 100), 2)

        # To view the items that are scraped uncomment the next line.
        # print(name, price, group)

        db.insert(name, price, brand, weight, group)

# Show the total time.
end = time.time()
print(str.format("Total time elapsed: {0} seconds", round(end - start)))
