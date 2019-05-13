import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType

class mod():
    def __init__(self, bot):
        self.bot = bot

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
