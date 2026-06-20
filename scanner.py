import socket
import sys
import time
import pyfiglet

# Stylish Banner
banner = pyfiglet.figlet_format("PARV SCANNER V2", font="slant")
print("\033[92m" + banner + "\033[0m")

# USER INPUT: Ab aap website ya IP khud daal sakte hain
target_input = input("Enter Target Website or IP (e.g., google.com): ")

try:
    # Agar domain name dala hai toh ye use IP me badal dega
    target = socket.gethostbyname(target_input)
except socket.gaierror:
    print("\033[91m[-] Invalid Website/IP. Exiting...\033[0m")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target_input} ({target})")
print("Started at: " + str(time.strftime("%Y-%m-%d %H:%M:%S")))
print("-" * 50)

# Common ports to scan
ports = [21, 22, 80, 443, 8080]

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"\033[96m[+] Port {port}: OPEN\033[0m")
        else:
            print(f"[-] Port {port}: Closed")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script...")
    sys.exit()

