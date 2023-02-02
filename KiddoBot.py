'''
The new and improved KiddoBot.py file
Maximlian && Phillip
❤
12.01.2023
'''

import discord
import csv
import message_handler



client = discord.Client(intents = discord.Intents.all())

with open("data.txt") as token:
  reader = csv.reader(token)
  TOKEN = next(reader)
  GUILD = next(reader)

TOKEN = TOKEN[0]


##############################################################################################

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



@client.event
async def on_message(message):
    if message.author != client.user:
        await message_handler.main_handler(message, client)

#Kann voice channel erstellen aber noch nicht den member reinziehen!
@client.event
async def on_voice_state_update(member, before, after):
    if str(after.channel) == '➕ Erstelle Channel':
        #if str(after) != str(before):
        channel= await after.channel.clone(name=f'{member}s channel')
        await member.move_to(channel)
    #lölsche den channel wenn der member den channel verlässt
    if str(before.channel) != '➕ Erstelle Channel' and str(before.channel) != 'None' and str(before.channel) != '🎵 Musik':
        if before.channel.category.name == '⋙ 🎤 Voice Channels ⋘' or'🎤 Voice Channels':
            if len(before.channel.members) == 0:
                await before.channel.delete()



##############################################################################################


client.run(TOKEN)