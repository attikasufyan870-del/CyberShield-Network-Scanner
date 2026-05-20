import socket
import sys
from datetime import datetime

# Ports ki dictionary taake tool ko pata ho kaun sa port kya kaam karta hai
PORT_SERVICES = {
    21: "FTP (File Transfer - Unencrypted, High Risk!)",
    22: "SSH (Secure Shell - Remote Access)",
    23: "Telnet (Remote Management - Insecure, Critical Risk!)",
    25: "SMTP (Email Routing)",
    80: "HTTP (Web Traffic - Unencrypted)",
    443: "HTTPS (Secure Web Traffic - Encrypted)",
    8080: "HTTP-Proxy / Alternate Web Port"
}

def get_ai_advice(port):
    """Open ports ke liye intelligent security advice generator"""
    advice = {
        21: "AI Advice: Close FTP if not needed. Use SFTP (Port 22) for secure file sharing.",
        22: "AI Advice: Ensure strong SSH passwords or SSH Keys. Change default port to prevent brute-force.",
        23: "AI Advice: SHUT DOWN TELNET IMMEDIATELY! It sends data in clear text. Use SSH instead.",
        25: "AI Advice: Verify if an authorized mail server is running. Restrict unauthorized relaying.",
        80: "AI Advice: Website traffic is unencrypted. Migrate your web server to HTTPS (Port 443).",
        443: "AI Advice: Secure port, but monitor SSL/TLS certificates regularly for vulnerabilities.",
        8080: "AI Advice: Often used for testing. Ensure it requires strict login authentication."
    }
    return advice.get(port, "AI Advice: Unknown service on open port. Investigate network logs.")

def start_scanner():
    target_host = input("Enter Target IP Address or Website (e.g., 127.0.0.1): ")
    
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("\n[!] Invalid Hostname/IP. Exiting...")
        sys.exit()

    print("-" * 65)
    print(f"CyberShield AI-Ready Scanner Target: {target_ip} ({target_host})")
    print(f"Time Started: {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
    print("-" * 65)

    # Ports list jo check karni hai
    ports_to_scan = [21, 22, 23, 25, 80, 443, 8080]

    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5) # Thoda extra timeout stability ke liye
        
        result = s.connect_ex((target_ip, port))
        service_name = PORT_SERVICES.get(port, "Unknown Service")
        
        if result == 0:
            print(f"[ * ] Port {port} ({service_name}): OPEN ⚠️")
            # AI Advice print karna
            print(f"      👉 {get_ai_advice(port)}\n")
        else:
            print(f"[   ] Port {port}: Closed")
            
        s.close()

    print("-" * 65)
    print("[+] Scan Completed Successfully!")

if __name__ == "__main__":
    start_scanner()
