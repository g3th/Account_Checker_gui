# Drag, copy and paste colours from this list
# to colourize the GUI titles

import requests
from bs4 import BeautifulSoup as soup

def parse_and_store_500_colours():

	page='https://cloford.com/resources/colours/500col.htm'
	colour_list =[]
	request = requests.get(page)
	parse_request = soup(request.content,'html.parser')
	get_colours = parse_request.find_all('a',href=True)

	for i in get_colours:
		colour_list.append(str(i).split('>')[1].replace('</a','').replace(' ',''))
	del colour_list[0:11]
	del colour_list[-3:]
	return colour_list

colours = parse_and_store_500_colours()
print(colours)

