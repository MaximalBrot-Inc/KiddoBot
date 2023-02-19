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
#import message_handler
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

async def switchstate(message):
    if message.content.startswith('!!switchpls'):
        if message.author.id == 695885580629704734 or message.author.id == 408627107795828746:
            readline = open("switch.txt", "r")
            switch_state = readline.read()
            if switch_state == 'False':
                await message.channel.send("Der Schalter ist an. Alle neuen Mitglieder werden gebannt. :)")
                readline = open("switch.txt", "w")
                readline.write('True')
            elif switch_state == 'True':
                await message.channel.send("Der Schalter ist aus. Alle neuen Mitglieder werden begrüßt. :)")
                readline = open("switch.txt", "w")
                readline.write('False')
        else:
            await message.channel.send(
                "!Switchpls broken, bitte Brot#0685 kontaktieren, er muss wieder reparieren kommen :)")
    else:
        await message.channel.send("Du bist nicht berechtigt diesen Befehl auszuführen. Tut mir leid :)")
@commands.command(name = 'switchpls' , help = 'Schaltet den Schalter um (nur wenn du cool bist)')
async def switch(ctx):
    if ctx.content == '-switchpls':
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            readline = open("switch.txt", "r")
            switch_state = readline.read()
            if switch_state == 'True':
                switch_state = 'False'
                await ctx.send('Der Schalter wurde ausgeschaltet')
            if switch_state == 'False':
                switch_state = 'True'
                await ctx.send('Der Schalter wurde eingeschaltet')
            switch = open("switch.txt", "w")
            switch.write(switch_state)
            switch.close()
        else:
            await ctx.send('Du bist nicht cool genug um den Schalter umzuschalten :)')


#@bot.event
#async def on_message(message):
 #   if message.author != bot.user:
  #      await message_handler.main_handler(message, bot)

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

@bot.event
async def on_message(message):
    #####MEGA GEBURTSTAG EVENT AAAAAAAAAAAAAAAAAAAAAAAAAAAA#############################################################
    if message.content == 'Geburtstag!':
        await message.channel.send('Oh hallo! Es is scho der 13. Februar? Des is heftig... I hab was tolles vorbereitet schau mal:')
        time.sleep(2)
        await message.channel.send("Lea war an diesem Tag besonders müde, denn sie hatte einen langen Schultag hinter sich.",
                                   file=discord.File("Bild1.JPG"))

        time.sleep(5)
        await message.channel.send("Eigentlich wollte sie nur noch zurück ins Internat um sich auszuruhen. "
                                    "Doch dann fällt ihr was ein. Soll sie noch vorher zu McDonald's (A) oder doch lieber Geld sparen und Direkt ins Internat (B)?"
                                    ,file=discord.File("Bild2.png"))

        response = await bot.wait_for("message" , timeout = 60)
        if response.clean_content.lower() == "a":
            await message.channel.send("Lea hat lust auf McDonald's. Als sie das Restaurant betritt, ging sie zu einem der freien Bestellterminals." ,
                                       file = discord.File("MCD.png"))
            time.sleep(5)
            await message.channel.send('Als sie gerade anfangen möchte zu bestellen, poppte auf ihrem Bildschirm ein Bild auf.'
                                       ' Es zeigte einen Gutschein mit bunten Ballons und einem Kuchen und der Überschrift: '
                                       '"Alles Gute zum  Geburtstag Frau Kapeller! Um solch einen besonderen Tag zu feiern, geben wir dir ein BigMac Menü Gratis!"'
                                       , file = discord.File("Terminal.png"))
            time.sleep(15)
            await message.channel.send("Lea war nun Traurig und Glücklich zugleich. Glücklich, "
                                       "da sie ein gratis Menü bekommen hatte und traurig, weil ihr auf einmal eingefallen ist, "
                                       "dass heute ihr geburtstag ist, und ihr noch niemand gratuliert hatte."
                                       , file = discord.File("Grlucklichtraurig.png"))
            time.sleep(10)
            await message.channel.send("Sie isst ihren BigMac und geht traurig zurück ins Internat, wo sie nichts besonderes erwartet."
                                       , file = discord.File("bubu.png"))

            time.sleep(10)
            await message.channel.send("Doch als sie die Tür zu ihrem Zimmer öffnete, wurde sie von lautem Jubel und Gesang überrascht."
                                       " Ihre Freunde hatten eine Überraschungsparty für sie organisiert,  denn heute war ja Leas Geburtstag! "
                                       "Lea konnte ihr Glück kaum fassen. Es gab Geschenke und Maxi hatte versucht einen Kuchen zu backen!"
                                       ,file = discord.File("überraschung.png"))

            time.sleep(15)
            await message.channel.send("Jedoch mit nur so semi Erfolg." , file = discord.File("kuchen.png"))

            time.sleep(5)
            await message.channel.send("Sie verbrachte den Abend damit, mit ihren Freunden zu lachen und zu feiern." ,
                                       file = discord.File("Feiern.png"))

            time.sleep(5)
            await message.channel.send("Als die Party zu Ende war und alle nach Hause gingen, legte sich Lea zufrieden in ihr Bett. "
                                       "Sie dachte daran, wie viel Freude ihr dieser Abend brachte, und wie toll ihre Freunde sind."
                                       , file = discord.File("Ende.png"))

            time.sleep(10)
            await message.channel.send("Ende :)")

        elif response.clean_content.lower() == "b":
            await message.channel.send('"Vielleicht sollte ich doch eher Geld sparen" dachte sie sich.\n '
                                       'Als sie losging, fällt ihr auf einmal ein, dass ja heute ihr Geburtstag ist, und ihr noch niemand gratuliert hat.')

            time.sleep(8)
            await message.channel.send("Lea geht traurig zurück in ihr Internat, wo sie nichts besonderes erwartet."
                                       , file = discord.File("bubu.png"))

            time.sleep(10)
            await message.channel.send('Doch als sie die Tür zu ihrem Zimmer öffnete, wurde sie von lautem Jubel und Gesang überrascht.'
                                       ' Ihre Freunde hatten eine Überraschungsparty für sie organisiert,  denn heute war ja Leas Geburtstag! '
                                       'Lea konnte ihr Glück kaum fassen. Es gab Geschenke und Maxi hatte versucht einen Kuchen zu backen!'
                                       ,file = discord.File("überraschung.png"))

            time.sleep(15)
            await message.channel.send("Jedoch mit nur so semi Erfolg." , file = discord.File("kuchen.png"))

            time.sleep(5)
            await message.channel.send("Sie verbrachte den Abend damit, mit ihren Freunden zu lachen und zu feiern." ,
                                       file = discord.File("Feiern.png"))

            time.sleep(5)
            await message.channel.send("Als die Party zu Ende war und alle nach Hause gingen, legte sich Lea zufrieden in ihr Bett. "
                                       "Sie dachte daran, wie viel Freude ihr dieser Abend brachte, und wie toll ihre Freunde sind."
                                       , file = discord.File("Ende.png"))

            time.sleep(10)
            await message.channel.send("Ende :)")


    if message.content == 'ping':
        await message.channel.send('pong')

    if message.content == '-help':
        embedVar = discord.Embed(title="Hier sind alle Commands:" , color=0xff00ff)
        embedVar.add_field(name="-ping" , value="pong" , inline=False)
        embedVar.add_field(name="-roll_dice" , value="Würfelt eine Zahl" , inline=False)
        embedVar.add_field(name="-dance" , value="Kiddo tanzt" , inline=False)
        embedVar.add_field(name="-details" , value="Zeigt dir die Konfigurationen des Channels" , inline=True)
        embedVar.add_field(name="-details2" , value="Zeigt dir die Konfigurationen des Servers" , inline=False)
        embedVar.add_field(name="-ABFAHRT" , value="KIDDO FÄHRT DAVON!!" , inline=False)
        embedVar.add_field(name="-help" , value="Zeigt dir alle Commands" , inline=False)
        embedVar.add_field(name="-play" , value="Spielt einen Song ab" , inline=False)
        embedVar.add_field(name="-stop" , value="Stoppt den Song" , inline=False)
        await message.channel.send(embed=embedVar)
    else:
        pass

    if message.content.startswith('!!lösche'):
        if message.author.id == 695885580629704734 or message.author.id == 408627107795828746:
            completeText = message.content.split(' ')[1]
            Limit = int(completeText)
            if Limit == 1:
                await message.channel.send('Eine Nachricht wird gelöscht... :)')
            elif Limit > 1:
                await message.channel.send(f'{Limit} Nachrichten werden gelöscht... :)')
            Limit = Limit + 2
            time.sleep(2)
            await message.channel.purge(limit=int(Limit))
            if Limit == 3:
                print('Eine Nachricht wurde gelöscht. Glückwunsch!')
            else:
                print(f'{Limit - 2} Nachrichten wurden gelöscht. Glückwunsch!')
        else:
            await message.channel.send('Du bist nicht cool genug um diesen Befehl auszuführen. Tut mir leid :)')


    if message.content == '!!details':
        if message.author.id == 695885580629704734 or message.author.id == 408627107795828746:
            await message.author.create_dm()
            await message.author.dm_channel.send(f"```"
                                    f"Halli Hallo 💕\n"
                                    f"Hier sind ein paar Details zu dem Channel :) \n"
                                    f"Channel: {message.channel}\n"
                                    f"Channel ID: {message.channel.id}\n"
                                    f"Channel Name: {message.channel.name}\n"
                                    f"Channel Type: {message.channel.type}\n"
                                    f"Channel Category: {message.channel.category}\n"
                                    f"Channel Category ID: {message.channel.category_id}\n"
                                    f"Channel Category Name: {message.channel.category.name}\n"
                                    f"Channel Category Type: {message.channel.category.type}\n"
                                    f"Channel Category Position: {message.channel.category.position}\n"
                                    f"TTS is {message.tts}\n"
                                    f"```")


    if message.content == '!!details2':
        if message.author.id == 695885580629704734 or message.author.id == 408627107795828746:
            await message.author.create_dm()
            await message.author.dm_channel.send(f"```"
                        f"Halli Hallo 💕\n"
                        f"Hier sind ein paar Details zu dem Server :) \n"
                        f"Server: {message.guild}\n"
                        f"Server ID: {message.guild.id}\n"
                        f"Server Name: {message.guild.name}\n"
                        f"Server Owner: {message.guild.owner}\n"
                        f"Server Owner ID: {message.guild.owner_id}\n"
                        f"Server Icon: {message.guild.icon}\n"
                        f"Server Splash: {message.guild.splash}\n"
                        f"Server Banner: {message.guild.banner}\n"
                        f"Server Discovery Splash: {message.guild.discovery_splash}\n"
                        f"Server Description: {message.guild.description}\n"
                        f"Server Features: {message.guild.features}\n"
                        f"```")
    else:
        pass


    if message.content.startswith("!!kiss"):
#        kiss = message.content.split(' ')[1]
 #       kiss = kiss.replace("<", "")
  #      kiss = kiss.replace(">", "")
   #     kiss = kiss.replace("@", "")
    #    user = await bot.fetch_user(kiss)
        file = open("kiss.txt", "r")
        #gif = random.choice(file.readlines())

        embedVar = discord.Embed(title="😘Kiss!", color=0xff00ff)
        embedVar.add_field(name='@' + f"{message.author} küsst " '@' + f"{message.mentions[0]}!" , value = "" , inline=False)

        embedVar.set_image(url = str(random.choice(file.readlines())))
        await message.channel.send(embed=embedVar)

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