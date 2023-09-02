import requests
from colorama import Fore, init
from datetime import datetime
import cloudscraper
import getpass
import time

scraper = cloudscraper.create_scraper()
init(autoreset=True)
time = datetime.now().strftime('%H:%M:%S')
print(Fore.YELLOW+'''
    ░█████╗░███████╗██╗░░██╗  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
    ██╔══██╗██╔════╝╚██╗██╔╝  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
    ██║░░╚═╝█████╗░░░╚███╔╝░  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
    ██║░░██╗██╔══╝░░░██╔██╗░  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
    ╚█████╔╝██║░░░░░██╔╝╚██╗  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
    ░╚════╝░╚═╝░░░░░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝

      '''+Fore.RED+'''Made By .exploited. on discord\n'''+Fore.RESET
)

def get_server_info(code):
    while True:
        try:
            getiNFO = scraper.get("https://servers-frontend.fivem.net/api/servers/single/"+code)
            getiNFO.raise_for_status()
            response_data = getiNFO.json()
            
            if "Data" in response_data and "vars" in response_data["Data"] and "sv_projectName" in response_data["Data"]["vars"]:
                serverName = response_data["Data"]["vars"]["sv_projectName"]
                serverIp = response_data["Data"]["connectEndPoints"]
                serverPlayers = response_data["Data"]["clients"]
                serverMaxPlayers = response_data["Data"]["sv_maxclients"]

                print("     [ "+Fore.YELLOW+time+Fore.RESET+" ] Server Name : "+Fore.GREEN+f"{serverName}")
                serverIps_str = ', '.join(serverIp)

                print("     [ "+Fore.YELLOW+time+Fore.RESET+" ] Server IP : "+Fore.GREEN+f"{serverIps_str}")
                print("     [ "+Fore.YELLOW+time+Fore.RESET+" ] Online Players : "+Fore.GREEN+f"{serverPlayers}/{serverMaxPlayers}")
                
                with open('data.txt', 'w', encoding='utf-8') as file:
                    for player in response_data['Data']['players']:
                        file.write(f"Player Name: {player['name']}\nIP: {player['endpoint']}\n")
                        if 'identifiers' in player:
                            for identifier in player['identifiers']:
                                if identifier.startswith('discord:'):
                                    discord_id = identifier.replace('discord:', '')
                                    file.write(f"Discord ID: {discord_id}\n\n")
                        else:
                            file.write(f"\n\n")

                print("     [ "+Fore.YELLOW+time+Fore.RESET+" ] Successfully "+Fore.GREEN+f"saved"+Fore.RESET+" players data in data.txt")
                break  # Exit the loop if successful
            else:
                print("     [ "+Fore.RED+time+Fore.RESET+" ] Error please make sure you entered a valid IP or try again later.")
        except requests.exceptions.RequestException as e:
            print("     [ "+Fore.RED+time+Fore.RESET+" ] An error occurred:", str(e))
            print("     [ "+Fore.YELLOW+time+Fore.RESET+" ] Please keep trying.")
            break
            time.sleep(60)

code = input("     [ "+Fore.YELLOW+time+Fore.RESET+" ] Enter Cfx Join Link : ")
if "cfx.re/join/" in code:
    code = code.replace("cfx.re/join/", "")

get_server_info(code)

mano = getpass.getpass("\n     [ "+Fore.YELLOW+time+Fore.RESET+" ] Press enter to exit.")
