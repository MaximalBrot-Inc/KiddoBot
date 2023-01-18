'''
A very friendly Discord bot
Maximlian
12.01.2023
'''
import discord
import os
from dotenv import load_dotenv
import time
import math
import random

intents = discord.Intents.all()
client = discord.Client(intents = intents)

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


def check(reaction, user):
    return user == message.author

def Schalter (response):
    if response == "y" or response == "yes" or response == "ja":
        switch = "an"
    if frage =="n" or response == "no" or response == "nein":
        switch = "aus"
    return switch

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
    ###Nicht so nette Nachrichten lol###
    if schalter == an:
        ###Banne alle neuen Mitglieder###
        await member.ban(reason = "Kiddo meint, du bist noch nicht groß genug für diesen Server. Du bist gebannt :)")
        await member.dm_channel.send('Tut mir leid, aber du bist noch nicht groß genug für den Server... :( Versuche es in ein paar Jahren nochmal :) Tschüssi :)')

    elif schalter == aus:
    ###Nette Nachrichten für neue Mitglieder###
        await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server! Regeln? Durchlesen? Schwachsinn! '
                                 f'Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig. Also keine Zeit verschwenden!!')






@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!switchstatus'):

        await message.channel.send(f'Möchtest du den status deines Schalters erfahren? (y , yes , ja / n, no, nein)')
        response =  await client.wait_for("y", check=check , timeout = 15)
        if response.clean_content.lower() == 'y' or response.clean_content.lower() == 'yes' or response.clean_content.lower() == 'ja':
            await client.say('Der Schalter ist ' + Schalter(response))

        elif response.clean_content.lower() == 'n' or response.clean_content.lower() == 'no' or response.clean_content.lower() == 'nein':
            await client.say('Okidoki, dann halt nicht :)')

        else:
            await client.say("Du bist zu dumm um zu verstehen, was ich dir sage :)")
        ###Wenn wir ganz gemein unterwegs sind###
            #await message.author.ban(reason = "Kiddo meint, du bist zu dumm um zu verstehen, was ich dir sage. Du bist gebannt :)")

        #await message.channel.send(f'Der Status deines Schalters ist {Schalter(frage)}')

       # if a == ('y' or 'yes' or 'ja'):
          #  frage = "y"
            #await message.channel.send(f'Der Schalter ist zur Zeit {Schalter(frage)} :)')
       # elif a == ('n' or 'no' or 'nein'):
          #  frage = "n"
            #await message.channel.send(f'Der Schalter ist zur Zeit {Schalter(frage)} :)')


        #if message.content.startswith('y' , 'yes' , 'ja'):
           # Switch = "y"
        #elif message.content.startswith('n' , 'no' , 'nein'):
           # Switch = "n"
            #await message.channel.send('OK! Der Schalter wurde nicht geändert :)')

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


    if message.content.startswith('!help'):
        await message.channel.send('Du brauchst wirklich hilfe :nauseated_face: :face_vomiting:')
        time.sleep(2)
        await message.channel.send(" ```"
                                   "Hier ist die Hilfe: \n"
                                   "!help: Zeigt diese Nachricht dödel! \n"
                                   "ping: Pong \n"
                                   "@ everyone: tu's nicht. \n"
                                   "!lösche belieb. Zahl: löscht beliebig viele Nachrichten \n"
                                   "!ban belieb. member: Bannt einen Member, wenn du die Rechte hast, das zu tun \n"
                                   "```")


###Unendliche Nachrichten###
    if message.content == 'happy birthday':
        while True:
            await message.channel.send('Happy Birthday! 🎈🎉')
            time.sleep(0.6)
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


client.run('TOKEN')