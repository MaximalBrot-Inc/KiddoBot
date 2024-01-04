import discord
import time
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!!', intents=discord.Intents.all())


async def voice(member, before, after):
    global role
    if str(after.channel) == '➕ Erstelle Channel':
        if member.nick == None:
            channel = await after.channel.clone(name=f"{member.name}'s channel")
        else:
            channel = await after.channel.clone(name=f"{member.nick}'s channel")

        await member.move_to(channel)
        if len(after.channel.members) == 1:
            role = await after.channel.guild.create_role(name=f'{after.channel.name} owner',
                                                         color=discord.Color(633573), reason='Channel owner')
            await after.channel.set_permissions(role, overwrite=discord.PermissionOverwrite(manage_channels=True,
                                                                                            connect=True, speak=True,
                                                                                            stream=True,
                                                                                            view_channel=True))
            await member.add_roles(role)

    if str(before.channel) != '➕ Erstelle Channel' and str(before.channel) != 'None' and str(
            before.channel) != '🎵 Musik':
        if before.channel.category.name == '⋙ 🎤 Voice Channels ⋘' or '🎤 Voice Channels':
            if len(before.channel.members) == 0:
                await member.remove_roles(role)
                await before.channel.delete()
                await role.delete()


async def record_voice(bot, message):
    if message.content == '!!recordpls':
        channel = message.author.voice.channel
        await channel.connect()
        await message.channel.send('Verbinde mich mit dem Voicechannel...')
        await message.channel.send('Verbindung erfolgreich!')
        channel.start_recording(testsink(), finished_callback, ctx.channel)

    if message.content == '!!stoppls':
        channel = message.author.voice
        await channel.disconnect(bot)
        await message.channel.send('Stoppe die Aufnahme...')
        channel.stop_recording()
        await message.channel.send('Aufnahme erfolgreich gestoppt!')

    if message.content == '!!disconnectpls':
        channel = message.guild.voice_client
        channel.stop_recording()
        await channel.disconnect()
        await message.channel.send('Aufnahme gestoppt und Verbindung erfolgreich getrennt!')
