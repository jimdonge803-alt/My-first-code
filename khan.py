import pyfiglet
import time

# Terminal ke colors ke liye codes (ANSI Escape Codes)
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "[+] Initializing secure system..." + RESET)
time.sleep(1) # 1 second ka delay real feel ke liye

print(GREEN + "===============================================" + RESET)
# pyfiglet aapke naam ko 'slant' font me convert karega
stylish_name = pyfiglet.figlet_format("PARVEJ KHAN", font="slant")
print(GREEN + stylish_name + RESET)
print(GREEN + "===============================================" + RESET)

print(CYAN + "[+] Welcome back, Admin." + RESET)


