import twilio.twiml
import config
import logging
from SoppParser import SoppParser # parser for sopp.no
from WeekMenu import WeekMenu
from datetime import datetime, timedelta# To check the weekday
def handle(sms):
	resp = twilio.twiml.Response()

	# this will be an hour or two off (because it is UTC)
	# But let's assume nobody will check todays dish between 22:00 and 02:00
	weekday = datetime.now().weekday()
	if weekday > 4:
		msg = u"Det serveres ikke middag i kantinen p\u00E5 HiG p\u00E5 %s" % (u"l\u00F8rdag" if weekday == 5 else  u"s\u00F8ndag")
		resp.message(msg)
	else:
		hig = SoppParser(config.SOPP_HIG)
		q = WeekMenu.today()
		if q:
			logging.info("Cache hit")
			hig.setMenu(q.menu)
		else:
			logging.info("Cache miss")
			hig.scrape()
			hig.extract()
			hig.extract()
			hig.parse()
			w = WeekMenu(school='hig', source=hig.getSourceText(), menu=hig.getMenu())
			w.put()
		resp.message(hig.mergeDishes(weekday))
	return resp
