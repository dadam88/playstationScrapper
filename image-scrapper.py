import requests
from bs4 import BeautifulSoup
import sys
# -*- coding: utf-8 -*-
url = "https://en.wikipedia.org/wiki/Cool_Boarders"

r = requests.get(url)

soup = BeautifulSoup(r.content)

games = soup.select("td > i > a")

filename = "log-images.txt"

images = soup.select("td > a > img")	
image = images[0].get('src')
image = "https:" + image
description = soup.find_all('p')
# answer is description [1]
descripe = description[1]

with open(filename, "w") as f:


    f.write(image.encode("utf-8") + "\t")
    f.write(descripe.encode("utf-8") + "\n\n")
    
 



#selected works
#discography
#compositions
#Musical Works


