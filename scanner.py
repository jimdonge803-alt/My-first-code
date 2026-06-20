import socket
import sys
import time
import pyfiglet

# Stylish Banner
banner = pyfiglet.figlet_format("PARV SCANNER", font="slant")
print("\033[92m" + banner + "\033[0m")
print("-" * 50)
print("Scanning target started at: " + str(time.strftime("%Y-%m-%d %H:%M:%S")))
print("-" * 50)

# Target IP (Hum local host test karenge)
target = "127.0.0.1" 

# Kuch common ports jo hum check karenge
ports = [21, 22, 80, 443, 5000, 8080]

try:
    for port in ports:
        # Socket object banana network connectivity check karne ke liye
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second ka wait time
        
        # Port connect karke dekhna
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"\033[96m[+] Port {port}: OPEN\033[0m")
        else:
            print(f"[-] Port {port}: Closed")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script...")
    sys.exit()
