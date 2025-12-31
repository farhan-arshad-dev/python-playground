from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):

    def _read_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length).decode("utf-8")

    def _send_response(self, status=200, body="OK"):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body.encode())

    def do_GET(self):
        """
        Handle GET requests
        """
        # Access Request
        print("Request path:", self.path)
        print("Request headers:", self.headers)

        # Prepare Response
        self._send_response(200, "{'status': 'Hello from Python HTTP server!'}")

    def do_POST(self):
        """
        Handle POST requests
        """
        post_data = self._read_body()
        print("Received POST data:", post_data)

        # Response
        self._send_response(201, "{'status': 'received with post request'}")

    def do_PUT(self):
        body = self._read_body()
        print("PUT body:", body)

        self._send_response(200, "{'status': 'received with put request'}")

    def do_PATCH(self):
        body = self._read_body()
        print("PATCH body:", body)

        self._send_response(200, "{'status': 'received with patch request'}")


def run(server_class=HTTPServer, handler_class=MyServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
