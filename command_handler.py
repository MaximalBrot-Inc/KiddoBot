import discord
#import voice_handler
import random
import time
#import geburtstag_handler
import qrcode_handler
import weather_handler
from discord.ext import commands
from Buttons import HL_Buttons
#from discord_components import DiscordComponents, Button
#import pathlib


def Schalter():
    readline = open("switch.txt", "r")
    switch_state = readline.read()
    switch = "error"
    if switch_state == 'True':
        switch = "an"
    if switch_state == 'False':
        switch = "aus"
    return switch
    def check(m):
        return m.content == 'y' or m.content == 'yes' or m.content == 'n' or m.content == 'no' or m.content == 'ja' or m.content == 'nein'

class KiddoBot(commands.Cog):
    bot = commands.Bot(commands.when_mentioned_or('!!'), intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    def freigabe():
        async def predicate(ctx):
            if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
                return True
            else:
                raise commands.MissingPermissions("Du bist nicht berechtigt diesen Befehl auszuführen. Tut mir leid :)")
        return commands.check(predicate)


    @bot.command()
    @freigabe()
    async def switchpls(self, ctx):
            readline = open("switch.txt", "r")
            switch_state = readline.read()
            if switch_state == 'False':
                await ctx.channel.send("Der Schalter ist an. Alle neuen Mitglieder werden gebannt. :)")
                readline = open("switch.txt", "w")
                readline.write('True')
            elif switch_state == 'True':
                await ctx.channel.send("Der Schalter ist aus. Alle neuen Mitglieder werden begrüßt. :)")
                readline = open("switch.txt", "w")
                readline.write('False')
            else:
                await ctx.channel.send(
                    "!!switchpls broken, bitte Brot#0685 kontaktieren, er muss wieder reparieren kommen :)")

    #TODO: Fix this command
    '''
    @bot.command()
    async def switchstate(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.channel.send(
                f'Möchtest du den status deines Schalters erfahren? (y , yes , ja / n, no, nein)')
            
            response = await ctx.wait_for('ctx', check=check, timeout=15)
            if response.clean_content.lower() == 'y' or response.clean_content.lower() == 'yes' or response.clean_content.lower() == 'ja':
                await ctx.channel.send('Der Schalter ist ' + Schalter())

            elif response.clean_content.lower() == 'n' or response.clean_content.lower() == 'no' or response.clean_content.lower() == 'nein':
                await ctx.channel.send('Okidoki, dann halt nicht :)')

            else:
                await ctx.channel.send("Du bist zu dumm um zu verstehen, was ich dir sage :)")
        else:
            await ctx.channel.send("Du bist nicht berechtigt diesen Befehl auszuführen. Tut mir leid :)")
    '''



    #####MEGA GEBURTSTAG EVENT AAAAAAAAAAAAAAAAAAAAAAAAAAAA#############################################################
    @bot.command()
    async def Geburtstag(self, ctx):
        await geburtstag_handler.geburtstag(ctx, bot)


    @bot.command(aliases=['Ping'])
    async def ping(self, ctx):
        await ctx.send('pong')

    @bot.command(aliases=['Hallo' , 'hallo kiddo' , 'Hallo kiddo' , 'hallo Kiddo' , 'Hallo Kiddo'])
    async def hallo(self,ctx):
        await ctx.send(f'Hallo {ctx.author.mention} :)')
    #if ctx.content == 'hallo' or ctx.content == 'Hallo' or ctx.content == 'hallo kiddo' or ctx.content == 'Hallo kiddo' or ctx.content == 'hallo Kiddo' or ctx.content == 'Hallo Kiddo':
       # await ctx.channel.send(f'Hallo {ctx.author.mention} :)')

    @bot.hybrid_command(aliases=['Hilfe'])
    async def hilfe(self, ctx):
        embedVar = discord.Embed(title="Hier sind alle Commands:", color=0xff00ff)
        embedVar.set_thumbnail(url="https://i.imgur.com/ed0LHRk.jpg")
        embedVar.add_field(name="!!hilfe", value="Zeigt dir alle Commands", inline=False)
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
        await ctx.send(embed=embedVar)

    @bot.command(aliases=['lösche'])
    async def clear(self, ctx, Limit=0):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            if Limit == 1:
                await ctx.channel.send('Eine Nachricht wird gelöscht... :)')
            elif Limit > 1:
                await ctx.channel.send(f'{Limit} Nachrichten werden gelöscht... :)')
            Limit = Limit + 2
            time.sleep(2)
            await ctx.channel.purge(limit=int(Limit))
            #if Limit == 3:
                #print('Eine Nachricht wurde gelöscht. Glückwunsch!')
            #else:
                #print(f'{Limit - 2} Nachrichten wurden gelöscht. Glückwunsch!')
        else:
            await ctx.channel.send('Du bist nicht cool genug um diesen Befehl auszuführen. Tut mir leid :)')

    @bot.command(aliases=['roll dice'])
    async def rolldice(self, ctx, numberofrolls=1, numberofsides=6):
        await ctx.channel.send(f'Würfel einen Würfel mit {numberofsides} Seiten {numberofrolls} mal...')
        time.sleep(1)
        for i in range(int(numberofrolls)):
            await ctx.channel.send(random.randint(1, int(numberofsides)))

    @bot.command()
    async def dance(self, ctx):
        dance = open("gifs.txt", "r")
        dance = dance.readlines()
        dance = random.choice(dance)
        await ctx.channel.send(dance)

    @bot.command()
    async def witz(self, ctx):
        zahl = random.randint(1 , 100)
        if zahl == 1:
            await ctx.channel.send("Du bist so hässlich, dass man dich nicht mal mit einem Taschenrechner vergleichen kann. Kein Witz. Einfach die Wahrheit.")
        else:
            witze = open("witze.txt", "r")
            witze = witze.readlines()
            witze = random.choice(witze)
            witze = str(witze)
            await ctx.channel.send(witze)

    @bot.command()
    async def qrcodepls (self, ctx):
        await qrcode_handler.qrcode(ctx, self)
    #TODO: Fix the qrcode handler

    #Todo: Fix the voice handler
    '''
    
    @bot.command()
    if ctx.content == '!!recordpls' or ctx.content =='!!stoppls' or ctx.content == '!!disconnectpls':
        await voice_handler.record_voice(bot, ctx)
    '''

    @bot.command()
    async def details(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(f"```"
                                                 f"Halli Hallo 💕\n"
                                                 f"Hier sind ein paar Details zu dem Channel :) \n"
                                                 f"Channel: {ctx.channel}\n"
                                                 f"Channel ID: {ctx.channel.id}\n"
                                                 f"Channel Name: {ctx.channel.name}\n"
                                                 f"Channel Type: {ctx.channel.type}\n"
                                                 f"Channel Category: {ctx.channel.category}\n"
                                                 f"Channel Category ID: {ctx.channel.category_id}\n"
                                                 f"Channel Category Name: {ctx.channel.category.name}\n"
                                                 f"Channel Category Type: {ctx.channel.category.type}\n"
                                                 f"Channel Category Position: {ctx.channel.category.position}\n"
                                                 f"```")
        else:
            pass

    @bot.command()
    async def details2(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(f"```"
                                                 f"Halli Hallo 💕\n"
                                                 f"Hier sind ein paar Details zu dem Server :) \n"
                                                 f"Server: {ctx.guild}\n"
                                                 f"Server ID: {ctx.guild.id}\n"
                                                 f"Server Name: {ctx.guild.name}\n"
                                                 f"Server Owner: {ctx.guild.owner}\n"
                                                 f"Server Owner ID: {ctx.guild.owner_id}\n"
                                                 f"Server Icon: {ctx.guild.icon}\n"
                                                 f"Server Splash: {ctx.guild.splash}\n"
                                                 f"Server Banner: {ctx.guild.banner}\n"
                                                 f"Server Discovery Splash: {ctx.guild.discovery_splash}\n"
                                                 f"Server Description: {ctx.guild.description}\n"
                                                 f"Server Features: {ctx.guild.features}\n"
                                                 f"```")
        else:
            pass


    @bot.hybrid_command()
    async def higherlower(self, ctx):
        view = HL_Buttons()

        number = random.randint(1, 100)
        number2 = random.randint(1, 100)
        hlembed = discord.Embed(title="**Higher or Lower?**", color=0xff00ff)
        hlembed.add_field(name=f"Ist die nächste Zahl **größer** oder **kleiner** als {number}? \n"
                               f"du hast 10 Sekunden Zeit! ⏱" , value=" " , inline=False)
        hlembed.set_footer(text="Schaffste eh nicht :D")
        message = await ctx.channel.send(embed=hlembed, view=view)

        await view.wait()
        hlembed.clear_fields()
        if view.value == None:
            hlembed.add_field(name="Du hast zu lang gebraucht! Du hast verloren!", value=" ", inline=False)
        elif view.value == "größer" and number2 > number:
            hlembed.add_field(name="Du hast gewonnen!", value="Die Zahl war {}".format(number2), inline=False)
        elif view.value == "kleiner" and number2 < number:
            hlembed.add_field(name="Du hast gewonnen!", value="Die Zahl war {}".format(number2), inline=False)
        else:
            hlembed.add_field(name="Du hast verloren!", value="{} ist nicht {} als {}".format(number2,view.value,number), inline=False)


        # comparen dann embed neu setzen
        await message.edit(embed=hlembed, view=view) #anschließend ausführen










    @bot.command()
    async def kiss(self, ctx, name: discord.Member = None):
        try:
            backup = name
            name = name.nick
            if name == None:
                name = backup

            kisser = ctx.author.nick
            if kisser == None:
                kisser = ctx.author.name

            file = open("kiss.txt", "r")
            embedVar = discord.Embed(title="😘 Kiss", color=0xff00ff)
            embedVar.add_field(name=f"**{name}**!" f" Du wirst von **{kisser}** geküsst!", value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.channel.send(embed=embedVar)
            file.close()
        except IndexError:
            file = open("kiss.txt", "r")
            embedVar = discord.Embed(title="😘 Kiss", color=0xff00ff)
            embedVar.add_field(name=f"**{ctx.author.nick}**! " 'küsst jeden!', value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.channel.send(embed=embedVar)
            file.close()

    @bot.command()
    async def hug(self, ctx, name: discord.Member = None):
        try:
            backup = name
            name = name.nick
            if name == None:
                name = backup

            hugger = ctx.author.nick
            if hugger == None:
                hugger = ctx.author.name

            file = open("hug.txt", "r")
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{name}**! " 'Du wirst von ' f"**{hugger}** umarmt!", value="",
                               inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.channel.send(embed=embedVar)
            file.close()

        except IndexError:
            file = open("hug.txt", "r")
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{ctx.author.nick}** umarmt jeden!", value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.channel.send(embed=embedVar)
            file.close()

    @bot.command()
    async def hit(self, ctx, name: discord.Member = None):
        try:
            backup = name
            name = name.nick
            if name == None:
                name = backup

            hitter = ctx.author.nick
            if hitter == None:
                hitter = ctx.author.name

            file = open("hit.txt", "r")
            embedVar = discord.Embed(title="😠 Hit!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{name}**! " 'Du wirst von **' + f"{hitter}** geschlagen!", value="",
                               inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.channel.send(embed=embedVar)
            file.close()
        except IndexError:
            file = open("hit.txt", "r")
            embedVar = discord.Embed(title="😠 Hit!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{ctx.author.nick}**! " 'schlägt jeden!', value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.channel.send(embed=embedVar)
            file.close()

    @bot.command(aliases=['Wetter','heute'])
    async def wetter(self, ctx, *, content=None):
        if content == None:
            await ctx.channel.send("Bitte gib einen Ort an!")
        else:
            await weather_handler.get_weather(content, ctx)
    @bot.command(aliases=['Morgen'])
    async def morgen(self, ctx, *, content=None):
        if content == None:
            await ctx.channel.send("Bitte gib einen Ort an!")
        else:
            await weather_handler.get_weather_forecast(content, ctx)
    @bot.command(aliases=['Alarm'])
    async def alarm(self, ctx, *, content = None):
        if content == None:
            await ctx.channel.send("Bitte gib einen Ort an!")
        else:
            await weather_handler.get_weather_alert(content, ctx)

    @bot.command()
    async def pingr(self, ctx):
        await ctx.channel.send('Pong! {0}'.format(round(bot.latency, 1)))