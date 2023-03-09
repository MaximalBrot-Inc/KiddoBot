import discord
import voice_handler
import random
import time
import geburtstag_handler
import qrcode_handler
import weather_handler
from discord.ext import commands
#import pathlib

bot = commands.Bot(command_prefix = '!!' , intents = discord.Intents.all())


async def main_handler(message , bot):

    def check(m):
        return m.content == 'y' or m.content == 'yes' or m.content == 'n' or m.content == 'no' or m.content == 'ja' or m.content == 'nein'

    def Schalter():
        readline = open("switch.txt", "r")
        switch_state = readline.read()
        switch = "error"
        if switch_state == 'True':
            switch = "an"
        if switch_state == 'False':
            switch = "aus"
        return switch

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
                    "!!switchpls broken, bitte Brot#0685 kontaktieren, er muss wieder reparieren kommen :)")
        else:
            await message.channel.send("Du bist nicht berechtigt diesen Befehl auszuführen. Tut mir leid :)")

    if message.content.startswith('!!switchstate'):
        if message.author.id == 695885580629704734 or message.author.id == 408627107795828746:
            await message.channel.send(
                f'Möchtest du den status deines Schalters erfahren? (y , yes , ja / n, no, nein)')

            response = await bot.wait_for('message', check=check, timeout=15)
            if response.clean_content.lower() == 'y' or response.clean_content.lower() == 'yes' or response.clean_content.lower() == 'ja':
                await message.channel.send('Der Schalter ist ' + Schalter())

            elif response.clean_content.lower() == 'n' or response.clean_content.lower() == 'no' or response.clean_content.lower() == 'nein':
                await message.channel.send('Okidoki, dann halt nicht :)')

            else:
                await message.channel.send("Du bist zu dumm um zu verstehen, was ich dir sage :)")

        else:
            await message.channel.send("Du bist nicht berechtigt diesen Befehl auszuführen. Tut mir leid :)")

    #####MEGA GEBURTSTAG EVENT AAAAAAAAAAAAAAAAAAAAAAAAAAAA#############################################################
    if message.content == 'Geburtstag!':
        if message.author != bot.user:
            await geburtstag_handler.geburtstag(message, bot)

    if message.content == 'ping':
        await message.channel.send('pong')

    if message.content == 'hallo' or message.content == 'Hallo' or message.content == 'hallo kiddo' or message.content == 'Hallo kiddo' or message.content == 'hallo Kiddo' or message.content == 'Hallo Kiddo':
        await message.channel.send(f'Hallo {message.author.mention} :)')

    if message.content == '!!help':
        embedVar = discord.Embed(title="Hier sind alle Commands:", color=0xff00ff)
        embedVar.set_thumbnail(url="https://i.imgur.com/ed0LHRk.jpg")
        embedVar.add_field(name="!!help", value="Zeigt dir alle Commands", inline=False)
        embedVar.add_field(name="ping", value="pong", inline=False)
        embedVar.add_field(name="!!roll_dice", value="Würfelt eine Zahl", inline=False)
        embedVar.add_field(name="!!dance", value="Kiddo tanzt", inline=False)
        embedVar.add_field(name="!!witz", value="Kiddo erzählt dir einen Witz", inline=False)
        embedVar.add_field(name="!!qrcodepls", value="Kiddo erstellt dir einen QR-Code", inline=False)
        embedVar.add_field(name="!!details", value="Zeigt dir die Konfigurationen des Channels", inline=True)
        embedVar.add_field(name="!!details2", value="Zeigt dir die Konfigurationen des Servers", inline=False)
        embedVar.add_field(name="!!ABFAHRT", value="KIDDO FÄHRT DAVON!!", inline=False)
        embedVar.add_field(name="!!play", value="Spielt einen Song ab", inline=False)
        embedVar.add_field(name="!!stop", value="Stoppt den Song", inline=False)
        embedVar.add_field(name="!!hit", value="+ @User um jemanden zu schlagen", inline=False)
        embedVar.add_field(name="!!kiss", value="+ @User um jemanden zu küssen", inline=False)
        embedVar.add_field(name="!!hug", value="+ @User um jemanden zu umarmen", inline=False)
        await message.channel.send(embed=embedVar)

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

    if message.content.startswith("!!rolldice"):
        numberofrolls = message.content.split(' ')[1]
        numberofsides = message.content.split(' ')[2]
        await message.channel.send(f'Würfel einen Würfel mit {numberofsides} Seiten {numberofrolls} mal...')
        time.sleep(1)
        for i in range(int(numberofrolls)):
            await message.channel.send(random.randint(1, int(numberofsides)))

    if message.content.startswith("!!dance"):
        dance = open("gifs.txt", "r")
        dance = dance.readlines()
        dance = random.choice(dance)
        await message.channel.send(dance)

    if message.content == '!!witz':
        zahl = random.randint(1 , 100)
        if zahl == 1:
            await message.channel.send("Du bist so hässlich, dass man dich nicht mal mit einem Taschenrechner vergleichen kann. Kein Witz. Einfach die Wahrheit.")
        else:
            witze = open("witze.txt", "r")
            witze = witze.readlines()
            witze = random.choice(witze)
            witze = str(witze)
            await message.channel.send(witze)

    if message.content == '!!qrcodepls':
        await qrcode_handler.qrcode(message, bot)


    if message.content == '!!recordpls' or message.content =='!!stoppls' or message.content == '!!disconnectpls':
        await voice_handler.record_voice(bot, message)


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
        else:
            pass

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
        try:
            kiss = message.content.split(' ')[1]

            kiss = message.mentions[0].nick
            if kiss == None:
                kiss = message.mentions[0].name

            kisser = message.author.nick
            if kisser == None:
                kisser = message.author.name

            file = open("kiss.txt", "r")
            embedVar = discord.Embed(title="😘 Kiss", color=0xff00ff)
            embedVar.add_field(name=f"**{kiss}**!" f" Du wirst von **{kisser}** geküsst!", value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await message.channel.send(embed=embedVar)
            file.close()
        except IndexError:
            file = open("kiss.txt", "r")
            embedVar = discord.Embed(title="😘 Kiss", color=0xff00ff)
            embedVar.add_field(name=f"**{message.author.nick}**! " 'küsst jeden!', value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await message.channel.send(embed=embedVar)
            file.close()

    if message.content.startswith("!!hug"):
        try:
            hug = message.content.split(' ')[1]
            hug = message.mentions[0].nick
            if hug == None:
                hug = message.mentions[0].name

            hugger = message.author.nick
            if hugger == None:
                hugger = message.author.name

            file = open("hug.txt", "r")
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{hug}**! " 'Du wirst von ' f"**{hugger}** umarmt!", value="",
                               inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await message.channel.send(embed=embedVar)
            file.close()

        except IndexError:
            file = open("hug.txt", "r")
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{message.author.nick}** umarmt jeden!", value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await message.channel.send(embed=embedVar)
            file.close()

    if message.content.startswith("!!hit"):
        try:
            hit = message.content.split(' ')[1]
            hit = message.mentions[0].nick
            if hit == None:
                hit = message.mentions[0].name

            hitter = message.author.nick
            if hitter == None:
                hitter = message.author.name

            file = open("hit.txt", "r")
            embedVar = discord.Embed(title="😠 Hit!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{hit}**! " 'Du wirst von **' + f"{hitter}** geschlagen!", value="",
                               inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await message.channel.send(embed=embedVar)
            file.close()
        except IndexError:
            file = open("hit.txt", "r")
            embedVar = discord.Embed(title="😠 Hit!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{message.author.nick}**! " 'schlägt jeden!', value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await message.channel.send(embed=embedVar)
            file.close()

    if message.content.startswith("!!Wetter" or "!!wetter"):
        await weather_handler.get_weather(message)
    elif message.content.startswith("!!Morgen"):
        await weather_handler.get_weather_forecast(message)
    elif message.content.startswith("!!Alarm"):
        await weather_handler.get_weather_alert(message)


