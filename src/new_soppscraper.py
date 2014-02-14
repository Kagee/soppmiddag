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
	return "andag" in lxml.html.tostring(plist[0]) and \
		"irsdag" in lxml.html.tostring(plist[1]) and \
		"nsdag" in lxml.html.tostring(plist[2]) and \
		"orsdag" in lxml.html.tostring(plist[3]) and \
		"redag" in lxml.html.tostring(plist[4])

def run(url):
	text = scraper.scrape(url, "Sopp-Middag-Scraper-hildenae-at-gmail-com")
	root = lxml.html.fromstring(text)
	ps = list_of_p(div(root))
	h = HTMLParser.HTMLParser()
	for el in ps:
		day = lxml.html.tostring(el).strip();
		day = h.unescape(day)
		day = re.sub(r"\xa0", ' ', day)
		day = re.sub(r"  ", '', day)
		day = re.sub(r"\x00d8", r"---", unicode(day))
		#dayEl = lxml.html.fromstring(day);
		#day = dayEl.text_content()
		print day
		#print ":".join("{0:x}".format(ord(c)) for c in day)
	print verify(ps)


print "HIG"
#run("http://sopp-no.herokuapp.com/spisesteder-gjovik")
run("http://localhost:8000/hig.html")
print "\nHIL"
run("http://localhost:8000/hil.html")
#run("http://sopp-no.herokuapp.com/spisesteder")
