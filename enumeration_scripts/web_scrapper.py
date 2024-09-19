#!/usr/bin/python
# run "pip install lxml requests" before running
# this uses XPATH to grab strings
import lxml.html
import requests

page = requests.get('http://quotes.toscrape.com') # Default url, replace as needed
tree = lxml.html.fromstring(page.content)

# Specifies strings to grab
authors = tree.xpath('//small[@class="author"]/text()')
print ('Authors: ',authors)
