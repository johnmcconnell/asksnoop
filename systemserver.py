import sys
import BaseHTTPServer
import cgi
import src.factcheck as fc
import json
from urlparse import urlparse, parse_qs
from SimpleHTTPServer import SimpleHTTPRequestHandler

class NLTKHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
	params = parse_qs(urlparse(s.path).query)
	phrase = fc.check(params['query'][0])
	s.wfile.write(json.dumps({'topics':phrase}))

HandlerClass = NLTKHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()


