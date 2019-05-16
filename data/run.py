#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #

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
import botextensions as botext
print("[DEBUG] Imported botextensions as botext")
import datetime
print("[DEBUG] Imported datetime")
uptime = datetime.datetime.utcnow()  # Refreshed before login
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

@bot.event
async def on_member_join(member):
    if os.path.isfile('data/acb/cogs/autorole/{}/config.json'.format(member.server.id)):
        with open('data/acb/cogs/autorole/{}/config.json'.format(member.server.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Config']:
                role = discord.utils.get(member.server.roles, name=p['role'])
                await bot.add_roles(member, role)
                pass
    if os.path.isfile('data/cogs/welcome/{}/config.json'.format(member.server.id)):
        with open('data/cogs/welcome/{}/config.json'.format(member.server.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Welcome']:
                try:
                    channel = bot.get_channel(p['channel'])
                    em = discord.Embed(color=0x000000, description=p['msg'])
                    em.set_author(name=member, icon_url=member.avatar_url)
                    await bot.send_message(channel, embed=em)
                    mg = await bot.send_message(channel, "<@{}>".format(member.id))
                    await bot.delete_message(mg)
                except:
                    pass
@bot.event
async def on_resumed():
    print("[CONSOLE] Resumed bot")

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await bot.send_message(ctx.message.channel, content='This command is on a %.2fs cooldown!' % error.retry_after)
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        print("\n[{}] \n{}".format(ctx.message.server, error))
        if os.path.isfile('data/utils/settings.json'):
            with open('data/utils/settings.json') as json_file:  
                data = json.load(json_file)
                for p in data['Config']:
                    try:
                        channel = bot.get_channel(p['errorchannel'])
                        await bot.send_message(channel, "`[{}]` `{}` `{}` ```py\n{}\n```".format(ctx.message.server, ctx.message.author, commands, error))
                    except Exception as e:
                        exc = '{}: {}'.format(type(e).__name__, e)
                        print("[CONSOLE] Unable to send error message to log channel!\n{}".format(exc))

@bot.event
async def on_ready():
    data = {}
    data['Cog'] = []
    data['Cog'].append({
        'cogs': "{}".format(botext.extensions),
        'count': "{}".format(len(botext.extensions))
        })
    with open('data/cogs.json', 'w') as outfile:
        json.dump(data, outfile)
    print("[COG] Set cog files")
    time.sleep(1)
    clear_screen()
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    print("ArtCustomBot made by Artucuno")
    print("-=-=-=-=-=-=-=-\n"
          " {}\n"
          "-=-=-=-=-=-=-=-\n".format(bot.user.name))
    print("Servers  {}\n"
          "Channels {}\n"
          "Users    {}\n".format(servers, channels, users))
    print("\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1".format(bot.user.id))
    print("\n"
          "----- COGS -----")
    if __name__ == "__main__":
        for extension in botext.extensions:
            try:
                bot.load_extension(extension)
                if extension == "audio":
                    print("[COG] Loaded audio (NOTE: It will send feedback messages!)")
                else:
                    print("[COG] Loaded {}".format(extension))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('[COG] Failed to load extension {}\n{}'.format(extension, exc))
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

@bot.command(pass_context=True)
async def stats(ctx):
    """Show bot statistics"""
    import datetime
    today = datetime.date.today()
    since = datetime.date(2019, 5, 13)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    em = discord.Embed(description="Made with [ArtCustomBot](https://github.com/Articuno1234/ArtCustomBot)")
    em.set_author(name='Bot Statistics')
    em.add_field(name='Memory usage', value=mem_usage)
    em.add_field(name='Guilds', value=(servers))
    em.add_field(name='Users', value=(users))
    em.add_field(name='Channels', value=(channels))
    em.add_field(name='Commands', value=(len(bot.commands)))
    em.add_field(name='Discord.py', value=(discord.__version__))
    em.add_field(name='Uptime', value=(uptime))
    em.set_footer(text='Running since {} days'.format(today - since))
    msg = await bot.say(embed=em)
    # just a bit extra lol
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)
    await bot.edit_message(msg, embed=em)
    asyncio.sleep(5)

if os.path.isfile('data/config.json'):
    with open('data/config.json') as json_file:  
        data = json.load(json_file)
        for p in data['Config']:
            clear_screen()
            print("Logging into Discord...")
            time.sleep(2)
            clear_screen()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(bot.run(tken.token))
