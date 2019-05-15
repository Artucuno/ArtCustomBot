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
numtest = 1
class mod():
    def __init__(self, bot):
        self.bot = bot

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
