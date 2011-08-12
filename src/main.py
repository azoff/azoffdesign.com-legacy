#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from src.handlers import PageRequestHandler, SitemapHandler

_mappings = [];
_mappings.append(('/sitemap.xml', SitemapHandler));
_mappings.append(('/(.*)', PageRequestHandler));

if __name__ == '__main__':

	application = webapp.WSGIApplication(_mappings, debug=True)
	
	util.run_wsgi_app(application)
