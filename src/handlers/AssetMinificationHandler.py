from os import path

from google.appengine.ext import webapp
from google.appengine.api import memcache, urlfetch

from src.externs import closure, cssmin
from src.model import Defaults

import logging, urllib

TIMEOUT 		= 60 * 60 * 24 * 7
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
			
			response = ""
			
			compiled = ""
			
			if output is None:
				
				output = { "Content": "" }
				
				if files.endswith(".js"):
					
					output["Content-Type"] = "text/javascript"
					
					for f in files.split(","):
						
						f = f.strip();
						
						filePath = path.join(JS, f)
						
						if path.exists(filePath):
							
							response += open(filePath).read()
						
						else:
							
							logging.error("Path does not exist: %s", filePath)
					
					if len(response) > 0:
						
						compiled = closure.compile(response)
						
						if compiled is None:
							
							compiled = response
					
					output["Content"] = compiled
				
				elif files.endswith(".css"):
					
					output["Content-Type"] = "text/css"
					
					for f in files.split(","):
						
						f = f.strip()
						
						filePath = path.join(CSS, f)
						
						if path.exists(filePath):
							
							response += open(filePath).read()
						
						else:
							
							logging.error("Path does not exist: %s", filePath)
					
					if len(response) > 0:
						
						compiled = cssmin(response, 3)
						
						if compiled is None:
							
							compiled = response
					
					output["Content"] = compiled
				
				if Defaults.USE_MEMCACHE and not memcache.add(files, output, TIMEOUT):
					
					logging.error("Could not save value into memcached for key %s" % files)
				
		
		self.response.headers['Content-Type'] = output["Content-Type"]
		
		self.response.out.write(output["Content"])
				
				