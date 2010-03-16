from ConfigParser import ConfigParser
from os import path

ROOT = path.dirname(path.dirname(path.dirname(__file__)))
PAGES = path.join(ROOT, "pages.ini")

TITLE 			= "Azoff Design"
KEYWORDS		= "Azoff Design"
STYLES			= "reset.css, jquery-ui-1.8rc3.custom.css"
SCRIPTS			= "jquery-1.4.2.js, jquery-ui-1.8rc3.custom.js"

_map = {}

_parser = ConfigParser()

_parser.read(PAGES)

def _keyExists(section, key):
	return (_parser.has_option(section, key) and len(_parser.get(section, key)) > 0)

for page in _parser.sections():

	if _keyExists(page, "source"):
		source				= path.join(path.join(ROOT, "pages"), _parser.get(page, "source"))
		page 				= page.strip().lower() if page else ""
		model 				= {}
		model["source"]		= open(source).read();
		model["title"] 		= ("%s | %s" % (TITLE, _parser.get(page, "title"))) if _keyExists(page, "title") else TITLE
		model["keywords"] 	= ("%s, %s" % (KEYWORDS, _parser.get(page, "keywords"))) if _keyExists(page, "keywords") else KEYWORDS
		model["script"] 	= (("%s, %s" % (SCRIPTS, _parser.get(page, "script"))) if _keyExists(page, "script") else SCRIPTS).replace(" ", "")
		model["style"] 		= (("%s, %s" % (STYLES, _parser.get(page, "style"))) if _keyExists(page, "style") else STYLES).replace(" ", "")
		model["scripts"] 	= model["script"].split(",")
		model["styles"] 	= model["style"].split(",")
		model["isCompiled"] = _parser.getboolean(page, "compile") if _keyExists(page, "compile") else True

		_map[page] = model
	
		if(_keyExists(page, "default") and _parser.getboolean(page, "default")):
			_default = model
	
		if(_keyExists(page, "alias")):
			aliases = _parser.get(page, "alias").replace(" ", "").split(",")
			for alias in aliases:
				if alias:
					alias = alias.strip().lower()
					_map[alias] = model

def get(url):
	url = url.strip().lower() if url else ""
	
	if len(url) > 0:
		if _map.has_key(url):
			return _map[url]
		else:
			return _map["404"]
	else:
		return _default;