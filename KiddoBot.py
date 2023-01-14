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
                                 f'Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig. Also keine Zeit verschwenden!!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

    elif message.content.startswith('@everyone'):
        await message.channel.send('LEISE!')

    elif message.content.startswith('!lösche'):
        completeText = message.content.split(' ') [1]
        Limit = int(completeText)
        if Limit == 1:
           await message.channel.send('Eine Nachricht wird gelöscht... :)')
        elif Limit > 1:
            await message.channel.send(f'{Limit} Nachrichten werden gelöscht... :)')
        Limit = Limit + 2
        time.sleep(2)
        await message.channel.purge(limit = int(Limit))
        print(f'{Limit} Nachrichten wurden gelöscht. Glückwunsch!')

    if message.content.startswith('!ban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member : Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await message.channel.send(f'{member} wird gebannt... Tschüssi {member} :)')
                time.sleep(2)
                await member.ban()
                await message.channel.send(f'{member} wurde gebannt :)')
            else:
                await message.channel.send('Der User wurde nicht gefunden!')

    if message.content.startswith('!bänn all'):
        await message.channel.send('Alle User werden gebannt... Tschüssi :)')
        time.sleep(2)
        for guild in message.client.guild:
            for member in guild.members:
                await member.ban()
                await message.channel.send(f'{member} wurde gebannt!')
        #await message.guild.ban()
        #await message.channel.send('Alle User wurden gebannt!')

###Funktioniert NOCH nicht###Notiz: Wahrscheinlich kann man keine Channel in einem Community Server löschen###
#@client.event
#async def on_message(message):
  #  if message.content.startswith("channel löschen"):
     #   await message.channel.send('Okidoki bin dabei :)')
        #for guild in client.guilds:
           # for channel in guild.channels:
              #  await channel.delete()



#@client.event
#async def on_message(message):
  #  if message.content.startswith('!lösche'):
     #   completeText = message.content.split(' ') [1]
        #Limit = int(completeText)
        #Limit = Limit + 1
       # await message.channel.purge(limit = int(Limit))
       # print(f'{Limit} Nachrichten wurden gelöscht. Glückwunsch!')

###Unendliche Nachrichten###Notiz: Wenn man sie aktiviert funktioniert alles andere nicht mehr keine ahnung warum###
#@client.event
#async def on_message(message):
  #  if message.content =='happy birthday':
     #   while True:
        #    await message.channel.send('Happy Birthday! 🎈🎉')
           # time.sleep(0.6)


client.run(TOKEN)