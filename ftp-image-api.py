import os
import ssl
import logging
from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import socket

# Configuration
image_directory = "/home/ftpserveradmin/upload/"
http_port = 8089
https_port = 8087

# Read from environment variables
cert_file = os.getenv("SSL_CERT_FILE", "path/to/dev/fullchain.pem")
key_file = os.getenv("SSL_KEY_FILE", "path/to/dev/privkey.pem")

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - %s" % (self.client_address[0], format % args))

class RedirectHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_response(301)
            self.send_header('Location', f'https://{self.server.server_address[0]}:{https_port}{self.path}')
            self.end_headers()
        else:
            super().do_GET()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def run():
    httpd = ThreadedHTTPServer(('0.0.0.0', http_port), RedirectHTTPRequestHandler)
    logging.info(f"Serving HTTP on http://{socket.gethostname()}:{http_port} (redirecting to HTTPS)")

    # SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)

    httpsd = ThreadedHTTPServer(('0.0.0.0', https_port), CustomHTTPRequestHandler)
    httpsd.socket = context.wrap_socket(httpsd.socket, server_side=True)
    logging.info(f"Serving files securely on https://{socket.gethostname()}:{https_port}/")

    try:
        from threading import Thread
        Thread(target=httpd.serve_forever).start()
        httpsd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server stopped by user.")
    except Exception as e:
        logging.error(f"Server encountered an error: {e}")
    finally:
        httpd.server_close()
        httpsd.server_close()
        logging.info("Server has been shut down.")

if __name__ == "__main__":
    run()
