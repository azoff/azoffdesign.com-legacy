from google.appengine.api import urlfetch
from src.model import Defaults
import urllib

COMPILER_URL='http://closure-compiler.appspot.com/compile'

def compile(code):
    
    payload = urllib.urlencode([
        ('js_code', code),
        ('compilation_level', Defaults.COMPILE_MODE),
        ('output_format', 'text'),
        ('output_info', 'compiled_code'),
    ])

    headers = { "Content-type": "application/x-www-form-urlencoded" }
    
    response = urlfetch.fetch(COMPILER_URL, payload, 'POST', headers)
    
    return response.content