from os import path

from google.appengine.ext import webapp
from google.appengine.api import memcache, urlfetch

from src.externs import jsmin, cssmin, jspack

import logging, urllib

USE_MEMCACHE	= True
TIMEOUT 		= 60 * 60 * 24
ROOT 			= path.dirname(path.dirname(path.dirname(__file__)))
ASSETS 			= path.join(ROOT, "assets")
CSS 			= path.join(ASSETS, "css")
JS 				= path.join(ASSETS, "js") 

class AssetMinificationHandler(webapp.RequestHandler):

  def get(self, files):
    
	files = urllib.unquote(files).strip().replace(" ", "").lower()
	
	if len(files) > 0:
		
		output = memcache.get(files) if USE_MEMCACHE else None
		
		if output is None:
			
			output = { "Content": "" }
			
			if files.endswith(".js"):
				
				output["Content-Type"] = "text/javascript"

				for f in files.split(","):
					
					output["Content"] += open(path.join(JS, f)).read()
					
				output["Content"] = jspack(jsmin(output["Content"]))
				
			else:
				
				output["Content-Type"] = "text/css"
				
				for f in files.split(","):
					
					output["Content"] += open(path.join(CSS, f)).read()
					
				output["Content"] = cssmin(output["Content"], 3)					

			if not memcache.add(files, output, TIMEOUT):

				logging.error("Could not save value into memcached for key %s" % files)	
				
				
		self.response.headers['Content-Type'] = output["Content-Type"]
		
		self.response.out.write(output["Content"])		
				
				