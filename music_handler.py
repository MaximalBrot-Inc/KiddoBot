import os
import time

import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from pytube import YouTube, exceptions, Search

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

source = None


async def stream_audio(ctx, audio_stream):
    global source
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(audio_stream.url, **FFMPEG_OPTIONS), volume=0.5)

    discord.VoiceClient.play(source=source, after=None, self=ctx.voice_client)

    await ctx.interaction.followup.send(f'Spiele {audio_stream.title} ab')
    return source


async def stream_youtube(ctx, query):
    try:
        audio_stream = YouTube(query)
        audio_stream = audio_stream.streams.get_audio_only()

        await stream_audio(ctx, audio_stream)
    except exceptions.VideoUnavailable:
        await ctx.interaction.followup.send('Das Video ist nicht verfügbar :(')
        return



async def search_and_play(ctx, query):
    try:
        search = Search(query)
        audio_stream = search.results[0]
        audio_stream = audio_stream.streams.get_audio_only()

        await stream_audio(ctx, audio_stream)
    except exceptions.VideoUnavailable or IndexError:
        await ctx.interaction.followup.send('Ich konnte das Video nicht finden :(')
        return



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

        try:
            await discord.VoiceChannel.connect(self=ctx.author.voice.channel)
        except discord.ClientException:
            await ctx.send('Ich bin schon in einem Voice Channel!')

        if source.startswith('https://') or source.startswith('http://'):

            if source.startswith('https://www.youtube.com/watch?v=') or source.startswith('https://youtu.be/'):

                await stream_youtube(ctx, source)

            else:
                await ctx.interaction.followup.send('Das ist kein Youtube Link!')
                await discord.TextChannel.send(content='Andere Links werden noch nicht unterstützt :(',
                                               self=ctx.channel)
                await discord.TextChannel.send(
                    content='P.S. Ich bin noch in der Entwicklung, also bitte nicht zu hart sein :3', self=ctx.channel)
                await discord.TextChannel.send(
                    content='P.P.S. Ich bin ein Bot, also kann ich nicht wirklich fühlen, aber ich gebe mir Mühe!',
                    self=ctx.channel)
        else:
            await search_and_play(ctx, source)

    @commands.hybrid_command(aliases=['s'], brief='Stoppt die Musik', description='Stoppt die Musik')
    async def stop(self, ctx):
        try:
            discord.VoiceClient.stop(self=ctx.voice_client)
            await discord.VoiceClient.disconnect(self=ctx.bot.voice_client)

            await ctx.send('Musik gestoppt und Verbindung getrennt')

        except AttributeError:
            await ctx.send('Ich bin nicht in einem Voice Channel!')

    @commands.hybrid_command(brief='Pausiert die Musik', description='Pausiert die Musik')
    async def pause(self, ctx):
        try:
            discord.VoiceClient.pause(self=ctx.voice_client)
        except AttributeError:
            await ctx.send('Ich bin nicht in einem Voice Channel!')

    @commands.hybrid_command(brief='Setzt die Musik fort', description='Setzt die Musik fort')
    async def resume(self, ctx):
        try:
            discord.VoiceClient.resume(self=ctx.voice_client)
        except AttributeError:
            await ctx.send('Ich bin nicht in einem Voice Channel!')

    @commands.hybrid_command(alias=['vol'], brief='Ändert die Lautstärke', description='Ändert die Lautstärke')
    async def volume(self, ctx, volume: int):

        volume_float = volume/100

        if ctx.voice_client.source is None:
            await ctx.send('Ich spiele gerade keine Musik ab')
            return

        elif (volume < 0) or (volume > 100):
            await ctx.send('Bitte gib eine Zahl zwischen 0 und 100 an')
            return

        if (ctx.voice_client.source.volume-volume_float) < .1:
            while ctx.voice_client.source.volume < volume_float:
                ctx.voice_client.source.volume += 0.05
                time.sleep(0.1)
        elif (ctx.voice_client.source.volume-volume_float) > -.1:
            while ctx.voice_client.source.volume > volume_float:
                ctx.voice_client.source.volume -= 0.05
                time.sleep(0.1)
        else:
            ctx.voice_client.source.volume = volume_float

        await ctx.send(f'Lautstärke auf {volume}% gesetzt')


