class StatusMessage:

	CODE_OK = 200
	CODE_PRECODITION_FAILED = 412
	CODE_NOT_IMPLEMENTED = 501
	CODE_INTERNAL_SERVER_ERROR = 500

	def __init__(self, code, title, message):
		self.code = code
		self.title = title
		self.message = message
		
	def asJson(self):
		return '{"code": %s, "title": "%s", "message": "%s"}' % (self.code, self.title.replace('"', '\\"'), self.message.replace('"', '\\"'))