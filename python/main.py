"""
Json http server
"""
import json
from http import HTTPStatus
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import Optional


class JSONHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Json http request handler"""

    def do_GET(self) -> None:
        """
        Http get method
        :return:
        """
        print(self.headers)
        data = {
            'status': True,
            'headers': dict(self.headers),
        }

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(data).encode('utf-8'))


def run(port: Optional[int] = 8084) -> None:
    """
    Run http server
    :param port:
    :return:
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, JSONHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()