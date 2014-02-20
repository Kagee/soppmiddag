import importlib
import re

def getModule(sms):
	"""Verifies that the codeword is a valid module name
	:param sms: The complete SMS message
	:returns Module or None
	"""
	# Get (first) word
	word = sms.split(" ")[0].lower()	

	# maxlength of ten alafanumeric chars for word
	if not re.match(r"^[a-z0-9]{1,10}$", word):
		print "regexp failed"
		return None

	try:
		module = importlib.import_module(word, "smsmodules")
		return module
	except ImportError as e:
		print "module load failed: %s" % (e)
		return None

if __name__ == "__main__":
	print getModule("foo")
	print getModule("middag")
	print getModule("middag hil")
	print getModule("ymp3 https://www.youtube.com/watch?v=aWuDWUdjWH4")
	print getModule("asdfghjkloiu")
