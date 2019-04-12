from lxml import html
import requests

response = requests.get('https://stats.nba.com/player/201566/')
doc = html.fromstring(response.text)

tag1 = doc.cssselect('div.player-stats.n-p')[0].text_content()

tag2 = doc.cssselect('span.player-stats__stat-value')[0].text_content()
tag3 = doc.cssselect('div.player-stats__reb')[0].text_content()
tag4 = doc.cssselect('div.player-stats__ast')[0].text_content()

print()
print("Russell Westbrook Current Stats and Info: ", end = '')
print()
print(tag1.strip())
print()
#print("Russell WestBrook's current PPG average:", tag2.strip())
#print("Russell WestBrook's current REB average:", tag3.strip())
#print("Russell WestBrook's current AST average:", tag4.strip())
#print()


'''
from lxml import html
import requests
response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
doc = html.fromstring(response.text)
title = doc.cssselect('h3.dataset-heading')[0].text_content()
print("The name of the most recently added dataset on data.gov:")
print(title.strip())
'''
