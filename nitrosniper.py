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
 if message.content.startswith('https://discord.gift/'):
        code = re.search("https://discord.gift/(.*)", message.content).group(1)
        if len(code) != 16:
            print("\033[31mFake Code: \033[97m"+code+Fore.RESET)
        else:
            print(Fore.RED+f"Nitro Sniped: \033[97m"+code+Fore.RESET)
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
                ).text
            if 'This gift has been redeemed already.' in r:
                print("\033[31mCode Already \033[97mRedeemed")

 if message.content.startswith('discord.gift/'):
     code = re.search("discord.gift/(.*)", message.content).group(1)
     if len(code) != 16:
         print("\033[31mFake Code: \033[97m"+code+Fore.RESET)
     else:
         print(Fore.RED+"Nitro Sniped: \033[97m"+code+Fore.RESET)
         headers = {'Authorization': token}
         r = requests.post(
             f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
             headers=headers,
         ).text

if __name__ == '__main__':
    Init()