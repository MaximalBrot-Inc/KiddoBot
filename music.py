import discord
import pytube
import os

async def play(message):
    channel = message.author.voice.channel
    await message.channel.send(f'Ich bin bald in {channel} :)')
    global file
    file = pytube.YouTube(message.content[6:]).streams.get_audio_only().download()
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(file))
    vc.is_playing()
    await message.channel.send('Ich spiele jetzt ' + message.content[6:] + ' :)')
    await os.remove(file)

async def pause(message):
    await message.guild.voice_client.pause()
    await message.channel.send('Ich habe die Musik pausiert :)')

async def resume(message):
    await message.guild.voice_client.resume()
    await message.channel.send('Ich habe die Musik fortgesetzt :)')

async def leave(message):
    await message.guild.voice_client.disconnect()
    await message.channel.send('Ich habe den Voice-Channel verlassen :)')
    os.remove(file)