 🕵️ GhostTrack Pro

**GhostTracker Pro** is an advanced OSINT (Open Source Intelligence) and educational tracking tool designed for cybersecurity professionals, researchers, and ethical hackers. It combines traditional information gathering with a **real-time GPS phishing module** to demonstrate how location data can be captured via social engineering.

> **⚠️ DISCLAIMER:** This tool is for **educational purposes and authorized testing only**.  
> - Do not use this to track individuals without their explicit consent.  
> - Unauthorized tracking may violate privacy laws and computer misuse acts in your jurisdiction.  
> - The developer is not responsible for misuse of this tool.

## 🚀 Capabilities

### 1. IP Information Gathering
- Retrieves public registration data for any IP address.
- **Data Provided:** Country, City, ISP, Organization, ASN, Timezone, and approximate region.
- **Limitation:** Provides registration info, **not** real-time GPS location.

### 2. Phone Number Intelligence
- Analyzes phone numbers for validity and carrier information.
- **Data Provided:** Carrier name, registered region/country, line type (mobile/fixed), and validity status.
- **Limitation:** Cannot track real-time GPS location of a phone number without a warrant or spyware.

### 3. Username OSINT
- Checks the existence of a username across major social media platforms (Facebook, Instagram, Twitter, etc.).
- Helps identify a target's digital footprint.

### 4. 🌍 Live GPS Tracker (NEW & Advanced)
- **How it works:** Creates a local web server that generates a "trap" link (e.g., a fake security alert page).
- **The Attack:** When the target clicks the link and grants location permission, their **exact real-time GPS coordinates**, device info, and IP address are sent to your terminal.
- **Use Case:** Demonstrates the dangers of granting location permissions to unknown links.
- **Requirement:** For remote targets (outside your WiFi), this feature requires a tunneling service like **Ngrok** or **Localxpose** to expose your local server to the internet.

---

## 📋 Requirements
- **Python 3.x** (Required)
- **Operating System:** Linux (Kali, Ubuntu, etc.) or Android (Termux).
- **Dependencies:**
  - `requests` (For API calls)
  - `phonenumbers` (For phone analysis)
  - `flask` (For the Live GPS Tracker server)

---

## 🛠️ Installation & Setup

### Option A: Kali Linux / Parrot OS / Ubuntu

1. **Update your system:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python and Git:**
   ```bash
   sudo apt install python3-pip git -y
   ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/akramlatif/GhostTrackerPro.git
   cd GhostTrackerPro
   ```

4. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the tool:**
   ```bash
   python3 GhostTrackerPro.py
   ```

### Option B: Termux (Android)

> **Note:** Do not use the Play Store version of Termux. Download it from F-Droid or the official GitHub repository, as the Play Store version is outdated.

1. **Update packages:**
   ```bash
   pkg update && pkg upgrade
   ```

2. **Install Python and Git:**
   ```bash
   pkg install python git
   ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/akramlatif/GhostTrackerPro.git
   cd GhostTrackerPro
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the tool:**
   ```bash
   python GhostTrackerPro.py
   ```

---

## 🌐 How to Use the Live GPS Tracker (Important)

The Live GPS Tracker (Option 5) works in two scenarios:

### Scenario 1: Local Network (Same WiFi)
- If you and the target are connected to the same WiFi network:
  - Run Option 5.
  - Copy the `http://192.168.x.x:5000` link provided.
  - Send it to the target device on the same network.
- If they click and allow location, you will see their coordinates.

### Scenario 2: Remote Network (Internet)
- If the target is on mobile data or a different network, your local server is not visible to them. You must use a tunneling service to expose your local port.

**Using Ngrok (Recommended):**
1. Sign up at [ngrok.com](https://ngrok.com) to get an auth token.
2. Install Ngrok:
   - **Kali:** `sudo apt install ngrok` (or download from official site)
   - **Termux:** `pkg install ngrok` (if available) or download the binary.
3. Link your account:
   ```bash
   ngrok config add-authtoken <YOUR_TOKEN>
   ```
4. Run the tunnel:
   ```bash
   ngrok http 5000
   ```
5. Ngrok will provide an `https://...` link. Use this link instead of the local IP.
6. Send this HTTPS link to the target. When they click and grant permission, you will receive their location.

---

## ❓ FAQ & Limitations

**Q:** Can I track a phone's real-time location just by entering the number?  
**A:** No. It is technically impossible to get real-time GPS from a phone number alone without carrier access (warrant) or installing spyware. This tool provides carrier/registration info only. For real-time GPS, you must use the Live GPS Tracker feature, which requires the target to click a link and grant permission.

**Q:** Can I track someone's IP to their exact house?  
**A:** No. IP addresses only reveal the location of the ISP's server (City/Region), not a specific house or person.

**Q:** Why do I need Flask?  
**A:** Flask is required to run the local web server for the Live GPS Tracker feature. Without it, Option 5 will not work.

**Q:** Is this legal?  
**A:** Yes, for educational purposes and authorized testing (e.g., testing your own devices or with written permission). Using it to track someone without consent may be illegal in your country.

---

## 📂 File Structure

```
GhostTrackPro/
├── GhostTrackPro.py      # Main script
├── requirements.txt      # Dependencies
├── README.md             # This file
└── logs/                 # (Auto-created) Stores captured data
```

> **Note:** Unlike other tools, this project does not require a separate `templates/index.html` file. The HTML template for the phishing page is embedded directly within the Python script for ease of use and portability. You do not need to create any extra files.

---

## 📜 License

This project is licensed for educational use only. By using this tool, you agree to comply with all local and international laws regarding privacy and data protection.
 
**Version:** 2.0 (Pro)
```
