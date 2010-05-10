from os import path

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from src.model import Pages

SITEMAP_PATH = path.join(path.join(path.dirname(path.dirname(path.dirname(__file__))), 'pages'), 'sitemap.xml')

class SitemapHandler(webapp.RequestHandler):
	
	def get(self):

		model = { 'aliases': Pages.getAliases() }

		self.response.headers['Content-Type'] = "text/xml";

		self.response.out.write(template.render(SITEMAP_PATH, model))