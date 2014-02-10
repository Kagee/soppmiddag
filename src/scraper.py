import lxml.html
from lxml import etree
import urllib2
import logging

def scrape(url, user_agent) :
    headers = { 'User-Agent': user_agent }
    req = urllib2.Request(url, headers=headers)
    f = urllib2.urlopen(req)
    text = f.read()
    f.close()
    return text

def extractTable(root):
    for el in root.cssselect("div.content table.contentpaneopen table"):
        tableSource = lxml.html.tostring(el)
        if "Ukedag" in tableSource:
            return el        

def cleanup(table):
    etree.strip_tags(table,'span','strong','div', 'tbody')
    for tag in table.iter():
        for att in tag.attrib.keys():
            tag.attrib.pop(att)
        if tag.tag == "table": tag.set('border','1')
    return table;

def tds(td):
    tdstr = lxml.etree.tostring(td)
    cleaned = tdstr.replace('&#13;','').replace('&#160;', ' ').replace('/n', '').replace('</td>', '').replace('<td>', '').replace('<p>','').replace('<br />','<br>');
    cleaned = " ".join(cleaned.split())
    cleaned2 = cleaned.replace('</p>','<br>').replace('<br><br>','<br>').replace('> ','>').replace(' <','<');
    if cleaned2.endswith("<br>"):
        r =cleaned2[:-4];
    else: r = cleaned2;
    return br2eller(r);

def br2eller(s):
    numbr = s.count('<br>')
    s = s.replace("<br>", ", ", numbr-1);
    return s.replace("<br>", ", eller ").replace('m/', "med ");

def tableToDict(ctable):
    names = ['header','Mandag','Tirsdag','Onsdag','Torsdag', 'Fredag']
    d = {}
    trs = ctable.cssselect("tr");
    td = 0;
    for tr in range(0,6):
        d[names[tr]] = [tds(trs[tr][td]),tds(trs[tr][td+1]),tds(trs[tr][td+2])]
    return d;

def plainText(week, separator):
	#print week
	printout = "";
	for weekday in 'Mandag','Tirsdag','Onsdag','Torsdag', 'Fredag':
		for kantine in 1,2:
			week[weekday][kantine] = week[weekday][kantine].capitalize()
		f = lxml.html.fromstring(';'.join(week[weekday][1:3]))
		printout = printout + weekday + separator + f.text+"\n"
	return printout

