from modules import port_scanner, brute_forcer, banner_grabber


def main():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Forcer")
        print("3. Banner Grabber")
        print("4. Exit")

        choice = input("\nSelect module (1-4): ").strip()

        if choice == '1':
            host = input("Enter target host (IP or domain): ").strip()
            try:
                port_scanner.scan_ports(host)  # Renamed for clarity
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '2':
            try:
                brute_forcer.run_brute_forcer()
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '3':
            try:
                banner_grabber.grab_banner()
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '4':
            print("Exiting... Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
