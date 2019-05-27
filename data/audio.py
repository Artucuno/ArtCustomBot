#  ============================================== ArtCustomBot ==============================================  #
# | Made by Artucuno                                  ||||                    https://github.com/Articuno1234| #
# | https://discord.gg/6V82bKP                        ||||                             First version: 13/5/19| #
#  ==========================================================================================================  #

import discord
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
from discord.voice_client import VoiceClient
from discord.utils import get
import logging
from utils import checks
import os
import json
import time
import subprocess
import youtube_dl
import settings

if settings.DJ == True:
    drole = settings.DJRole
else:
    drole = None

def get_voice_state(self, server):
    state = self.voice_states.get(server.id)
    if state is None:
        state = VoiceState(self.bot)
        self.voice_states[server.id] = state
    return state

def check_files():
    if os.path.isdir("data/acb/cogs/audio/failed"):
        pass
    else:
        print("[AUDIO] Created Audio Failed folder")
        os.mkdir("data/acb/cogs/audio/failed")

class audio():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def summon(self, ctx):
        """Join a voice channel"""
        try:
            voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
        except:
            await ctx.send("Unable to join voice channel!")

    @commands.command(pass_context=True)
    async def play(self, ctx, url=""):
        """Play something"""
        author = ctx.message.author
        server = ctx.message.guild
        role = discord.Role = drole
        if drole == None:
            pass
        else:
            if drole in [y.id for y in author.roles]:
                pass
            else:
                await ctx.send(":x: You do not have the required role (`{}`)\n".format(drole, role))
                return
        if url == "":
            await ctx.send("```\n"
                               "play [url]\n"
                               "```")
        else:
            try:
                voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
            except:
                for x in self.bot.voice_clients:
                    if(x.server == ctx.message.guild):
                        await x.disconnect()
                        voice = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
            player = await voice.create_ytdl_player(url)
            player.start()
            if settings.playing == True:
                try:
                    if os.path.isfile('data/acb/cogs/audio/failed/{}-{}.json'.format(player.title, player.uploader)):
                        print("[AUDIO] Passed Failed Song playing")
                        if os.path.isfile('data/acb/cogs/audio/failed/{}-{}.json'.format(player.title, player.uploader)):
                            with open('data/acb/cogs/audio/failed/{}-{}.json'.format(player.title, player.uploader)) as json_file:  
                                data = json.load(json_file)
                                for p in data['Config']:
                                    em = discord.Embed()
                                    em.set_author(name='Now Playing {}...'.format(player.title))
                                    em.set_footer(text='Failed song request found! | {} | {} | {} | found by {}'.format(p['url'], p['date'], p['title'], p['foundby']))
                                    await ctx.send(embed=em)
                    else:
                        em = discord.Embed()
                        em.add_field(name='Now playing...', value=(player.title))
                        em.add_field(name='Uploader', value=(player.uploader))
                        em.add_field(name='Description', value=(player.description))
                        em.add_field(name='Duration', value=(player.duration))
                        await ctx.send(embed=em)
                except Exception as e:
                    data = {}
                    data['Config'] = []
                    data['Config'].append({
                        'foundby': "{}".format(author),
                        'url': "{}".format(url),
                        'date': "{}".format(time.asctime()),
                        'title': "{}".format(player.title)
                        })
                    with open('data/acb/cogs/audio/failed/{}-{}.json'.format(player.title, player.uploader), 'w') as outfile:
                        json.dump(data, outfile)
                    exc = '{}: {}'.format(type(e).__name__, e)
                    print("[AUDIO] Unable to show Now Playing for {}\n{}".format(url, exc))
            else:
                pass

    @commands.command(pass_context = True)
    async def disconnect(self, ctx):
        """Disconnect from a voice channel"""
        for x in self.bot.voice_clients:
            if(x.server == ctx.message.guild):
                return await x.disconnect()
    

def setup(bot):
    check_files()
    bot.add_cog(audio(bot))
