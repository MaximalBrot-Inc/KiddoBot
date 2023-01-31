import random
import time

async def leon(message):
    if "leon" or "Leon" in message.content:
        await message.channel.send('Ab ins Timeout mit dir :)')

async def mods(message):
    if "mods" in message.content:
        mods = 100
        while mods > 0:
            await message.author.create_dm()
            await message.author.send('https://tenor.com/view/mrbeast-mr-beast-gif-25629645')
            time.sleep(0.5)
            await message.author.send(
            'https://tenor.com/view/dont-do-not-do-not-cat-dangerous-individual-man-dancing-while-cat-threatens-your-family-gif-26522356')
            mods = mods - 1

async def berat(message):
    if "berat" or "Berat" in message.content:
        berat = open("berat.txt", "r")
        berat = berat.readlines()
        berat = random.choice(berat)
        await message.channel.send(berat)