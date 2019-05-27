#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #

import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import logging
from utils import checks
import os
import json
import time
import subprocess
import botextensions as botext
import asyncio
debugcommandreq = False
try:
    import inspect
    print("[IMPORT] Imported Inspect!")
except:
    print("[COG] Installing Requirements for debug command!")
    code = subprocess.call(("pip", "install", "inspect"))
    if code == 0:
        debugcommandreq = True
    else:
        codee = subprocess.call(("pip", "install", "inspect"))
        if code == 0:
            debugcommandreq = True
        else:
            print("[COG] Unable to install requirements so the command 'debug' will be disabled!")
            debugcommandreq = False

class main():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def set(self, ctx):
        """Set bot settings

        game [type] [game]
        owner [id]
        errchannel [id]"""
        await ctx.send("```\n"
                           "Set bot settings\n"
                           "set game [type] [game]\n"
                           "set owner [id]\n"
                           "set errchannel [id]\n```")

    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def game(self, ctx, typ=1, *, game=""):
        """Set bot status

        set game [type] [game]"""
        
        await self.bot.change_presence(game=discord.Game(name=game, type=typ))

    @commands.command(pass_context=True, no_pm=True)
    async def owner(self, ctx, user: discord.Member = None):
        """Set bot owner

        set owner [id]"""
        char = ["a", "A", "Q", "G", "h", "L", "%", "@", "=", "+", "/", "-", "y", "o", "O", "$", "E"]
        author = ctx.message.author
        channel = ctx.message.channel
        await ctx.send("I have sent a code to the bot console please type it in chat!")
        data = {}
        data['Owner'] = []
        data['Owner'].append({
            'code': "{}{}{}{}{}{}{}{}{}{}{}{}{}".format(random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char))
            })
        with open('data/code.json', 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(2)
        if os.path.isfile('data/code.json'):
            with open('data/code.json') as json_file:  
                data = json.load(json_file)
                for p in data['Owner']:
                    print("[CONSOLE] Owner Code: {}".format(p['code']))
                    time.sleep(1)
                    def check(m):
                        return m.content == '{}'.format(p['code']) and m.channel == channel
                    msg = await self.bot.wait_for("{}".format(p['code']), check=check)
                    if os.path.isfile('data/utils/settings.json'):
                        with open('data/utils/settings.json') as json_file:  
                            data = json.load(json_file)
                            for p in data['Config']:
                                data = {}
                                data['Config'] = []
                                data['Config'].append({
                                    'owner': "{}".format(msg.author),
                                    'ownerid': "{}".format(msg.author.id),
                                    'errorchannel': p['errorchannel']
                                    })
                                with open('data/utils/settings.json', 'w') as outfile:
                                    json.dump(data, outfile)
                                os.remove("data/code.json")
                                await ctx.send("<@{}> is now the bot owner!".format(msg.author.id))
                                print("[CONSOLE] {} is the new bot owner | Restarting...".format(msg.author))
                                await self.bot.change_presence(status=discord.Status.dnd)
                                self.bot.logout()
                                subprocess.call((sys.executable, "data/run.py"))
        else:
            await ctx.send(":x: Could not find the code file!")
            return

    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def errchannel(self, ctx, chann = None):
        """Set error logging channel

        set errorchannel [id]"""
        author = ctx.message.author
        channel = self.bot.get_channel(chann.id)
        await ctx.send("Are you sure you want to set <#{}> as your error log channel? type yes or no".format(channel.id))
        msg = await self.bot.wait_for(author=author, content='yes')
        if os.path.isfile('data/utils/settings.json'):
            with open('data/utils/settings.json') as json_file:  
                data = json.load(json_file)
                for p in data['Config']:
                    data = {}
                    data['Config'] = []
                    data['Config'].append({
                        'owner': p['owner'],
                        'ownerid': p['ownerid'],
                        'errorchannel': "{}".format(channel.id)
                        })
                    with open('data/utils/settings.json', 'w') as outfile:
                        json.dump(data, outfile)
                    
                    await ctx.send("Set Error logging channel!")


    @checks.is_owner()
    @commands.command(pass_context=True)
    async def reload(self, ctx, *, cog):
        """Reload a cog/module"""
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send(":joy: :ok_hand: ")
            print("[CONSOLE] The cog '{}' was reloaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await ctx.send(exc)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def load(self, ctx, *, cog):
        """Load a cog/module"""
        author = ctx.message.author
        try:
            self.bot.load_extension(cog)
            await ctx.send(":ok_hand: ")
            print("[CONSOLE] The cog '{}' was loaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await ctx.send(exc)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def unload(self, ctx, *, cog):
        """Unload a cog/module"""
        author = ctx.message.author
        try:
            self.bot.load_extension(cog)
            await ctx.send(":ok_hand: ")
            print("[CONSOLE] The cog '{}' was loaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await ctx.send(exc)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def shutdown(self, ctx):
        """Shutdown"""
        voicec = 0
        await ctx.send(":wave:")
        print("[CONSOLE] Logging out...")
        asyncio.sleep(5)
        try:
            for x in self.bot.voice_clients:
                voicec += 1
                await x.disconnect()
            time.sleep(2)
            print("[AUDIO] Disconnected {} voice clients!".format(voicec))
        except:
            pass
        asyncio.sleep(15)
        await self.bot.logout()
        exit(10)

    @checks.is_owner()
    @commands.command(pass_context=True, hidden=True)
    async def debug(self, ctx, *, code : str):
        """Debug a script"""
        if debugcommandreq == False:
            await ctx.send("This command is disabled due to lack of requirements!")
            return
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.guild,
            'channel': ctx.message.channel,
            'author': ctx.message.author,
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await ctx.send(python.format(type(e).__name__ + ': ' + str(e)))
            return

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def restart(self, ctx):
        """Restart"""
        voicec = 0
        await ctx.send("Restarting...")
        print("[CONSOLE] Restarting...")
        for x in self.bot.voice_clients:
            voicec += 1
            await x.disconnect()
        print("[AUDIO] Disconnected {} voice clients!".format(voicec))
        asyncio.sleep(15)
        await self.bot.logout()
        subprocess.call(("python3", "data/run.py"))

def setup(bot):
        bot.add_cog(main(bot))
