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

#Using to test functions
numtest = 1

class mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def autorole(self, ctx):
        """Setup autorole"""
        # Very Confusing...
        author = ctx.message.author
        server = ctx.message.server
        if ctx.message.author.server_permissions.manage_server:
            await self.bot.say("Would you like to remove autorole? (yes = Remove, no = Setup, exit = Exit)")
            msg = await self.bot.wait_for_message(author=author)
            if msg.content == "yes":
                if os.path.isfile('data/acb/cogs/autorole/{}/config.json'.format(server.id)):
                    os.remove("data/acb/cogs/autorole/{}/config.json".format(server.id))
                    await self.bot.say("Removed Autorole")
                else:
                    await self.bot.say("Unable to remove because it is not active!")
            if msg.content == "exit":
                return
            elif msg.content == "no":
                if os.path.isfile('data/acb/cogs/autorole/{}/config.json'.format(server.id)):
                    await self.bot.say("Autorole already exists would you like to edit it? (yes/no/exit)")
                    msgg = await self.bot.wait_for_message(author=author)
                    if msgg.content == "yes":
                        await self.bot.say("Enter a role (name/id/mention)")
                        msgrole = await self.bot.wait_for_message(author=author)
                        rle = discord.Role = "{}".format(msgrole.content)
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'role': "{}".format(rle)
                            })
                        with open('data/acb/cogs/autorole/{}/config.json'.format(server.id), 'w') as outfile:
                            json.dump(data, outfile)
                    elif msgg.content == "no":
                        await self.bot.say("Exited")
                    else:
                        return
                else:
                    if os.path.isdir('data/acb/cogs/autorole/{}'.format(server.id)):
                        await self.bot.say("Enter a role! (name/id/mention)")
                        msgggg = await self.bot.wait_for_message(author=author)
                        rle = discord.Role = "{}".format(msgggg.content)
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'role': "{}".format(rle)
                            })
                        with open('data/acb/cogs/autorole/{}/config.json'.format(server.id), 'w') as outfile:
                            json.dump(data, outfile)
                        await self.bot.say("Set autorole!")
                    else:
                        try:
                            try:
                                os.mkdir("data/acb/cogs/autorole/{}".format(server.id))
                            except:
                                pass
                            await self.bot.say("Enter a role! (name/id/mention)")
                            msgggg = await self.bot.wait_for_message(author=author)
                            rle = discord.Role = "{}".format(msgggg.content)
                            data = {}
                            data['Config'] = []
                            data['Config'].append({
                                'role': "{}".format(rle)
                                })
                            with open('data/acb/cogs/autorole/{}/config.json'.format(server.id), 'w') as outfile:
                                json.dump(data, outfile)
                            await self.bot.say("Set autorole!")
                        except Exception as e:
                            exc = '{}: {}'.format(type(e).__name__, e)
                            await self.bot.say("Unable to create file\n`{}`".format(exc))
                            return

    @commands.command(pass_context=True)
    async def welcomemsg(self, ctx):
        """Setup welcome messages"""
        # Very Confusing... again
        author = ctx.message.author
        server = ctx.message.server
        if ctx.message.author.server_permissions.manage_server:
            await self.bot.say("Would you like to remove welcome messages? (yes = Remove, no = Setup, exit = Exit)")
            msg = await self.bot.wait_for_message(author=author)
            if msg.content == "yes":
                if os.path.isfile('data/acb/cogs/welcome/{}/config.json'.format(server.id)):
                    os.remove("data/acb/cogs/welcome/{}/config.json".format(server.id))
                    await self.bot.say("Removed Welcome messages!")
                else:
                    await self.bot.say("Unable to remove because it is not active!")
            if msg.content == "exit":
                return
            elif msg.content == "no":
                if os.path.isfile('data/acb/cogs/welcome/{}/config.json'.format(server.id)):
                    await self.bot.say("Autorole already exists would you like to edit it? (yes/no/exit)")
                    msgg = await self.bot.wait_for_message(author=author)
                    if msgg.content == "yes":
                        await self.bot.say("Enter a channel (id/hashtag)")
                        msgrole = await self.bot.wait_for_message(author=author)
                        await self.bot.say("Enter a welcome message!")
                        welmsgt = await self.bot.wait_for_message(author=author)
                        rle = discord.Channel = "{}".format(msgrole.content)
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'channel': "{}".format(rle),
                            'msg': "{}".format(welmsgt)
                            })
                        with open('data/acb/cogs/welcome/{}/config.json'.format(server.id), 'w') as outfile:
                            json.dump(data, outfile)
                    elif msgg.content == "no":
                        await self.bot.say("Exited")
                    else:
                        return
                else:
                    if os.path.isdir('data/acb/cogs/welcome/{}'.format(server.id)):
                        await self.bot.say("Enter a channel! (id/hashtag)")
                        msgggg = await self.bot.wait_for_message(author=author)
                        await self.bot.say("Enter a welcome message!")
                        welmsgo = await self.bot.wait_for_message(author=author)
                        rle = discord.Channel = "{}".format(msgggg.content)
                        data = {}
                        data['Config'] = []
                        data['Config'].append({
                            'channel': "{}".format(rle),
                            'msg': "{}".format(welmsgo)
                            })
                        with open('data/acb/cogs/welcome/{}/config.json'.format(server.id), 'w') as outfile:
                            json.dump(data, outfile)
                        await self.bot.say("Set Welcome Messages!")
                    else:
                        try:
                            try:
                                os.mkdir("data/acb/cogs/welcome/{}".format(server.id))
                            except:
                                pass
                            await self.bot.say("Enter a channel! (id/hashtag)")
                            msgggg = await self.bot.wait_for_message(author=author)
                            await self.bot.say("Enter a welcome message!")
                            welmsgth = await self.bot.wait_for_message(author=author)
                            rle = discord.Role = "{}".format(msgggg.content)
                            data = {}
                            data['Config'] = []
                            data['Config'].append({
                                'channel': "{}".format(rle),
                                'msg': "{}".format(welmsgth)
                                })
                            with open('data/acb/cogs/welcome/{}/config.json'.format(server.id), 'w') as outfile:
                                json.dump(data, outfile)
                            await self.bot.say("Set Welcome Messages!")
                        except Exception as e:
                            exc = '{}: {}'.format(type(e).__name__, e)
                            await self.bot.say("Unable to create file\n`{}`".format(exc))
                            return
                    

    @commands.command(pass_context=True)
    async def purge(self, ctx, number: int):
        """Delete Messages"""
        if ctx.message.author.server_permissions.manage_messages:
            pass
        else:
            await self.bot.say("You do not have perms!")
            return
        author = ctx.message.author
        channel = ctx.message.channel
        try:
            msges = 0
            if number > 0 and number < 10000:
                async for x in self.bot.logs_from(channel, limit=number + 1):
                    await self.bot.delete_message(x)
                    msges += 1
                await self.bot.say("Purged {} messages!".format(msges))
        except discord.errors.Forbidden:
            await self.bot.say("I need permissions to manage messages in this channel.")

    @commands.command(pass_context=True)
    async def ban(self, ctx, user: discord.User = None):
        """Ban somebody from your server"""
        if ctx.message.author.server_permissions.ban_members:
            if user == None:
                await self.bot.say("```\n"
                                   "ban <user>\n"
                                   "\n"
                                   "Ban somebody from your server\n```")
            try:
                await self.bot.ban(user)
                await self.bot.say("Banned {}!".format(user))
            except:
                await self.bot.say("Unable to ban {}".format(user))

    @commands.command(pass_context=True)
    async def unban(self, ctx, user: discord.User = None):
        """Unban somebody from your server"""
        if ctx.message.author.server_permissions.ban_members:
            if user == None:
                await self.bot.say("```\n"
                                   "unban <userid>\n"
                                   "\n"
                                   "unban somebody from your server\n```")
            try:
                await self.bot.ban(user)
                await self.bot.say("Unbanned {}!".format(user))
            except:
                await self.bot.say("Unable to unban {}".format(user))

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.User = None):
        """Kick somebody from your server"""
        if ctx.message.author.server_permissions.ban_members:
            if user == None:
                await self.bot.say("```\n"
                                   "kick <user>\n"
                                   "\n"
                                   "Kick somebody from your server\n```")
            try:
                await self.bot.kick(user)
                await self.bot.say("Kicked {}!".format(user))
            except:
                await self.bot.say("Unable to kick {}".format(user))        

def setup(bot):
        bot.add_cog(mod(bot))
