import discord
import random
import time
import geburtstag_handler
from discord.ext import commands

bot = commands.Bot(command_prefix = '!!' , intents = discord.Intents.all())


async def main_handler(message , bot):
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

#@bot.event
#async def on_voice_state_update(member, before, after):

#    global role
 #   if member.nick == None:
  #      channel = await after.channel.clone(name=f"{member.name}'s channel")
   # else:
    #    channel = await after.channel.clone(name=f"{member.nick}'s channel")

#    await member.move_to(channel)
 #   if len(after.channel.members) == 1:
  #      role = await after.channel.guild.create_role(name=f'{after.channel.name} owner', color=discord.Color(633573),
   #                                                 reason='Channel owner')
    #    await after.channel.set_permissions(role, overwrite=discord.PermissionOverwrite(manage_channels=True, connect=True,
     #                                                                                   speak=True, stream=True,
      #                                                                                  view_channel=True))
       # await member.add_roles(role)

#    if str(before.channel) != '➕ Erstelle Channel' and str(before.channel) != 'None' and str(before.channel) != '🎵 Musik':
 #       if before.channel.category.name == '⋙ 🎤 Voice Channels ⋘' or '🎤 Voice Channels':
  #          if len(before.channel.members) == 0:
   #             await member.remove_roles(role)
    #            await before.channel.delete()
     #           await role.delete()

    @bot.event
    async def on_message(message):
        #####MEGA GEBURTSTAG EVENT AAAAAAAAAAAAAAAAAAAAAAAAAAAA#############################################################
        if message.content == 'Geburtstag!':
            if message.author != bot.user:
                await geburtstag_handler.geburtstag(message, bot)


        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == '!!help':
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
                embedVar.add_field(name = f"**{kiss}**!" f" Du wirst von **{kisser}** geküsst!" , value = "" , inline=False)
                embedVar.set_image(url = str(random.choice(file.readlines())))
                await message.channel.send(embed=embedVar)
                file.close()
            except IndexError:
                file = open("kiss.txt" , "r")
                embedVar = discord.Embed(title="😘 Kiss", color=0xff00ff)
                embedVar.add_field(name = f"**{message.author.nick}**! " 'küsst jeden!' , value = "" , inline=False)
                embedVar.set_image(url = str(random.choice(file.readlines())))
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
                embedVar.add_field(name = '**' + f"{message.author.nick}** umarmt jeden!" , value="" , inline=False)
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
                embedVar.add_field(name='**' + f"{hit}**! " 'Du wirst von **' + f"{hitter}** geschlagen!" , value = "" , inline=False)
                embedVar.set_image(url = str(random.choice(file.readlines())))
                await message.channel.send(embed=embedVar)
                file.close()
            except IndexError:
                file = open("hit.txt" , "r")
                embedVar = discord.Embed(title="😠 Hit!", color=0xff00ff)
                embedVar.add_field(name='**' + f"{message.author.nick}**! " 'schlägt jeden!' , value = "" , inline=False)
                embedVar.set_image(url = str(random.choice(file.readlines())))
                await message.channel.send(embed=embedVar)
                file.close()