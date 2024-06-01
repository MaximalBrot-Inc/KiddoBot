import os

import asyncio
import discord
from requests import get, exceptions
from discord import app_commands
from discord.ext import commands

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
ydl_opts = {'format': 'bestaudio'}

source = None


async def stream_audio(ctx, audio_stream):
    global source
    #source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(audio_stream["url"], **FFMPEG_OPTIONS), volume=0.5)
    source = discord.FFmpegOpusAudio(audio_stream["url"], **FFMPEG_OPTIONS)
    discord.VoiceClient.play(source=source, after=None, self=ctx.voice_client)


    await ctx.interaction.followup.send(f'Spiele {audio_stream["title"]} ab')
    return source


async def stream_youtube(ctx, query):
    try:
        with YoutubeDL(ydl_opts) as ydl:
            video = ydl.extract_info(url=query, download=False)

        await stream_audio(ctx, video)
    except DownloadError:
        await ctx.send('Es gab ein Problem beim Herunterladen des Videos :(')


async def search_and_play(ctx, query):
    with YoutubeDL(ydl_opts) as ydl:
        try:
            get(query)
        except exceptions.MissingSchema:
            video = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        else:
            video = ydl.extract_info(query, download=False)

    await stream_audio(ctx, video)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=['p'], brief='Spielt Musik ab', description='Spielt Musik ab', )
    async def play(self, ctx, *, source=None):
        if source is None:
            await ctx.send('Du hast weder einen Titel noch Link angegeben :(')
            await discord.TextChannel.send(content='Ich benötige aber eins von beiden sonst kann ich nichts abspielen',
                                           self=ctx.channel)
            return

        await ctx.interaction.response.defer(ephemeral=True, thinking=True)

        if source.startswith('https://') or source.startswith('http://'):

            await stream_youtube(ctx, source)

        else:
            await search_and_play(ctx, source)

    @commands.hybrid_command(aliases=['s'], brief='Stoppt die Musik', description='Stoppt die Musik')
    async def stop(self, ctx):

        ctx.voice_client.stop()
        await discord.VoiceClient.disconnect(self=ctx.voice_client)

        await ctx.send('Musik gestoppt und Verbindung getrennt')

    @commands.hybrid_command(brief='Pausiert die Musik', description='Pausiert die Musik')
    async def pause(self, ctx):
        try:
            discord.VoiceClient.pause(self=ctx.voice_client)
        except AttributeError:
            await ctx.send('Ich bin nicht in einem Voice Channel!')

    @commands.hybrid_command(brief='Setzt die Musik fort', description='Setzt die Musik fort')
    async def resume(self, ctx):
        discord.VoiceClient.resume(self=ctx.voice_client)

    @commands.hybrid_command(alias=['vol'], brief='Ändert die Lautstärke', description='Ändert die Lautstärke')
    async def volume(self, ctx, volume: int):

        volume_float = volume / 100

        if ctx.voice_client.source is None:
            await ctx.send('Ich spiele gerade keine Musik ab')
            return

        elif (volume < 0) or (volume > 100):
            await ctx.send('Bitte gib eine Zahl zwischen 0 und 100 an')
            return

        if (ctx.voice_client.source.volume - volume_float) < .1:
            while ctx.voice_client.source.volume < volume_float:
                ctx.voice_client.source.volume += 0.05
                await asyncio.sleep(0.1)
        elif (ctx.voice_client.source.volume - volume_float) > -.1:
            while ctx.voice_client.source.volume > volume_float:
                ctx.voice_client.source.volume -= 0.05
                await asyncio.sleep(0.1)
        else:
            ctx.voice_client.source.volume = volume_float

        await ctx.send(f'Lautstärke auf {volume}% gesetzt')

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Du bist in keinem Voice Channel")
                return
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

    @stop.before_invoke
    @pause.before_invoke
    async def no_voice(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Ich bin in keinem Voice Channel")
            return
        elif not ctx.voice_client.is_playing():
            await ctx.send("Ich spiele gerade keine Musik ab")
            return

    @resume.before_invoke
    async def no_voice(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("Ich bin in keinem Voice Channel")
            return
        elif ctx.voice_client.is_playing():
            await ctx.send("Ich spiele bereits Musik ab")
            return
