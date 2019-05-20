#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #

import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType

class server():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Show current server info"""
        server = ctx.message.server
        em = discord.Embed()
        em.set_author(name=ctx.message.server)
        em.add_field(name="Owner", value=(ctx.message.server.owner))
        em.add_field(name="ID", value=(ctx.message.server.id))
        em.add_field(name="Created At", value=(ctx.message.server.created_at))
        await self.bot.say(embed=em)

def setup(bot):
        bot.add_cog(server(bot))
