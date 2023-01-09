'''
A very friendly Discord bot
Maximilian
08.01.23
'''
# bot.py
import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

#file = open("hallo.txt" , "r")
#aus der datei hallo.txt die erste zeile lesen und in eine Variable speichern
#TOKEN = file.readline()
#aus der datei hallo.txt die zweite zeile lesen und in eine Variable speichern
#GUILD = file.readline()

#file.close()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready ():
    for guild in bot.guilds:
       if guild.name == GUILD:
           break

    print(f'{bot.user} hat sich in folgenden Server eingespeist: \n' f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Servermitglieder: \n - {members}')
    print("Bot ready")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server! Regeln? Durchlesen? Schwachsinn! Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig.'
                                 f' Also keine Zeit verschwenden!!')

@bot.command(name = 'create_channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name = 'kiddos-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Du hast nicht die richtige Rolle um diesen Befehl auszuführen lol')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')

    elif message.content == 'hello':
        await message.channel.send('Hello!')

    elif message.content == '@everyone':
       await message.channel.send('Halt die Fresse du Penner!')

    elif message.content == 'Joe':
        await message.channel.send("Who's Joe? I don't know any Joe!")

    elif message.content == 'Joe Mama' or message.content == 'Joe Mama!':
        await message.channel.send("Damn...")


@bot.command(name='roll_dice', help=' | Gib nach dem Befehl 2 Zahlen ein.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command (name = 'happy' , help = ' | Kiddo wünscht dir alles gute zum Geburtstag!')
async def on_message2(ctx):
            await ctx.channel.send('Happy Birthday! 🎈🎉')

@bot.command (name = 'happyhappy' , help = ' | Kiddo wünscht dir viel gutes zum Geburtstag!')
async def on_message2(ctx):
        while True:
            await ctx.channel.send('Happy Birthday! 🎈🎉')
            time.sleep(0.8)

############################################################################################################

bot.run(TOKEN)