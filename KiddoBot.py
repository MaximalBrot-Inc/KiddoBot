'''
A very friendly Discord bot
Maximlian
12.01.2023
'''
import discord
import os
from dotenv import load_dotenv
import time

intents = discord.Intents.all()
client = discord.Client(intents = intents)

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


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
    await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server! Regeln? Durchlesen? Schwachsinn! '
                                 f'Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig.Also keine Zeit verschwenden!!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

    elif message.content.startswith('!lösche'):
        completeText = message.content.split(' ') [1]
        Limit = int(completeText)
        Limit = Limit + 1
        await message.channel.purge(limit = int(Limit))
        print(f'{Limit} Nachrichten wurden gelöscht. Glückwunsch!')


#@client.event
#async def on_message(message):
  #  if message.content.startswith('!lösche'):
     #   completeText = message.content.split(' ') [1]
        #Limit = int(completeText)
        #Limit = Limit + 1
       # await message.channel.purge(limit = int(Limit))
       # print(f'{Limit} Nachrichten wurden gelöscht. Glückwunsch!')

###Unendliche Nachrichten###Notitz: Wenn man sie aktiviert funktioniert alles andere nicht mehr keine ahnung warum###
#@client.event
#async def on_message(message):
  #  if message.content =='happy birthday':
     #   while True:
        #    await message.channel.send('Happy Birthday! 🎈🎉')
           # time.sleep(0.6)


client.run('TOKEN')