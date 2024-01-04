"""
The new and improved KiddoBot.py file
Maximilian && Phillip
❤
12.01.2023
"""


import csv
import time
import random
import asyncio
import discord
import command_handler
from discord import app_commands
from discord.ext import commands
from help_system import HelpCommand
from command_handler import KiddoBot
#import voice_handler


def getname(ctx):
    user = ctx.author.guild.fetch_member.name(id)
    return user

with open("data.txt") as token:
    reader = csv.reader(token)
    TOKEN = next(reader)
    GUILD = next(reader)

TOKEN = TOKEN[0]

bot = commands.AutoShardedBot(
    commands.when_mentioned_or('!!'),
    intents=discord.Intents.all())

#bot.remove_command('switchstate')

bot.help_command = HelpCommand()

########################################################################

@bot.event
async def on_ready ():
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

    print("Moiners werter Herr :3    <3")



    await bot.add_cog(KiddoBot(bot))
    await bot.tree.sync()

########################################################################


@bot.event
async def on_member_join(member):
    await member.create_dm()
    ###Nicht so nette Nachrichten lol###
    readline = open("switch.txt", "r")
    switch_state = readline.read()
    if switch_state == 'True':
        ###Banne alle neuen Mitglieder###
        await member.dm_channel.send(
            'Tut mir leid, aber du bist noch nicht groß genug für den Server... :('
            'Versuche es in ein paar Jahren nochmal :) Tschüssi :)')
        await member.ban(
            reason = "Kiddo meint, du bist noch nicht groß genug für diesen Server. "
                     "Du bist gebannt :)")

    else:
    ###Nette Nachrichten für neue Mitglieder###
        await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server! Regeln? Durchlesen? Schwachsinn! '
                                    f'Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig. '
                                     f'Also keine Zeit verschwenden!!')


@bot.event
async def on_guild_join(guild):
    bans = open("ban_list.txt", "r")

    for line in bans:
        try:
            user = await bot.fetch_user(line)
            await guild.unban(user)
            print("Unbanned " + user.name)
        except:
            print("Failed to unban " + user.name)
            continue


########################################################################


#@bot.event
#async def on_voice_state_update(member, before, after):
 #   await voice_handler.voice(member, before, after)


########################################################################

bot.run(TOKEN)
