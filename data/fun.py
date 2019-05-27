#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #

import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import aiohttp

class fun():
    def __init__(self, bot):
        import aiohttp
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command(pass_context=True)
    async def dice(self, ctx):
        """Roll the dice"""
        nums = ['1', '2', '3', '4', '5', '6']
        await ctx.send(random.choice(nums))

    @commands.command()
    async def cat(self, ctx):
        """Show random images of cats"""
        resp = await self.session.get("http://aws.random.cat/meow")
        image_url = await resp.json()
        resp.close()
        image_url = image_url["file"]
        msg = await ctx.send("Loading...")
        await msg.edit(content=image_url)
        
    @commands.command()
    async def dog(self, ctx):
        """Show random images of dogs"""
        resp = await self.session.get("https://random.dog/woof.json")
        image_url = await resp.json()
        resp.close()
        image_url = image_url["url"]
        msg = await ctx.send("Loading...")
        await msg.edit(content=image_url)

    @commands.command(pass_context=True)
    async def say(self, ctx, *, msg=""):
        """Make me say something"""
        await ctx.send(msg)

def setup(bot):
        bot.add_cog(fun(bot))
