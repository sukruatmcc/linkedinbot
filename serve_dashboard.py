#!/usr/bin/env python3
"""Basit HTTP server - Dashboard'u görüntülemek için"""

import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Dashboard çalışıyor: http://localhost:{PORT}/dashboard.html")
    print("Durdurmak için Ctrl+C")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Dashboard kapatıldı")
