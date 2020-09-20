import http.server 
import socketserver 

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Musicle is running on port", PORT)
    print("You can see the local host here 127.0. 0.1.")
    httpd.serve_forever()