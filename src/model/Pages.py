from ConfigParser import ConfigParser
from os import path
from datetime import datetime

from src.model import Defaults

ROOT = path.dirname(path.dirname(path.dirname(__file__)))
PAGES = path.join(ROOT, "pages.ini")

TITLE 			= Defaults.TITLE
DESCRIPTION		= Defaults.DESCRIPTION
KEYWORDS		= Defaults.KEYWORDS
STYLES			= Defaults.STYLES
SCRIPTS			= Defaults.SCRIPTS

_map = {}

_parser = ConfigParser()

_parser.read(PAGES)

def _keyExists(section, key):
	return (_parser.has_option(section, key) and len(_parser.get(section, key)) > 0)

for page in _parser.sections():

	if _keyExists(page, "source"):
		page 				= page.strip().lower() if page else ""
		model 				= {}
		model["path"]		= path.join(path.join(ROOT, "pages"), _parser.get(page, "source"))
		model["title"] 		= ("%s | %s" % (TITLE, _parser.get(page, "title"))) if _keyExists(page, "title") else TITLE
		model["keywords"] 	= ("%s,%s" % (KEYWORDS, _parser.get(page, "keywords"))) if _keyExists(page, "keywords") else KEYWORDS
		model["scripts"] 	= ("%s,%s" % (SCRIPTS, _parser.get(page, "scripts").replace(" ", ""))) if _keyExists(page, "scripts") else SCRIPTS
		model["styles"] 	= ("%s,%s" % (STYLES, _parser.get(page, "styles").replace(" ", ""))) if _keyExists(page, "styles") else STYLES
		model["description"]= _parser.get(page, "description") if _keyExists(page, "description") else DESCRIPTION
		model["isCompiled"] = _parser.getboolean(page, "compile") if _keyExists(page, "compile") else False
		model["year"] 		= datetime.now().year

		if not model["isCompiled"]:
			model["scripts"] = model["scripts"].split(",")
			model["styles"] = model["styles"].split(",")

		_map[page] = model
	
		if(_keyExists(page, "default") and _parser.getboolean(page, "default")):
			_default = model
	
		if(_keyExists(page, "alias")):
			aliases = _parser.get(page, "alias").replace(" ", "").split(",")
			for alias in aliases:
				if alias:
					alias = alias.strip().lower()
					_map[alias] = model

def getPage(url):
	url = url.strip().lower() if url else ""
	
	if len(url) > 0:
		if _map.has_key(url):
			return _map[url]
		else:
			return _map["404"]
	else:
		return _default;