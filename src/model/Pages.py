from ConfigParser import RawConfigParser
from os import path
from datetime import datetime
from time import strptime

from src.model import Defaults

ROOT = path.dirname(path.dirname(path.dirname(__file__)))
PAGES = path.join(ROOT, "pages.ini")

TITLE 			= Defaults.TITLE
DESCRIPTION		= Defaults.DESCRIPTION
KEYWORDS		= Defaults.KEYWORDS
STYLES			= Defaults.STYLES
SCRIPTS			= Defaults.SCRIPTS

_map = {}
_aliases = []
_projects = []

_parser = RawConfigParser()
_parser.read(PAGES)

def _keyExists(section, key):
	return (_parser.has_option(section, key) and len(_parser.get(section, key)) > 0)

def _getSummary(description):
	start = 350
	end = description.find(" ", start)
	return  "%s..." % description[0:end]

for page in _parser.sections():

	if _keyExists(page, "source"):
		page 				= page.strip().lower() if page else ""
		model 				= {}
		model["path"]		= path.join(path.join(ROOT, "pages"), _parser.get(page, "source"))
		model["keywords"] 	= ("%s,%s" % (KEYWORDS, _parser.get(page, "keywords"))) if _keyExists(page, "keywords") else KEYWORDS
		model["scripts"] 	= ("%s,%s" % (SCRIPTS, _parser.get(page, "scripts").replace(" ", ""))) if _keyExists(page, "scripts") else SCRIPTS
		model["styles"] 	= ("%s,%s" % (STYLES, _parser.get(page, "styles").replace(" ", ""))) if _keyExists(page, "styles") else STYLES
		model["title"]		= _parser.get(page, "title") if _keyExists(page, "title") else TITLE
		model["pageTitle"] 	= "%s | %s" % (TITLE, model["title"])
		model["description"]= _parser.get(page, "description") if _keyExists(page, "description") else DESCRIPTION
		model["debug"] = _parser.getboolean(page, "debug") if _keyExists(page, "debug") else False
		model["isProject"]	= _keyExists(page, "date")
		model["date"]		= datetime(*strptime(_parser.get(page, "date"), "%m/%d/%Y")[0:5]) if model["isProject"] else datetime.now()
		model["isDefault"]	= _parser.getboolean(page, "default") if _keyExists(page, "default") else False
		model["year"] 		= datetime.now().year
		model["scripts"] = model["scripts"].split(",")
		model["styles"] = model["styles"].split(",")

		_map[page] = model
		
		if model["isProject"]:
			model["link"] = "/%s" % page
			model["thumb"] = "/static/img/thumb-%s.jpg" % page
			model["summary"] = _getSummary(model["description"])
			_projects.append(model)
	
		if model["isDefault"]:
			_default = model
	
		if(_keyExists(page, "alias")):
			aliases = _parser.get(page, "alias").replace(" ", "").split(",")
			for alias in aliases:
				if alias:
					alias = alias.strip().lower()
					_map[alias] = model

_aliases = _map.keys();
_projects = sorted(_projects, key=lambda project: project["date"], reverse=True);				
_default["projects"] = _projects

def getAliases():
	return _aliases;

def getPage(url):
	url = url.strip().lower() if url else ""
	
	if len(url) > 0:
		if _map.has_key(url):
			return _map[url]
		else:
			return _map["404"]
	else:
		return _default;