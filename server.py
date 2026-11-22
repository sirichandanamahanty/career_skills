import os
import json
import http.server
import socketserver
from urllib.parse import urlparse

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CareerAIRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS for local testing
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ["/api/health", "/api/status"]:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "online",
                "service": "Career Skill Gap AI",
                "port": PORT
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return
        
        # Default route serves index.html
        if parsed.path in ["/", ""]:
            self.path = "/index.html"
            
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else "{}"
        try:
            data = json.loads(body)
        except Exception:
            data = {}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        if parsed.path == "/api/progress/save":
            resp = {"status": "success", "message": "Progress saved successfully"}
        elif parsed.path == "/api/ai/ask-mentor":
            role_name = data.get("role_name", "your target career")
            hrs = data.get("hours_per_week", 10)
            resp = {
                "answer": f"For {role_name} with {hrs} hrs/week:\n1. Focus first on your highest priority skill gap.\n2. Dedicate 60% of your time to theory and 40% to building real projects.\n3. Maintain consistent weekly study blocks."
            }
        else:
            resp = {"status": "ok"}

        self.wfile.write(json.dumps(resp).encode("utf-8"))

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), CareerAIRequestHandler) as httpd:
        print(f"Serving Career Skill Gap AI at http://localhost:{PORT}", flush=True)
        print(f"Also available at http://127.0.0.1:{PORT}", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    run()
