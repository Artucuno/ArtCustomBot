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
        await self.bot.say("```\n"
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

    # token = 'NTc2OTMwMTIzNjUyMDA1OTA5.XNpwvQ.nWO2bOG4Ho9du8tDzXUZk33FaOk'
    @commands.command(pass_context=True, no_pm=True)
    async def owner(self, ctx):
        """Set bot owner

        set owner [id]"""
        char = ["a", "A", "Q", "G", "h", "L", "%", "@", "=", "+", "/", "-", "y", "o", "O", "$", "E"]
        author = ctx.message.author
        await self.bot.say("I have sent a code to the bot console please type it in chat!")
        data = {}
        data['Owner'] = []
        data['Owner'].append({
            'code': "{}{}{}{}{}{}{}".format(random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char), random.choice(char))
            })
        with open('data/code.json', 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(2)
        if os.path.isfile('data/code.json'):
            with open('data/code.json') as json_file:  
                data = json.load(json_file)
                for p in data['Owner']:
                    print("[CONSOLE] Owner Code: {}".format(p['code']))
                    msg = await self.bot.wait_for_message(content=p['code'])
                    if os.path.isfile('data/utils/settings.json'):
                        with open('data/utils/settings.json') as json_file:  
                            data = json.load(json_file)
                            for p in data['Config']:
                                data = {}
                                data['Config'] = []
                                data['Config'].append({
                                    'ownerid': "{}".format(msg.author.id),
                                    'errorchannel': p['errorchannel']
                                    })
                                with open('data/utils/settings.json', 'w') as outfile:
                                    json.dump(data, outfile)
                                os.remove("data/code.json")
                                await self.bot.say("<@{}> is now the bot owner!".format(msg.author.id))
                                print("[CONSOLE] {} is the new bot owner | Restarting...")
                                await self.bot.change_presence(status=discord.Status.dnd)
                                self.bot.logout()
                                subprocess.call(("python3", "data/run.py"))
        else:
            await self.bot.say(":x: Could not find the code file!")
            return
    @checks.is_owner()
    @commands.command(pass_context=True, no_pm=True)
    async def errchannel(self, ctx, chann: discord.Channel = None):
        """Set error logging channel

        set errorchannel [id]"""
        author = ctx.message.author
        channel = self.bot.get_channel(chann.id)
        await self.bot.say("Are you sure you want to set <#{}> as your error log channel? type yes or no".format(channel.id))
        msg = await self.bot.wait_for_message(author=author, content='yes')
        if os.path.isfile('data/utils/settings.json'):
            with open('data/utils/settings.json') as json_file:  
                data = json.load(json_file)
                for p in data['Config']:
                    data = {}
                    data['Config'] = []
                    data['Config'].append({
                        'ownerid': p['ownerid'],
                        'errorchannel': "{}".format(channel.id)
                        })
                    with open('data/utils/settings.json', 'w') as outfile:
                        json.dump(data, outfile)
                    await self.bot.say("Set Error logging channel!")


    @checks.is_owner()
    @commands.command(pass_context=True)
    async def reload(self, ctx, *, cog):
        """Reload a cog/module"""
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await self.bot.say(":joy: :ok_hand: ")
            print("[CONSOLE] The cog '{}' was reloaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await self.bot.say(exc)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def load(self, ctx, *, cog):
        """Load a cog/module"""
        author = ctx.message.author
        try:
            self.bot.load_extension(cog)
            await self.bot.say(":ok_hand: ")
            print("[CONSOLE] The cog '{}' was loaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await self.bot.say(exc)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def unload(self, ctx, *, cog):
        """Unload a cog/module"""
        author = ctx.message.author
        try:
            self.bot.load_extension(cog)
            await self.bot.say(":ok_hand: ")
            print("[CONSOLE] The cog '{}' was loaded".format(cog))
        except Exception as e:
            exc = ':x: {}: {}'.format(type(e).__name__, e)
            await self.bot.say(exc)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def shutdown(self, ctx):
        """Shutdown"""
        voicec = 0
        await self.bot.say(":wave:")
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
    @commands.command(pass_context=True)
    async def restart(self, ctx):
        """Restart"""
        voicec = 0
        await self.bot.say("Restarting...")
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
