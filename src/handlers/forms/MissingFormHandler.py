from src.util import StatusMessage

class MissingFormHandler:
	
	def process(request):
		
		return StatusMessage(StatusMessage.CODE_NOT_IMPLEMENTED, "No handler found!", "No form handler found for this request!")