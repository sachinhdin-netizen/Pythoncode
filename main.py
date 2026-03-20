from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello World</h1>")

def run():
    server_address = ('0.0.0.0', 9090)  # Listen on all interfaces
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving Hello World on port 9090...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
