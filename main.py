from http.server import SimpleHTTPRequestHandler, HTTPServer

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('0.0.0.0', 9090)  # Listen on all interfaces, port 9090
    httpd = server_class(server_address, handler_class)
    print("Serving Hello World on port 9090...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Create a simple Hello World page
    with open("index.html", "w") as f:
        f.write("<h1>Hello World</h1>")

    run()
