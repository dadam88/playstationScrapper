import requests
from bs4 import BeautifulSoup
import sys
import time
import json
# -*- coding: utf-8 -*-
filename = "log-games.txt"

data = {}

with open(filename, "r") as f:

	n = 0
	for line in f:
		currentwork = line
		# File stored in this format
		# Title Of A Piece /wiki

		# Find index of / to grab rest of url string
		url_start = currentwork.find("/")

		# Grab name/title of piece working backwards from slash to beginning
		# striping whitespace out
		name = currentwork[:url_start].strip()
		urlcurrent = currentwork[url_start:].strip()

		url =  "https://en.wikipedia.org" + urlcurrent

		# Time to scrap!
		r = requests.get(url)
		soup = BeautifulSoup(r.content)

		# Get data
		images = soup.select("td > a > img")
			
		try:
			image = images[0].get('src')
			image = "https:" + image
		except IndexError:
		    image = 'null'

		# description = soup.find_all('p')

		# try:
		#     descripe = description[1]
		# except IndexError:
		#     descripe = 'null'

		data[name] = image
		# time.sleep(.5) # to not get blacklisted
	

	with open('final_results.json', 'w') as result_file:
		json.dump(data, result_file)
		
		


 


