import music
import BHEL

import discord
from discord.ext import commands
import random
import time


bot = commands.Bot(command_prefix = '-' , description = 'KiddoBot' , intents = discord.Intents.all())
bot.remove_command('help')

async def main_handler(message , client):

    def Schalter():
        readline = open("switch.txt", "r")
        switch_state = readline.read()
        switch = "error"
        if switch_state == 'True':
            switch = "an"
        if switch_state == 'False':
            switch = "aus"
        return switch

    @bot.command(name = 'switchstate' , help = 'Zeigt den Status des Schalters an' , aliases = ['switchstate'])
    async def switchstate(ctx):
        switch = Schalter()
        await ctx.send(f'Der Schalter ist {switch}')

    @bot.command(name = 'switchpls' , help = 'Schaltet den Schalter um (nur wenn du cool bist)')
    async def switch(ctx):
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

    @bot.command(name = 'ping' , help = 'pong')
    async def ping(ctx):
        await ctx.send('pong')

    @bot.command(name = 'rolldice' , help = 'Würfelt eine Zahl zwischen 1 und 6')
    async def roll(ctx, number_of_dice, number_of_sides):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    @bot.command(name = '8ball' , help = 'Stellt eine Frage und der Bot gibt dir eine Antwort')
    async def eight_ball(ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don\'t count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @bot.command(name = 'lösche' , help = 'Löscht eine bestimmte Anzahl an Nachrichten')
    async def clear(ctx, Limit):
        if message.author.gild_permissions.manage_messages:
            Limit = message.content.spit(' ')[1]
            Limit = int(Limit)
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
            await message.channel.send('Du bist nicht cool genug um Nachrichten zu löschen :)')

    @bot.command(name = 'ban' , help = 'Bannt einen User')
    async def ban(ctx, member : discord.Member, *, reason=None):
        reason = 'Tschüssi :)'
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @bot.command(name = 'kick' , help = 'Kickt einen User')
    async def kick(ctx, member : discord.Member, *, reason=None):
        reason = 'Tschüssi :)'
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @bot.command(name = 'Baustelle' , help = 'Bannt alle User')
    async def banall(ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            for member in ctx.guild.members:
                await member.ban()
                await ctx.send(f'Banned {member.mention}')
        else:
            await ctx.send('Du bist kein Bauarbeiter :)')

    @bot.command(name = 'changenickto' , help = 'Ändert den Nickname aller User')
    async def changenickto(ctx, *, reason=None):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.send(f'Changing nicknames...')
            for member in ctx.guild.members:
                await member.edit(nick=reason)
                await ctx.send(f'Changed nickname of {member.mention} to {reason}')
            await ctx.send('Fertig :)')
        else:
            pass

    @bot.command(name = 'dance' , help = 'Kiddo tanzt alleine oder mit seinen Freunden')
    async def dance(ctx):
        dance = open("gifs.txt", "r")
        dance = dance.readlines()
        dance = random.choice(dance)
        await ctx.send(dance)

    @bot.command(name = 'L' , help = 'L')
    async def L(ctx):
        await ctx.send('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL' ,
                       tts = True)

    @bot.command(name = 'details' , help = 'Zeigt dir die Konfigurationen des Channels')
    async def details(ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.send(f"```"
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
                        f"Channel Category Position: {xtc.channel.category.position}\n"
                        f"TTS is {ctx.tts}\n"
                        f"```")
        else:
            pass

    @bot.command(name = 'details2' , help = 'Zeigt dir die Konfigurationen des Servers')
    async def details2(ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.send(f"```"
                       f"Halli Hallo 💕\n"
                        f"Hier sind ein paar Details zu dem Server :) \n"
                        f"Server: {ctx.guild}\n"
                        f"Server ID: {ctx.guild.id}\n"
                        f"Server Name: {ctx.guild.name}\n"
                        f"Server Type: {ctx.guild.type}\n"
                        f"Server Region: {ctx.guild.region}\n"
                        f"Server Owner: {ctx.guild.owner}\n"
                        f"Server Owner ID: {ctx.guild.owner_id}\n"
                        f"Server Icon: {ctx.guild.icon}\n"
                        f"Server Icon URL: {ctx.guild.icon_url}\n"
                        f"Server Icon URL As Static: {ctx.guild.icon_url_as(static_format='png')}\n"
                        f"Server Icon URL As Static 1024: {ctx.guild.icon_url_as(static_format='png', size=1024)}\n"
                        f"Server Splash: {ctx.guild.splash}\n"
                        f"Server Splash URL: {ctx.guild.splash_url}\n"
                        f"Server Splash URL As Static: {ctx.guild.splash_url_as(static_format='png')}\n"
                        f"Server Splash URL As Static 1024: {ctx.guild.splash_url_as(static_format='png', size=1024)}\n"
                        f"Server Banner: {ctx.guild.banner}\n"
                        f"Server Banner URL: {ctx.guild.banner_url}\n"
                        f"Server Banner URL As Static: {ctx.guild.banner_url_as(static_format='png')}\n"
                        f"Server Banner URL As Static 1024: {ctx.guild.banner_url_as(static_format='png', size=1024)}\n"
                        f"Server Discovery Splash: {ctx.guild.discovery_splash}\n"
                        f"Server Discovery Splash URL: {ctx.guild.discovery_splash_url}\n"
                        f"Server Discovery Splash URL As Static: {ctx.guild.discovery_splash_url_as(static_format='png')}\n"
                        f"Server Discovery Splash URL As Static 1024: {ctx.guild.discovery_splash_url_as(static_format='png', size=1024)}\n"
                        f"Server Description: {ctx.guild.description}\n"
                        f"Server Features: {ctx.guild.features}\n")
        else:
            pass

    @bot.command(name = 'ABFAHRT' , help = 'KIDDO FÄHRT DAVON!!')
    async def ABFAHRT(ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            await ctx.send("ABFAHRT!!!" , file=discord.File("C:\_FSST\Jaeger\Shooting Range\KiddoBot\ABFAHRT.PNG"))
            time.sleep(8)
            for channel in ctx.guild.channels:
                await channel.delete(reason='MFG KiddoBot :)')
            for role in ctx.guild.roles:
                await role.delete(reason='MFG KiddoBot :)')
            for member in ctx.guild.members:
                await member.ban(reason='MFG KiddoBot :)')
            for emoji in ctx.guild.emojis:
                await emoji.delete(reason='MFG KiddoBot :)')
            for category in ctx.guild.categories:
                await category.delete(reason='MFG KiddoBot :)')
            for voice_channel in ctx.guild.voice_channels:
                await voice_channel.delete(reason='MFG KiddoBot :)')
            for stage_channel in ctx.guild.stage_channels:
                await stage_channel.delete(reason='MFG KiddoBot :)')
            for store_channel in ctx.guild.store_channels:
                await store_channel.delete(reason='MFG KiddoBot :)')
            for thread in ctx.guild.threads:
                await thread.delete(reason='MFG KiddoBot :)')

        else:
            await ctx.send('Du hast kein KlimaTicket :(')

    @bot.command(name = 'help' , help = 'Zeigt dir alle Commands')
    async def help(ctx):
        if ctx.author.id == 695885580629704734 or ctx.author.id == 408627107795828746:
            embedVar = discord.Embed(title="Hier sind alle Commands:" , color=0x546e7a)
            embedVar.add_field(name=":ping" , value="pong" , inline=False)
            embedVar.add_field(name=":roll_dice" , value="Würfelt eine Zahl" , inline=False)
            embedVar.add_field(name=":dance" , value="Kiddo tanzt" , inline=False)
            embedVar.add_field(name=":details" , value="Zeigt dir die Konfigurationen des Servers" , inline=False)
            embedVar.add_field(name=":details2" , value="Zeigt dir die Konfigurationen des Servers" , inline=False)
            embedVar.add_field(name=":ABFAHRT" , value="KIDDO FÄHRT DAVON!!" , inline=False)
            embedVar.add_field(name=":help" , value="Zeigt dir alle Commands" , inline=False)
            embedVar.add_field(name=":play" , value="Spielt einen Song ab" , inline=False)
            embedVar.add_field(name=":stop" , value="Stoppt den Song" , inline=False)
            await ctx.send(embed=embedVar)
        else:
            pass

########## Music #######################################################################################################

    @bot.command(name = 'play' , help = 'Spielt einen Song ab')
    async def play(ctx, url: str):
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        embedVar = discord.Embed(title="Ich spiele jetzt den Song:" ,
                             description=f'```{player.title}```' , color=0x546e7a)
        await ctx.send(embed=embedVar)

    @bot.command(name = 'stop' , help = 'Stoppt den Song')
    async def stop(ctx):
        await ctx.voice_client.disconnect()

    @bot.command(name = 'pause' , help = 'Pausiert den Song')
    async def pause(ctx):
        await ctx.voice_client.pause()
        await ctx.send("Song wurde pausiert :)")

    @bot.command(name = 'resume' , help = 'Spielt den Song weiter')
    async def resume(ctx):
        await ctx.voice_client.resume()
        await ctx.send("Song wird weitergespielt :)")

########## 2BHEL #######################################################################################################

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if 'leon' or 'Leon' in message.content:
            await message.channel.send('Leon ist ein Pferd')

        elif 'mods' or 'Mods' in message.content:
            mods = 100
            while mods > 0:
                await message.author.create_dm()
                await message.author.send('https://tenor.com/view/mrbeast-mr-beast-gif-25629645')
                time.sleep(0.5)
                await message.author.send(
                    'https://tenor.com/view/dont-do-not-do-not-cat-dangerous-individual-man-dancing-while-cat-threatens-your-family-gif-26522356')
                mods = mods - 1

        elif 'berat' or 'Berat' in message.content:
            berat = open("berat.txt", "r")
            berat = berat.readlines()
            berat = random.choice(berat)
            await message.channel.send(berat)
