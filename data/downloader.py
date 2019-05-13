import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
from utils import checks

class mod():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def cog(self, ctx):
        """Dashboard"""
        
        
def setup(bot):
        bot.add_cog(mod(bot))
