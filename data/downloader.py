import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
from utils import checks
import subprocess

class downloader():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def cog(self, ctx):
        """Dashboard"""
        await self.bot.say("```\n"
                           "Commands:\n"
                           "download [git repo] [cog]\n"
                           "```")

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def download(self, ctx, gitrepo="", cog=""):
        """Download a cog"""
        if gitrepo == "":
            await self.bot.say("```\n"
                               "download [git repo] [cog]\n"
                               "```")
        else:
            if cog == "":
                await self.bot.say("```\n"
                                   "download [git repo] [cog]\n"
                                   "```")
            else:
                await self.bot.say("Installing...")
                print("[DOWNLOADER] Installing...")
                code = subprocess.call(("git", "clone", "{}".format(gitrepo), "data/cog/{}".format(cog)))
                if code == 0:
                    await self.bot.say("Installed!")
                    try:
                        await self.bot.load_extension("data.cog.{}.{}.py".format(cog, cog))
                        await self.bot.say("Loaded `{}`".format(cog))
                    except:
                        await self.bot.say("Unable to load")
                else:
                    print("ooops")
        
        
        
def setup(bot):
        bot.add_cog(downloader(bot))
