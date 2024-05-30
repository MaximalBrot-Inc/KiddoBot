import os
import discord
from discord.ext import commands
from pytube import YouTube, exceptions, Search

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


async def stream_audio(ctx, audio_stream):
    source = discord.FFmpegPCMAudio(audio_stream.url, **FFMPEG_OPTIONS)

    discord.VoiceClient.play(source=source, after=None, self=ctx.voice_client)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=['p'], brief='Spielt Musik ab', description='Spielt Musik ab')
    async def play(self, ctx, *, titel=None, link=None):
        if (titel is None) & (link is None):
            await ctx.send('Du hast weder einen Titel noch Link angegeben :(')
            await discord.TextChannel.send(content='Ich benötige aber eins von beiden sonst kann ich nichts abspielen',
                                           self=ctx.channel)
            return

        try:
            await discord.VoiceChannel.connect(self=ctx.author.voice.channel)
        except discord.ClientException:
            await ctx.send('Ich bin schon in einem Voice Channel!')
        if link is not None:
            if link.startswith('https://www.youtube.com/watch?v=') or link.startswith('https://youtu.be/'):
                try:
                    audio_stream = YouTube(link)
                    audio_stream = audio_stream.streams.get_audio_only()

                    await stream_audio(ctx, audio_stream)

                except exceptions.VideoUnavailable:
                    await ctx.send('Das Video ist nicht verfügbar :(')
            else:
                print(link)
                print(link.startswith('https://www.youtube.com/watch?v=') or link.startswith('https://youtu.be/'))
                await ctx.send('Das ist kein Youtube Link!')
                await discord.TextChannel.send(content='Andere Links werden noch nicht unterstützt :(',
                                               self=ctx.channel)
                await discord.TextChannel.send(
                    content='P.S. Ich bin noch in der Entwicklung, also bitte nicht zu hart sein :3', self=ctx.channel)
                await discord.TextChannel.send(
                    content='P.P.S. Ich bin ein Bot, also kann ich nicht wirklich fühlen, aber ich gebe mir Mühe!',
                    self=ctx.channel)
        else:
            try:
                results = Search(titel)
                audio_stream = results.results[0]
                audio_stream = audio_stream.streams.get_audio_only()

                await stream_audio(ctx, audio_stream)

            except exceptions.VideoUnavailable:
                await ctx.send('Das Video ist nicht verfügbar :(')

    @commands.hybrid_command(aliases=['s'], brief='Stoppt die Musik', description='Stoppt die Musik')
    async def stop(self, ctx):
        try:
            discord.VoiceClient.stop(self=ctx.voice_client)
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
