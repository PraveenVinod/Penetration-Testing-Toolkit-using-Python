# modules/brute_forcer.py

import time
import random
from modules import html_report


def run_brute_forcer():
    findings = []
    print("\n--- Brute Forcer (Demo Version) ---")
    target = input("Enter target service (e.g., SSH/FTP): ").strip()
    username = input("Enter username: ").strip()
    wordlist = input("Enter path to wordlist (or leave blank for demo list): ").strip()

    demo_wordlist = ["123456", "password", "admin", "letmein", "qwerty"]
    passwords = []

    if wordlist:
        try:
            with open(wordlist, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("[!] Wordlist file not found. Using demo wordlist instead.")
            passwords = demo_wordlist
    else:
        passwords = demo_wordlist

    findings.append(f"Target Service: {target}")
    findings.append(f"Username: {username}")
    findings.append(f"Wordlist used: {wordlist if wordlist else 'Demo Wordlist'}")

    success_password = random.choice(passwords)

    try:
        for password in passwords:
            attempt = f"Trying password: {password}"
            print(attempt)
            findings.append(attempt)
            time.sleep(0.3)
            if password == success_password:
                success = f"[SUCCESS] Password found: {password}"
                print(success)
                findings.append(success)
                break
        else:
            findings.append("[!] Brute force completed. No password found.")

        # Generate report
        html_report.generate_html_report("Brute Force Report", findings, "brute_force_report.html")

    except KeyboardInterrupt:
        print("\n[!] Brute force stopped by user.")
