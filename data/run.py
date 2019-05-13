import subprocess
print("[DEBUG] Imported subprocess")
try:
    import discord
    from discord.ext import commands
    from discord.ext.commands import Bot
    print("[DEBUG] Imported discord.py")
except:
    subprocess.call(("python3", "-m", "pip", "install", "-U discord.py==0.16.0"))
import logging
print("[DEBUG] Imported logging")
import random
print("[DEBUG] Imported random")
import sys, os, time
print("[DEBUG] Imported sys, os, time")
from utils import checks
print("[DEBUG] Imported checks")
import json
print("[DEBUG] Imported json")
import timeit
print("[DEBUG] Imported timeit")
import tken
print("[DEBUG] Imported tken")
try:
    import psutil
    print("[DEBUG] Imported psutil")
except:
    subprocess.call(("pip3", "install", "psutil"))
import asyncio
print("[DEBUG] Imported asyncio")
print("\n"
      "\n")
if os.path.isfile('data/config.json'):
    with open('data/config.json') as json_file:  
        data = json.load(json_file)
        for p in data['Config']:
            global botdesc
            botdesc = "{}".format(p['Descript'])

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
if os.path.isfile('data/config.json'):
    with open('data/config.json') as json_file:  
        data = json.load(json_file)
        for p in data['Config']:
            global ownerid
            ownerid = p['oid']
            bot = Bot(command_prefix=p['prefix'], description=botdesc) # Sets the client and sets the prefix
else:
    input("[CONSOLE] MISSING CONFIG FILE!")
    exit(10)
extensions = ["mod"]

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await bot.send_message(ctx.message.channel, content='This command is on a %.2fs cooldown!' % error.retry_after)
    else:
        print(error)

@bot.event
async def on_ready():
    clear_screen()
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    if __name__ == "__main__":
        for extension in extensions:
            try:
                bot.load_extension(extension)
                print("[CONSOLE] Loaded {}".format(extension))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
    print("-=-=-=-=-=-=-=-\n"
          " {}\n"
          "-=-=-=-=-=-=-=-\n".format(bot.user.name))
    print("Servers  {}\n"
          "Channels {}\n"
          "Users    {}\n".format(servers, channels, users))
    print("\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1".format(bot.user.id))
    if os.path.isfile('data/game.json'):
        with open('data/game.json') as json_file:  
            data = json.load(json_file)
            for p in data['Game']:
                await bot.change_presence(game=discord.Game(name=p['Gme'], type=p['Type']))
    if os.path.isfile('data/mdbl.json'):
        with open('data/mdbl.json') as json_file:  
            data = json.load(json_file)
            for p in data['Mdbl']:
                if p['Active'] == "False":
                    print("[MDBL] Not active")
                else:
                    if os.path.isfile('data/apipy/mdbl.py'):
                        from apipy import mdbl
                        await mdbl.start(bot)
                        await mdbl.post(servers, users, channels, cmds)
                    else:
                        subprocess.call(("git", "clone", "https://github.com/MegaDiscordBotList/apipy.git", "data/apipy"))

if os.path.isfile('data/config.json'):
    with open('data/config.json') as json_file:  
        data = json.load(json_file)
        for p in data['Config']:
            print("Logging in as {}".format(tken.token))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(bot.run(tken.token))
