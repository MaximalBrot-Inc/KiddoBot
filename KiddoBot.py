'''
The new and improved KiddoBot.py file
Maximilian && Phillip
❤
12.01.2023
'''

import discord
from discord.ext import commands
from discord import app_commands
import csv
import message_handler
import time
import random
import voice_handler


def check(message):
    return message.content == 'a'

def getname(ctx):
    user = ctx.author.guild.fetch_member.name(id)
    return user

with open("data.txt") as token:
  reader = csv.reader(token)
  TOKEN = next(reader)
  GUILD = next(reader)

TOKEN = TOKEN[0]

bot = commands.Bot(command_prefix = '!!' , intents = discord.Intents.all())
#bot.remove_command('switchstate')
bot.remove_command('help')

##############################################################################################

@bot.event
async def on_ready ():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='durch dein Fenster :)'))
    for guild in bot.guilds:
       if guild.name == GUILD:
           break

    print(f'{bot.user.name} hat sich in folgenden Server eingespeist: \n' f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Servermitglieder: \n - {members}')
    print("Moiners werter Herr!")

    await bot.tree.sync()


##############################################################################################


@bot.event
async def on_member_join(member):
    await member.create_dm()
    ###Nicht so nette Nachrichten lol###
    readline = open("switch.txt", "r")
    switch_state = readline.read()
    if switch_state == 'True':
        ###Banne alle neuen Mitglieder###
        await member.dm_channel.send('Tut mir leid, aber du bist noch nicht groß genug für den Server... :( Versuche es in ein paar Jahren nochmal :) Tschüssi :)')
        await member.ban(reason = "Kiddo meint, du bist noch nicht groß genug für diesen Server. Du bist gebannt :)")

    else:
    ###Nette Nachrichten für neue Mitglieder###
        await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server! Regeln? Durchlesen? Schwachsinn! '
                                 f'Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig. Also keine Zeit verschwenden!!')

##############################################################################################

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await message_handler.main_handler(message, bot)

##############################################################################################

#Slash commands in bearbeitung. Muss schaun wie de funktionieren lol
#@app_commands.command()
#async def rolldice(bot, interaction: discord.Interaction , member: discord.Member):
#    await interaction.response.send_message('Rolling the dice...' , ephemeral=True)
##############################################################################################

@bot.event
async def on_voice_state_update(member, before, after):
    await voice_handler.voice(member, before, after)

##############################################################################################

bot.run(TOKEN)