#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lxml.html # parsing html
from lxml.html.clean import Cleaner
import scraper
import re
import HTMLParser
def div(root):
	return root.cssselect("div.module-article.turkis.clearfix")

def list_of_p(div):
	if len(div) == 1:
		return div[0].cssselect("p")
	else :
		return [] # 500

def verify(plist):
	return None != (re.search(r"(?i)mandag",  lxml.html.tostring(plist[0])) and \
		re.search(r"(?i)tirsdag", lxml.html.tostring(plist[1])) and \
		re.search(r"(?i)onsdag", lxml.html.tostring(plist[2])) and \
		re.search(r"(?i)torsdag", lxml.html.tostring(plist[3])) and \
		re.search(r"(?i)fredag", lxml.html.tostring(plist[4])))

def run(url):
	text = scraper.scrape(url, "hildenae-at-gmail.com-soppmiddagscraper")
	root = lxml.html.fromstring(text)
	ps = list_of_p(div(root))
	h = HTMLParser.HTMLParser()
	menu = {}
	weekday = 0
	for el in ps:
		# convert from HTML to string as we need to look at the tags
		day = lxml.html.tostring(el).strip();
		day = h.unescape(day) # Resolve html entitites to characters
		day = re.sub(r"\xa0", ' ', day) # Remove nonbreaking spaces
		day = re.sub(r"  ", '', day) # Remove double spaces

		# Insert a newline before any capital characters after a <br>|<br />|<br/>
		# This seems like the best way to differenciate between <br>s because
		# the name of the dish was to long, and <br>s to indicate a new dish
		day = re.sub(r"<br[ ]*[/]*>[ ]*([A-Z\xC6\xD8\xC5])", r"\n\1", day)
		dayEl = lxml.html.fromstring(day); # Convert back to HTML/lxml
		day = dayEl.text_content() # Get only the text content (removing any <p>, <br> etc)
		lines = day.split("\n") # Dishes are separated by newline
		day, firstDish = lines[0].split(":") 	# The day of week and first dish is on the same line,
												# but separated by a :
		lines[0] = firstDish.strip()
		dishes = [line.strip() for line in lines] # Remove extra whitespace around text.
		print day + ":", " eller ".join(dishes)
		menu[weekday] = dishes;
		weekday += 1
	print menu
	print verify(ps)


print "HIG"
#run("http://www.sopp.no/spisesteder-gjovik")
run("http://localhost:8000/hig.html")
print "\nHIL"
run("http://localhost:8000/hil.html")
#run("http://www.sopp.no/spisesteder")
