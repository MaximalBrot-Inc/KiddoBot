import time
import discord
from discord.ext import commands


async def qrcode(ctx, self):

    bot = commands.AutoShardedBot(commands.when_mentioned_or('!!'), intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    await ctx.author.create_dm()
    await ctx.author.dm_channel.send('Du willst also einen QR-Code? Dann brauch ich als erstes einen Link. Schreib mir einfach den Link in die DMs und ich erstelle dir einen QR-Code :)')

    def check(m):
        return m.author == message.author and m.channel == ctx.author.dm_channel

    self.bot.wait_for('message', check=check)

    if ctx.startswith ('https://') or ctx.startswith('http://') or ctx.startswith('www.'):
        await ctx.author.dm_channel.send('Okay, ich erstelle dir jetzt einen QR-Code für ' + msg.content + ' :)')
        time.sleep(3)
        await ctx.author.dm_channel.send('Hier ist dein QR-Code :)')
        await ctx.author.dm_channel.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + msg.content)
        await ctx.author.dm_channel.send('Willst du noch einen QR-Code? Dann schreib mir einfach "y" (Du hast 60 Sekunden Zeit ⏱ )  :)')
        self.bot.wait_for('y', timeout=60, check=check)

        try:
            if ctx.content == 'y':
                await qrcode(message, bot)
        except asyncio.exceptions.TimeoutError:
            await ctx.author.dm_channel.send(
                'Du hast zu lange gebraucht. Schreibe den Befehl wieder, wenn du noch einen Code erstellen willst :)')
            return

    else:
        try:
            'https://' + ctx.content
            await message.author.dm_channel.send('Okay, ich erstelle dir jetzt einen QR-Code für ' + msg.content + ' :)')
            time.sleep(3)
            await ctx.author.dm_channel.send('Hier ist dein QR-Code :)')
            await ctx.author.dm_channel.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + ctx.content)

        except:
            await ctx.author.dm_channel.send('Das ist kein Link. Versuche es nochmal :)')
            await qrcode(message , bot)

        await ctx.author.dm_channel.send('Willst du noch einen QR-Code? Dann schreib mir einfach "y" (Du hast 60 Sekunden Zeit ⏱ )  :)')
        msg = self.bot.wait_for('y', timeout=60, check=check)
        try:
            if msg.content == 'y':
                await qrcode(ctx, bot)
        except asyncio.exceptions.TimeoutError:
            await ctx.author.dm_channel.send('Du hast zu lange gebraucht. Schreibe den Befehl wieder, wenn du noch einen Code erstellen willst :)')
            return
