from os import path

from google.appengine.ext import webapp
from google.appengine.api import memcache, urlfetch

from src.externs import jsmin, cssmin, jspack
from src.model import Defaults

import logging, urllib

TIMEOUT 		= 60 * 60 * 24
ROOT 			= path.dirname(path.dirname(path.dirname(__file__)))
ASSETS 			= path.join(ROOT, "assets")
CSS 			= path.join(ASSETS, "css")
JS 				= path.join(ASSETS, "js") 

class AssetMinificationHandler(webapp.RequestHandler):

  def get(self, files):

	files = urllib.unquote(files)
	
	if len(files) > 0:
		
		output = { }
		
		if files == "flush":
			
			output["Content-Type"] = "text/plain"
			
			if memcache.flush_all():
			
				output["Content"] = "OK"
			
			else:
				
				output["Content"] = "ERR"
			
		else:
		
			output = memcache.get(files) if Defaults.USE_MEMCACHE else None
		
			if output is None:
			
				output = { "Content": "" }
			
				if files.endswith(".js"):
				
					output["Content-Type"] = "text/javascript"

					for f in files.split(","):
					
						f = f.strip();
					
						output["Content"] += open(path.join(JS, f)).read()
					
					output["Content"] = jspack(jsmin(output["Content"]))
				
				else:
				
					output["Content-Type"] = "text/css"
				
					for f in files.split(","):
					
						f = f.strip()
					
						output["Content"] += open(path.join(CSS, f)).read()
					
					output["Content"] = cssmin(output["Content"], 3)					

				if Defaults.USE_MEMCACHE and not memcache.add(files, output, TIMEOUT):

					logging.error("Could not save value into memcached for key %s" % files)	
				
				
		self.response.headers['Content-Type'] = output["Content-Type"]
		
		self.response.out.write(output["Content"])		
				
				