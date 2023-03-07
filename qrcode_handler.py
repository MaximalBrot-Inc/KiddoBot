import time

async def qrcode(message , bot):
    await message.author.create_dm()
    await message.author.dm_channel.send('Du willst also einen QR-Code? Dann brauch ich als erstes einen Link. Schreib mir einfach den Link in die DMs und ich erstelle dir einen QR-Code :)')
    def check(m):
        return m.author == message.author and m.channel == message.author.dm_channel
    msg = await bot.wait_for('message', check=check)
    if msg.content.startswith ('https://') or msg.content.startswith('http://') or msg.content.startswith('www.'):
        await message.author.dm_channel.send('Okay, ich erstelle dir jetzt einen QR-Code für ' + msg.content + ' :)')
        time.sleep(3)
        await message.author.dm_channel.send('Hier ist dein QR-Code :)')
        await message.author.dm_channel.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + msg.content)
        await message.author.dm_channel.send('Willst du noch einen QR-Code? Dann schreib mir einfach "y" (Du hast 60 Sekunden Zeit ⏱ )  :)')
        msg = await bot.wait_for('y', timeout=60, check=check)
        try:
            if msg.content == 'y':
                await qrcode(message, bot)
        except asyncio.exceptions.TimeoutError:
            await message.author.dm_channel.send(
                'Du hast zu lange gebraucht. Schreibe den Befehl wieder, wenn du noch einen Code erstellen willst :)')
            return

    else:
        try:
            'https://' + msg.content
            await message.author.dm_channel.send('Okay, ich erstelle dir jetzt einen QR-Code für ' + msg.content + ' :)')
            time.sleep(3)
            await message.author.dm_channel.send('Hier ist dein QR-Code :)')
            await message.author.dm_channel.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + msg.content)

        except:
            await message.author.dm_channel.send('Das ist kein Link. Versuche es nochmal :)')
            await qrcode(message , bot)

        await message.author.dm_channel.send('Willst du noch einen QR-Code? Dann schreib mir einfach "y" (Du hast 60 Sekunden Zeit ⏱ )  :)')
        msg = await bot.wait_for('y', timeout=60, check=check)
        try:
            if msg.content == 'y':
                await qrcode(message, bot)
        except asyncio.exceptions.TimeoutError:
            await message.author.dm_channel.send('Du hast zu lange gebraucht. Schreibe den Befehl wieder, wenn du noch einen Code erstellen willst :)')
            return