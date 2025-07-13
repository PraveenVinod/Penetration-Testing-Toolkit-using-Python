# modules/banner_grabber.py

import socket
from modules import html_report


def grab_banner():
    findings = []
    print("\n--- Banner Grabber ---")
    target = input("Enter target host (IP or domain): ").strip()

    try:
        port = int(input("Enter port: ").strip())
    except ValueError:
        print("[!] Invalid port number.")
        return

    findings.append(f"Target: {target}")
    findings.append(f"Port: {port}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((target, port))
            banner = s.recv(1024)
            try:
                banner_text = banner.decode().strip()
                print(f"\n[+] Banner: {banner_text}")
                findings.append(f"Banner: {banner_text}")
            except UnicodeDecodeError:
                print(f"\n[+] Banner (raw bytes): {banner}")
                findings.append(f"Banner (raw bytes): {banner}")

        html_report.generate_html_report("Banner Grabbing Report", findings, "banner_grab_report.html")

    except socket.timeout:
        print("[!] Connection timed out.")
        findings.append("Connection timed out.")
    except ConnectionRefusedError:
        print("[!] Connection refused.")
        findings.append("Connection refused.")
    except socket.gaierror:
        print("[!] Hostname could not be resolved.")
        findings.append("Hostname could not be resolved.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        findings.append(f"Unexpected error: {e}")
