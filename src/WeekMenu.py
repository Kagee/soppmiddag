from google.appengine.ext import ndb

class WeekMenu(ndb.Model):
	school = ndb.StringProperty()
	source = ndb.TextProperty()
	menu = ndb.JsonProperty()
	datetime = ndb.DateTimeProperty(auto_now_add=True)
