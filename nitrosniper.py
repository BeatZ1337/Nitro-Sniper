import os
import discord
from discord.ext import commands
from discord.ext import tasks
import colorama
from colorama import Fore, init
import ctypes
import re
import requests
colorama.init()



token = 'PUT TOKEN HERE'
prefix = '.'


BeatZ = commands.Bot(command_prefix=prefix, self_bot=True)
BeatZ.remove_command("help")

def Init():
    BeatZ.run(token, bot=False, reconnect=True)

def Clear():
    os.system('cls')
Clear()

@BeatZ.event
async def on_connect():
    guilds = len(BeatZ.guilds)
    Clear()
    os.system("mode con cols=49 lines=17")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Nitro Sniper || Logged In As: {BeatZ.user.name}')
    print('\033[31m╔══════════════════════════════════════════════╗')
    print('\033[31m║                                              ║')
    print('\033[31m║                 \033[31m╔╗╔╦╔╦╗╦═╗╔═╗\033[31m                ║')
    print('\033[31m║                 \033[91m║║║║ ║ ╠╦╝║ ║\033[31m                ║')
    print('\033[31m║                 \033[97m╝╚╝╩ ╩ ╩╚═╚═╝\033[31m                ║')
    print('\033[31m║                                              ║')
    print('\033[31m║               \033[31m╔═╗╔╗╔╦╔═╗╔═╗╦═╗\033[31m               ║')
    print('\033[31m║               \033[91m╚═╗║║║║╠═╝║╣ ╠╦╝\033[31m               ║')
    print('\033[31m║               \033[97m╚═╝╝╚╝╩╩  ╚═╝╩╚═\033[31m               ║')
    print('\033[31m║                \033[97mBy: \033[31mBeatZ#\033[97m0001\033[31m                ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m╚══════════════════════════════════════════════╝')


@BeatZ.event                
async def on_message(message):
          code = re.search(r'(discord.gift|discordapp.com/gifts)/\w{16,24}', message.content).group(0)
         print("\033[31mPOSSIBLE CODE: \033[97m"+code+Fore.RESET)
         token = config.get('token')
         headers = {'Authorization': token}
         r = requests.post(
             f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
             headers=headers,
             ).text
         if 'This gift has been redeemed already.' in r:
             print("\033[31mCode Already \033[97mRedeemed")
         elif 'nitro' in r:
             print(Fore.GREEN+"[+] found nitro : "+code+Fore.RESET)
         elif 'Unknow Gift Code' in r:
             print("[-] Invaild Code")
     except (AttributeError):
        pass
 else:
     pass

if __name__ == '__main__':
    Init()
