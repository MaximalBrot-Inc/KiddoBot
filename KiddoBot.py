"""
The new and improved KiddoBot.py file
Maximilian && Phillip
❤
12.01.2023
"""

import csv
import sys
import logging

import discord
import ctypes.util
from discord.ext import commands
from music_handler import Music
from help_system import HelpCommand
from command_handler import Commands
from weather_handler import Weather


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Assume client refers to a discord.Client subclass..


def getname(ctx):
    user = ctx.author.guild.fetch_member.name(id)
    return user


with open("data.txt") as token:
    reader = csv.reader(token)
    TOKEN = next(reader)
    GUILD = next(reader)

TOKEN = TOKEN[0]

'''
if sys.platform == "linux":
    #discord.opus.load_opus()
    discord.opus.load_opus(ctypes.util.find_library('opus'))
    print(ctypes.util.find_library('opus'))
    print(discord.opus.is_loaded())
'''

bot = commands.AutoShardedBot(
    commands.when_mentioned_or('!!'),
    intents=discord.Intents.all())

# bot.remove_command('switchstate')

bot.help_command = HelpCommand()


########################################################################

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name='durch dein Fenster :)'))
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(f'{bot.user.name} hat sich in folgenden Server eingespeist: \n\n'
          f'{guild.name} (id: {guild.id})')

    members = '\n        - '.join([member.name for member in guild.members])
    print(f'    Servermitglieder: \n        - {members}')

    print("\n    Alle Rollen in diesem Server (Von unten nach oben):")
    for role in guild.roles:
        print(f'        {role}')

    print("----------------------------------")

    print("Moiners, werter Herr :3")

    await bot.add_cog(Commands(bot))
    await bot.add_cog(Music(bot))
    await bot.add_cog(Weather(bot))
    await bot.tree.sync()


########################################################################


@bot.event
async def on_member_join(member):
    readline = open("switch.txt", "r")
    switch_state = readline.read()
    if switch_state == "on":
        reason = "Oopsie!"
        await member.create_dm()
        ###Banne alle neuen Mitglieder###
        await member.dm_channel.send("Oopsie, fehler! :face_with_spiral_eyes:")
        await member.ban(reason=reason)


@bot.event
async def on_guild_join(guild):
    bans = open("ban_list.txt", "r")
    link = "https://discord.gg/wrPWp3THwb"

    for line in bans:
        try:
            user = await bot.fetch_user(line)
            print(user)
            await guild.unban(user)
            print("Unbanned " + user.name)

            await user.create_dm()
            await user.dm_channel.send(
                f'Hewwow {user.name}, du wurdest erfolgreich von mir entbannt >////< \n'
                f'Mit diesem Link kannst du wieder auf den Server: {link} :33\n')

        except discord.NotFound:
            print("Failed to unban " + user.name)
            continue


########################################################################


# @bot.event
# async def on_voice_state_update(member, before, after):
#   await voice_handler.voice(member, before, after)


########################################################################

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
