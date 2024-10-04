from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyRequesthandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'to-do.html'
        return super().do_GET()
    
PORT = 8000
httpd = HTTPServer(('localhost', PORT),MyRequesthandler)

print(f"Serving on port {PORT}")
httpd.serve_forever()