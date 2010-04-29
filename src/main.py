#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from src.handlers import PageRequestHandler, AssetMinificationHandler

if __name__ == '__main__':

	application = webapp.WSGIApplication([('/minify/(.*)', AssetMinificationHandler),
										  ('/(.*)', PageRequestHandler)], debug=True)
	
	util.run_wsgi_app(application)
