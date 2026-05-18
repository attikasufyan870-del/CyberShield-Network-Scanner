import socket
import sys
from datetime import datetime

# Simple Cyber Security Port Scanner for GitHub Hackathon Project

def start_scanner():
    print("-" * 50)
    print("Welcome to CyberShield: Security Port Scanner")
    print("-" * 50)
    
    # User se website ya IP address lena
    target_host = input("Enter Target IP Address or Website (e.g., 127.0.0.1): ")
    
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("\n[!] Invalid Hostname. Exiting...")
        sys.exit()

    print(f"\n[+] Scanning Target: {target_ip}")
    print(f"[+] Scan Started At: {str(datetime.now())}")
    print("-" * 50)

    # Makhsoos standard ports check karna (HTTP, FTP, SSH, etc.)
    ports_to_scan = [21, 22, 23, 25, 80, 443, 8080]
    
    try:
        for port in ports_to_scan:
            # Socket connection banana timeout ke sath
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # 1 second timeout
            
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[ * ] Port {port}: OPEN (Potential Risk!)")
            else:
                print(f"[   ] Port {port}: Closed")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[-] Exiting Script...")
        sys.exit()
        
    print("-" * 50)
    print("[+] Scan Completed Successfully!")

if __name__ == "__main__":
    start_scanner()