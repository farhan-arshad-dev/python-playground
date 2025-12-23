from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests
        """
        # Access Request
        print("Request path:", self.path)
        print("Request headers:", self.headers)

        # Prepare Response
        self.send_response(200)  # HTTP status code
        self.send_header('Content-Type', 'text/plain')
        self.send_header('X-Custom-Header', 'MyHeaderValue')
        self.end_headers()

        # Write response body
        self.wfile.write(b"Hello from Python HTTP server!")

    def do_POST(self):
        """
        Handle POST requests
        """
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print("Received POST data:", post_data.decode('utf-8'))

        # Response
        self.send_response(201)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = b'{"status": "received"}'
        self.wfile.write(response)


def run(server_class=HTTPServer, handler_class=MyServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
