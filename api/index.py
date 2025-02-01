import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# List of student marks as dictionaries
student_marks = [
    {"name": "hPZTeg", "marks": 33},
    {"name": "ucIF7L", "marks": 60},
    {"name": "FHpnPdi", "marks": 38},
    {"name": "Y5E6KJQsF", "marks": 66},
    {"name": "B7Bfrp7", "marks": 13},
    {"name": "0e4ovvtj", "marks": 82},
    {"name": "4lTJW", "marks": 40},
    {"name": "2vL", "marks": 42},
    {"name": "NSVK", "marks": 57},
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Parse query parameters correctly
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            names = query_components.get("name", [])  # Extract list of names
            
            marks_list = []
            
            for name in names:
                student = next((s for s in student_marks if s["name"] == name), None)
                marks_list.append(student["marks"] if student else "Not Found")

            response = {"marks": marks_list}

            # Send JSON response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        
        except Exception as e:
            # Catch any runtime errors and return a proper error message
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"error": "Internal Server Error", "message": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
