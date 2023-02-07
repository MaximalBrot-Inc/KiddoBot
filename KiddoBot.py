'''
The new and improved KiddoBot.py file
Maximlian && Phillip
❤
12.01.2023
'''

import VoiceChannel
import discord
from discord.ext import commands
import csv
import message_handler
import time


#bot = discord.Client(intents = discord.Intents.all())

with open("data.txt") as token:
  reader = csv.reader(token)
  TOKEN = next(reader)
  GUILD = next(reader)

TOKEN = TOKEN[0]

bot = commands.Bot(command_prefix = '-' , intents = discord.Intents.all())

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

@bot.event
async def on_voice_state_update(member, before, after):
    global role
    if str(after.channel) == '➕ Erstelle Channel':
        if member.nick == None:
            channel= await after.channel.clone(name=f"{member.name}'s channel")
        else:
            channel= await after.channel.clone(name=f"{member.nick}'s channel")

        await member.move_to(channel)
        if len(after.channel.members) == 1:
            role = await after.channel.guild.create_role(name=f'{after.channel.name} owner' ,  color = discord.Color(633573) ,  reason = 'Channel owner')
            await after.channel.set_permissions(role , overwrite=discord.PermissionOverwrite(manage_channels=True, connect=True, speak=True, stream=True, view_channel=True))
            await member.add_roles(role)

    if str(before.channel) != '➕ Erstelle Channel' and str(before.channel) != 'None' and str(before.channel) != '🎵 Musik':
        if before.channel.category.name == '⋙ 🎤 Voice Channels ⋘' or '🎤 Voice Channels':
            if len(before.channel.members) == 0:
                await member.remove_roles(role)
                await before.channel.delete()
                await role.delete()

##############################################################################################


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