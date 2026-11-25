import json

from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer
)

from lambda_function import lambda_handler


class Handler(BaseHTTPRequestHandler):

    def _run(self, method):
        length = int(
            self.headers.get(
                "Content-Length",
                0
            )
        )

        body = (
            self.rfile.read(
                length
            ).decode("utf-8")
            if length
            else None
        )

        event = {
            "rawPath": self.path,
            "body": body,
            "requestContext": {
                "http": {
                    "method": method
                }
            },
        }

        result = lambda_handler(
            event,
            None
        )

        self.send_response(
            result["statusCode"]
        )

        for key, value in result[
            "headers"
        ].items():
            self.send_header(
                key,
                value
            )

        self.end_headers()

        self.wfile.write(
            result["body"].encode(
                "utf-8"
            )
        )

    def do_GET(self):
        self._run("GET")

    def do_POST(self):
        self._run("POST")


HTTPServer(
    (
        "127.0.0.1",
        8000
    ),
    Handler
).serve_forever()