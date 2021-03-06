from os import path

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from src.model import Pages, Handlers

TEMPLATE_PATH = path.join(path.join(path.dirname(path.dirname(path.dirname(__file__))), 'pages'), 'template.html')

class PageRequestHandler(webapp.RequestHandler):

  def get(self, url):

	model = Pages.getPage(url)
	path = model["path"];
	
	if path.startswith('http'):
		
		self.response.headers["Location"] = path
		
		self.response.set_status(301);
		
	else:
		
		if model["debug"] or ("source" not in model):
			
			model["source"] = template.render(path, model)
			
		self.response.out.write(template.render(TEMPLATE_PATH, model))
	
  def post(self, url):
	
	handler = Handlers.getHandler(url)

	status = handler.process(self.request)
	
	self.response.headers['Content-Type'] = "application/json"

	self.response.out.write(status.asJson())
		
		