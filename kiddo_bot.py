'''
a friendly Discord bot
Maximilian
08.01.2023
'''
# bot.py
import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import asyncio

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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Du hast nicht die richtige Rolle um diesen Befehl auszuführen lol')


############################################################################################################


@bot.hybrid_command(name = 'create_channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name = 'kiddos-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.hybrid_command(name = 'helö' , help = ' | Wenn du nicht schreiben kannst')
async def heloe (ctx):
        await ctx.channel.send('Hier ist deine Hilfe: ' , file = discord.File ("C:\_FSST\Jaeger\Shooting Range\KiddoBot\Bruh.png"))

@bot.hybrid_command(name='roll_dice', help=' | Gib nach dem Befehl 2 Zahlen ein.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.hybrid_command (name = 'happy' , help = ' | Kiddo wünscht dir alles gute zum Geburtstag!')
async def on_message2(ctx):
            await ctx.channel.send('Happy Birthday! 🎈🎉')

@bot.hybrid_command (name = 'happyhappy' , help = ' | Kiddo wünscht dir viel gutes zum Geburtstag!')
async def on_message2(ctx):
        while True:
            await ctx.channel.send('Happy Birthday! 🎈🎉')
            time.sleep(0.8)

@bot.command (name = '!delete-messages-from' , help = ' | Kiddo löscht alle Nachrichten von einem bestimmten User')
@commands.has_role('admin')
async def message_delete (ctx, member: discord.Member):
    await ctx.channel.purge(limit=100, check=lambda msg: msg.author == member)

@bot.hybrid_command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')


############################################################################################################

bot.run(TOKEN)