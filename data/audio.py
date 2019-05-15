#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #

import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
from discord.voice_client import VoiceClient
import logging
from utils import checks
import os
import json
import time
import subprocess
import youtube_dl

def get_voice_state(self, server):
    state = self.voice_states.get(server.id)
    if state is None:
        state = VoiceState(self.bot)
        self.voice_states[server.id] = state
    return state

class audio():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def summon(self, ctx):
        """Join a voice channel"""
        try:
            voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
        except:
            await self.bot.say("Unable to join voice channel!")

    @commands.command(pass_context=True)
    async def play(self, ctx, url=""):
        """Play something"""
        if url == "":
            await self.bot.say("```\n"
                               "play [url]\n"
                               "```")
        else:
            try:
                voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
            except:
                for x in self.bot.voice_clients:
                    if(x.server == ctx.message.server):
                        await x.disconnect()
                        voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
            player = await voice.create_ytdl_player(url)
            player.start()
            em = discord.Embed()
            em.add_field(name='Now playing...', value=(player.title))
            em.add_field(name='Uploader', value=(player.uploader))
            em.add_field(name='Description', value=(player.description))
            em.add_field(name='Duration', value=(player.duration))
            await self.bot.say(embed=em)

    @commands.command(pass_context = True)
    async def disconnect(self, ctx):
        """Disconnect from a voice channel"""
        for x in self.bot.voice_clients:
            if(x.server == ctx.message.server):
                return await x.disconnect()
    

def setup(bot):
        bot.add_cog(audio(bot))
