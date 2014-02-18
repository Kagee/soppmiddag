from google.appengine.ext import ndb
from datetime import datetime

class WeekMenu(ndb.Model):
	school = ndb.StringProperty()
	source = ndb.TextProperty()
	menu = ndb.JsonProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)

	@classmethod
	def today(cls):
		result = cls.query().order(-cls.datetime).fetch(1)
		if len(result) == 1 and result[0].datetime.date() == datetime.today().date():
			return result[0]
		else:
			return False

