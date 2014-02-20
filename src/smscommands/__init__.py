import importlib
import re
import logging

def getModule(sms):
	"""Verifies that the codeword is a valid module name
	:param sms: The complete SMS message
	:returns Module or None
	"""
	# Get (first) word
	word = sms.split(" ")[0].lower()	

	# maxlength of ten alafanumeric chars for word
	if not re.match(r"^[a-z0-9]{1,10}$", word):
		logging.info("Regexp failed for command: %s" % (word))
		return None
	try:
		module = importlib.import_module("." + word, "smscommands")
		return module
	except ImportError as e:
		logging.info("Module load failed: %s" % (e))
		return None
