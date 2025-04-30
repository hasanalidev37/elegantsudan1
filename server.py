from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import os

PORT = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path.startswith('/'):
            path = path[1:]
        if not path or path.endswith('/'):
            path = 'index.html'
        return path

Handler = CustomHandler

with HTTPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()