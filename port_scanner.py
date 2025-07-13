import socket
from datetime import datetime
from modules import html_report

# Top commonly used ports (you can modify this list)
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]


def scan_ports(target_host, start_port=None, end_port=None):
    findings = []

    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"\nScanning {target_ip}...")

        # Ask for port range if not provided
        if start_port is None or end_port is None:
            choice = input("Scan full range (1-1024) or common ports only? (f/c): ").strip().lower()
            if choice == 'f':
                start_port = 1
                end_port = 1024
            else:
                start_port = None
                end_port = None

        t1 = datetime.now()

        open_ports = []

        if start_port and end_port:
            print(f"\nScanning ports {start_port} to {end_port}...\n")
            for port in range(start_port, end_port + 1):
                if scan_port(target_ip, port):
                    open_ports.append(port)
        else:
            print(f"\nScanning common ports: {COMMON_PORTS}\n")
            for port in COMMON_PORTS:
                if scan_port(target_ip, port):
                    open_ports.append(port)

        for port in open_ports:
            findings.append(f"Port {port}: Open")

        if not open_ports:
            findings.append("No open ports found.")

        t2 = datetime.now()
        duration = t2 - t1
        findings.append(f"Scan completed in: {duration}")
        print(f"\nScan completed in: {duration}\n")

        # Generate HTML report
        html_report.generate_html_report("Port Scan Report", findings, "port_scan_report.html")

    except socket.gaierror:
        print("[!] Hostname could not be resolved.")
    except Exception as e:
        print(f"[!] Error: {e}")


def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.3)  # Fast response
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
                return True
    except:
        pass
    return False
