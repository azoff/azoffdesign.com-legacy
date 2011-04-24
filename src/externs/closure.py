from google.appengine.api import urlfetch
from src.model import Defaults
import logging
import urllib
import re

COMPILER_URL='http://closure-compiler.appspot.com/compile'

def compile(code):

	payload = urllib.urlencode([
		('js_code', code),
		('compilation_level', Defaults.COMPILE_MODE),
		('output_format', 'text'),
		('output_info', 'compiled_code'),
	])
	
	headers = { "Content-type": "application/x-www-form-urlencoded" }

	try:
		
		response = urlfetch.fetch(COMPILER_URL, payload, 'POST', headers).content
		
		if response.find("Error(") == 0:
			
			logging.error('Error returned from the closure compiler service: %s', response)
			
			response = code
		
		return response
		
	except Exception, e:
		
		logging.error('Error communicating with the closure compiler service: %s', e)
		
		return code