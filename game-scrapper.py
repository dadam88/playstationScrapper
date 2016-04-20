import requests
from bs4 import BeautifulSoup
import sys
# -*- coding: utf-8 -*-
url = "https://en.wikipedia.org/wiki/List_of_PSone_Classics_%28North_America%29"

r = requests.get(url)

soup = BeautifulSoup(r.content)

games = soup.select("td > i > a")

filename = "log-games.txt"

with open(filename, "w") as f:

    for game in games:
 
        f.write(game.get('title').encode("utf-8") + "\t")
        f.write(game.get('href').encode("utf-8") + "\n\n")
        
     



#selected works
#discography
#compositions
#Musical Works


