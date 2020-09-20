import http.server 
import socketserver 

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Musicle is running on port", PORT)
    print("You can see the local host here http://127.0.0.1:8080/")
    httpd.serve_forever()

##you can see the website by typing "python3 server.py" in the terminal 