import os
import time
import pyfiglet
from colorama import Fore, init
from twilio.rest import Client

# Initialize Colorama
init(autoreset=True)

# Aapke verified credentials
account_sid = 'AC76b2bde6569c5fefb1ad2bbca8cd628d'
auth_token = '71426b6771aef7b779bc123a8edba680'
client = Client(account_sid, auth_token)

def banner():
    os.system('clear')
    logo = pyfiglet.figlet_format("WHATS-PUSH", font="slant")
    print(Fore.CYAN + logo)
    print(Fore.YELLOW + "==========================================")
    print(Fore.GREEN + "  AUTHOR : NAHID-CODE | STATUS: ACTIVE")
    print(Fore.YELLOW + "==========================================\n")

def start():
    banner()
    # User input
    target = input(Fore.WHITE + "[?] Target Number (e.g. +92334...): ")
    msg = input(Fore.WHITE + "[?] Your Message: ")
    count = int(input(Fore.WHITE + "[?] How many times?: "))

    print(Fore.BLUE + "\n[*] Starting...")
    for i in range(count):
        try:
            # Twilio sandbox sending
            client.messages.create(
                from_='whatsapp:+14155238886',
                body=msg,
                to=f'whatsapp:{target}'
            )
            print(Fore.GREEN + f"[+] Message {i+1} Sent!")
            time.sleep(1.5)
        except Exception as e:
            print(Fore.RED + f"[!] Error: {e}")
            break

if __name__ == "__main__":
    start()
