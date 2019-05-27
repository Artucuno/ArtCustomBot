gitrepo = "https://github.com/Articuno1234/ArtCustomBot"
#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #
# sett = settings
import time
print("ArtCustomBot Made by Artucuno\n"
      "=======Links======\n"
      "https://github.com/Articuno1234/ArtCustomBot\n"
      "https://artcustombot.surge.sh/")
print("\n"
      "[CONSOLE] Getting Ready...")
time.sleep(3)
import subprocess    
print("[DEBUG] Imported subprocess")
try:
    import discord
    if discord.__version__ == "0.16.0" or "0.16.12":
        print("[DISCORD] Correct Discord Version!")
        time.sleep(2)
        from discord.ext import commands
        from discord.ext.commands import Bot
        print("[DEBUG] Imported discord.py")
    else:
        input("[DISCORD] Incorrect discord version! Needed: 0.16.0 or 0.16.12")
        exit(2)
except:
    code = subprocess.call(("python3", "-m", "pip", "install", "-U discord.py[voice]==0.16.0"))
    if code == 0:
        print("[PIP] Installed discord.py[voice] v0.16.0")
        try:
            import discord
            from discord.ext import commands
            from discord.ext.commands import Bot
        except:
            input("[CONSOLE] Unable to start (Discord failed to import!)")
            exit(2)
    else:
        input("[PIP] Unable to install discord.py[voice] v0.16.0")
        exit()
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
import datetime
print("[DEBUG] Imported datetime")
uptime = datetime.datetime.utcnow()  # Refreshed before login
if os.path.isfile('data/config.json'):
    with open('data/config.json') as json_file:  
        data = json.load(json_file)
        for p in data['Config']:
            global botdesc
            global botpref
            botpref = "{}".format(p['prefix'])
            botdesc = "{}".format(p['Descript'])
import aiohttp
import settings as sett
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

# Remove help command
if sett.helpcmd == True:
    bot.remove_command("help")
    helpc = True
else:
    helpc = False

async def send_cmd_help(ctx):
    try:
        if ctx.invoked_subcommand:
            pages = formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                await bot.send_message(ctx.message.channel, page)
        else:
            pages = formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await bot.send_message(ctx.message.channel, page)
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print(exc)

class Formatter(commands.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _add_subcommands_to_page(self, max_width, commands):
        for name, command in sorted(commands, key=lambda t: t[0]):
            if name in command.aliases:
                # skip aliases
                continue

            entry = '  {0:<{width}} {1}'.format(name, command.short_doc,
                                                width=max_width)
            shortened = self.shorten(entry)
            self._paginator.add_line(shortened)

@bot.event
async def on_command(ctx):
    if sett.commandoutput == True:
        print("[COMMAND] {} ({}{}) {}".format(ctx.message.guild, botpref, ctx.command, ctx.message.author))
    if ctx.command in sett.commands:
        if command == "stats":
            print("[COMMAND] Unable to disable this command!")
        elif command == "help":
            print("[COMMAND] Unable to disable this command!")
        else:
            await self.ctx.send(":x: Command disabled by Owner!")
            return

@bot.event
async def on_message(message):
    # Ignore bots
    if message.author.bot:
        return
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    if os.path.isfile('data/acb/cogs/autorole/{}/config.json'.format(member.server.id)):
        with open('data/acb/cogs/autorole/{}/config.json'.format(member.server.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Config']:
                role = discord.utils.get(member.server.roles, name=p['role'])
                await bot.add_roles(member, role)
    if os.path.isfile('data/acb/cogs/welcome/{}/config.json'.format(member.server.id)):
        with open('data/acb/cogs/welcome/{}/config.json'.format(member.server.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Config']:
                try:
                    channel = bot.get_channel(p['channel'])
                    em = discord.Embed(color=0x000000, description=p['msg'])
                    em.set_author(name=member, icon_url=member.avatar_url)
                    await bot.send_message(channel, embed=em)
                    mg = await bot.send_message(channel, "<@{}>".format(member.id))
                    await bot.delete_message(mg)
                except Exception as e:
                    pass
@bot.event
async def on_resumed():
    print("[CONSOLE] Reconnected Bot")

#@bot.event
#async def on_command_error(error, ctx):
#    if isinstance(error, commands.CommandOnCooldown):
#       await bot.send_message(ctx.message.channel, content='This command is on a %.2fs cooldown!' % error.retry_after)
#    elif isinstance(error, commands.CommandNotFound):
#        pass
#    elif isinstance(error, commands.BadArgument):
#        try:
#            await send_cmd_help(ctx)
#        except Exception as e:
#            exc = '{}: {}'.format(type(e).__name__, e)
#            print("[CONSOLE] Unable to send error message to log channel!\n{}".format(exc))
#    else:
#       print("\n[CONSOLE ERROR]\n{}".format(error))
#       if os.path.isfile('data/utils/settings.json'):
#            with open('data/utils/settings.json') as json_file:  
#                data = json.load(json_file)
#                for p in data['Config']:
#                    try:
#                        channel = bot.get_channel(p['errorchannel'])
#                        await channel.send("```ini\n [{}] {} {} \n[ ------------------------------------------------------- ]\n{}\n[ ------------------------------------------------------- ]\n[ {} ]```".format(ctx.message.guild, ctx.author, commands, error, time.asctime()))
#                    except Exception as e:
#                        exc = '{}: {}'.format(type(e).__name__, e)
#                        print("[CONSOLE] Unable to send error message to log channel!\n{}".format(exc))

@bot.event
async def on_ready():
    if 'bot' in sett.extensions:
        pass
    else:
        input("[ERROR] A vital module 'bot' was not found in extensions list!")
        exit()
    data = {}
    data['Cog'] = []
    data['Cog'].append({
        'cogs': "{}".format(sett.extensions),
        'count': "{}".format(len(sett.extensions))
        })
    with open('data/cogs.json', 'w') as outfile:
        json.dump(data, outfile)
    print("[COG] Set cog files")
    time.sleep(1)
    clear_screen()
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.guilds)
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
        for extension in sett.extensions:
            try:
                bot.load_extension(extension)
                if extension == "audio":
                    print("[COG] Loaded audio (NOTE: It will send feedback messages!)")
                else:
                    print("[COG] Loaded {}".format(extension))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                if extension == "bot":
                    input("[CONSOLE] Unable to load required extension '{}'\n{}".format(extension, exc))
                    print("[CONSOLE] Logging out...")
                    await bot.logout()
                    exit()
                else:
                    print('[COG] Failed to load extension {}\n{}'.format(extension, exc))
    try:
        await bot.change_presence(game=discord.Game(name=sett.game, type=sett.gtype))
        if sett.game == "":
            print("[GAME] No game was set!")
        else:
            print("[GAME] Set game to '{}'".format(sett.game))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[GAME] Unable to set game\n{}".format(exc))
    if sett.mdbl == True:
        if os.path.isfile('data/apipy/mdbl.py'):
            from apipy import mdbl
            await mdbl.start(bot)
            await mdbl.post(servers, users, channels, cmds)
        else:
            code = subprocess.call(("git", "clone", "https://github.com/MegaDiscordBotList/apipy.git", "data/apipy"))
            if code == 0:
                print("[MDBL] Downloaded MDBL module!")
            else:
                print("[MDBL] Unable to install MDBL Module!")
    print("----- Bot -----")
    if helpc == True:
        print("[CONSOLE] Removed {}help command".format(botpref))

@bot.command(pass_context=True)
async def stats(ctx):
    """Show bot statistics"""
    import datetime
    today = datetime.date.today()
    since = datetime.date(2019, 5, 12)
    users = len(set(bot.get_all_members()))
    servers = len(bot.guilds)
    channels = len([c for c in bot.get_all_channels()])
    mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    em = discord.Embed(description="Made with [ArtCustomBot](https://github.com/Articuno1234/ArtCustomBot)")
    em.set_author(name='Bot Statistics')
    em.add_field(name='Guilds', value=(servers))
    em.add_field(name='Users', value=(users))
    em.add_field(name='Channels', value=(channels))
    em.add_field(name='Commands', value=(len(bot.commands)))
    em.add_field(name='Uptime', value=(uptime))
    em.set_footer(text='Running since {} days | Say "next", "system", "acb", "exit"'.format(today - since))

    if os.path.isfile('data/utils/settings.json'):
        with open('data/utils/settings.json') as json_file:  
            data = json.load(json_file)
            for p in data['Config']:
                eem = discord.Embed(description="Made with [ArtCustomBot](https://github.com/Articuno1234/ArtCustomBot)")
                eem.set_author(name='Bot Statistics')
                eem.add_field(name='Owned by', value=("<@{}> ({})".format(p['ownerid'], p['owner'])))
                eem.add_field(name='Github', value=(gitrepo))
                eem.set_footer(text='Running since {} days'.format(today - since))

    eeem = discord.Embed(description="Made with [ArtCustomBot](https://github.com/Articuno1234/ArtCustomBot)")
    eeem.set_author(name='System Statistics')
    eeem.add_field(name='Memory usage', value=mem_usage)
    eeem.set_footer(text='Running since {} days'.format(today - since))

    acbe = discord.Embed(description="Made with [ArtCustomBot](https://github.com/Articuno1234/ArtCustomBot)")
    acbe.set_author(name='ArtCustomBot')
    acbe.add_field(name='Version', value=("[V2](https://artcustombot.surge.sh)"))
    acbe.add_field(name='Discord.py', value=(discord.__version__))
    acbe.set_footer(text='Running since {} days'.format(today - since))

    emmm = discord.Embed(description="Timed Out/Exited!")
    msg = await ctx.send(embed=em)
    try:
        mss = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10.0)
    except asyncio.TimeoutError:
        await msg.edit(embed=emmm)
    if mss.content == "next":
        await msg.edit(embed=eem)
    elif mss.content == "system":
        await msg.edit(embed=eeem)
    elif mss.content == "acb":
        await msg.edit(embed=acbe)
    elif mss.content == "exit":
        await msg.edit(embed=emmm)
    else:
        await msg.edit(embed=emmm)

if os.path.isfile('data/config.json'):
    with open('data/config.json') as json_file:  
        data = json.load(json_file)
        for p in data['Config']:
            clear_screen()
            print("Logging into Discord...")
            formatter_class = Formatter
            formatter = formatter_class(show_check_failure=False)
            time.sleep(2)
            clear_screen()
            try:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(bot.run(tken.token))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print("Unable to login to Discord!\n{}".format(exc))
                exit(1)
