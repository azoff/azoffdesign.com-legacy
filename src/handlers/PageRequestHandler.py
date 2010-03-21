from os import path
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from src.model import PageModel

TEMPLATE_PATH = path.join(path.join(path.dirname(path.dirname(path.dirname(__file__))), 'pages'), 'template.html')

class PageRequestHandler(webapp.RequestHandler):

  def get(self, url):

	model = PageModel.get(url)
	
	if not model["isCompiled"]:
		
		model["source"] = open(model["path"]).read()

	self.response.out.write(template.render(TEMPLATE_PATH, model))