'''
A very friendly Discord bot
Maximilian
08.01.23
'''

# bot.py
import os
import time
import discord
from dotenv import load_dotenv

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
client = discord.Client(intents = intents)

@client.event
async def on_ready ():
    for guild in client.guilds:
       if guild.name == GUILD:
           break

    print(f'{client.user} hat sich in folgenden Server eingespeist: \n' f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Servermitglieder: \n - {members}')
    print("Was geht! Ich bin bereit ein paar Server zu crashen baby!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')

    elif message.content == 'hello':
        await message.channel.send('Hello!')

    elif message.content == '@everyone':
        await message.channel.send('Halt die Fresse du Penner!')

    elif message.content == '!help':
        await message.channel.send('Du bekommst keine Hilfe loser!')

    elif message.content == 'Joe':
        await message.channel.send("Who's Joe? I don't know any Joe!")

    elif message.content == 'Joe Mama' or message.content == 'Joe Mama!':
        await message.channel.send("Damn...")

@client.event
async def on_message2(message):
    if 'happy birthday' in message.content.lower():
        while True:
            await message.channel.send('Happy Birthday! 🎈🎉')
            time.sleep(0.6)


client.run('TOKEN')