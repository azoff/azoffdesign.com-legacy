import logging

from urllib import quote

from google.appengine.api import mail, urlfetch

from src.util import StatusMessage

from src.model import Defaults

class ContactFormHandler:
	
	def process(self, request):
		
		sender = request.get("sender")
		
		body = request.get("body")
		
		recaptcha_data = "privatekey=6Ldc9QsAAAAAAP81ZNYlFl28AarMOvIhzAwsBpUp&remoteip=%s&challenge=%s&response=%s" % (quote(request.remote_addr), quote(request.get("recaptcha_challenge_field")), quote(request.get("recaptcha_response_field")))
		
		if len(body) > 0 and len(sender) > 0 and mail.is_email_valid(sender):
		
			output = None
			
			try:
				
				output = urlfetch.fetch("http://api-verify.recaptcha.net/verify", recaptcha_data, 'POST')
				
				if output.status_code == 200:
					
					status = output.content.split("\n");
					
					if status[0] == "true":
						
						mail.send_mail(sender, Defaults.EMAIL, "Azoff Design - Contact Form Submission", body)

						return StatusMessage(
							StatusMessage.CODE_OK,
							"Email Sent!", 
							"Your email has been sent, thank you for your inquiry")
						
					else:
						
						return StatusMessage(
							StatusMessage.CODE_INTERNAL_SERVER_ERROR,
							"Validation Failed!", 
							"It seems that the response you provided for the 'are you human' response was incorrect. Please review your submission and try again")
					
				else:
					
					logging.error("Recaptcha server errored out: '%s'" % output.content)
					
					return StatusMessage(
						StatusMessage.CODE_INTERNAL_SERVER_ERROR,
						"Oh No!", 
						"The server was unable to reach the captcha validation service. As a result your request could not be validated. Please try again later.")
				
			except:
				
				logging.error("Unable to communicate with the recaptcha server, exception raised!")
				
				return StatusMessage(
					StatusMessage.CODE_INTERNAL_SERVER_ERROR,
					"Oh No!", 
					"The server was unable to reach the captcha validation service. As a result your request could not be validated. Please try again later.")
			
		else:
			
			return StatusMessage(
				StatusMessage.CODE_PRECODITION_FAILED,
				"Oh No!", 
				"There seems to have been an error with your request. Please make sure you have provided a valid email address and message then try again.")