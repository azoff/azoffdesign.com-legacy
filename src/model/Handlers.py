from src.handlers.forms import *

def getHandler(name):
	
	handler = MissingFormHandler()
	
	if name == "contact":
		
		handler = ContactFormHandler()
		
	return handler 