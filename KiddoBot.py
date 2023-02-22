'''
The new and improved KiddoBot.py file
Maximilian && Phillip
❤
12.01.2023
'''

import VoiceChannel
import discord
from discord.ext import commands
from discord import app_commands
import csv
import message_handler
import time
import random


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

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await message_handler.main_handler(message, bot)



#Slash commands in bearbeitung. Muss schaun wie de funktionieren lol
#@app_commands.command()
#async def rolldice(bot, interaction: discord.Interaction , member: discord.Member):
#    await interaction.response.send_message('Rolling the dice...' , ephemeral=True)
##############################################################################################

#BAUSTELLE
#    if message.content.startswith('.record'):
 #       channel = message.author.voice.channel
  #      await channel.connect()
   #     await message.channel.send('Recording...')
    #    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f'{time.asctime([t])}.mp3'))
     #   message.guild.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
      #  await message.channel.send('Finished!')
       # await message.guild.voice_client.disconnect()

    #ctx.voice_client.start_recording(discord.sinks.MP3Sink(), finished_callback, ctx) # Start the recording
    #await ctx.respond("Recording...")

#async def finished_callback(sink, ctx):
 #   # Here you can access the recorded files:
  #  recorded_users = [
   #     f"<@{user_id}>"
    #    for user_id, audio in sink.audio_data.items()
    #]
    #files = [discord.File(audio.file, f"{user_id}.{sink.encoding}") for user_id, audio in sink.audio_data.items()]
    #await ctx.channel.send(f"Finished! Recorded audio for {', '.join(recorded_users)}.", files=files)

#@bot.command()
#async def stop_recording(ctx):
 #   ctx.voice_client.stop_recording() # Stop the recording, finished_callback will shortly after be called
  #  await ctx.respond("Stopped!")


##############################################################################################


bot.run(TOKEN)