import random
import time

async def main_handler(message):
    if message.content == 'leon' or message.content == 'Leon':
        await message.channel.send('Ab ins Timeout mit dir :)')


    elif message.content == 'mod' or message.content == 'Mod':
        mods = 100
        while mods > 0:
            await message.author.create_dm()
            await message.author.send('https://tenor.com/view/mrbeast-mr-beast-gif-25629645')
            time.sleep(0.5)
            await message.author.send(
                'https://tenor.com/view/dont-do-not-do-not-cat-dangerous-individual-man-dancing-while-cat-threatens-your-family-gif-26522356')
            mods = mods - 1


    elif message.content == 'berat' or message.content == 'Berat':
        berat = open("berat.txt", "r")
        berat = berat.readlines()
        berat = random.choice(berat)
        await message.channel.send(berat)

    elif message.content == 'ping':
        await message.channel.send('pong')
