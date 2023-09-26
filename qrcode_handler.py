import time
import discord
from discord.ext import commands


async def qrcode(ctx: commands.Context, self):

    bot = commands.AutoShardedBot(commands.when_mentioned_or('!!'), intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    await ctx.author.create_dm()
    await ctx.author.dm_channel.send('Du willst also einen QR-Code? Dann brauch ich als erstes einen Link. Schreib mir einfach den Link in die DMs und ich erstelle dir einen QR-Code :)')

    def check(message: discord.Message):
        return message.channel == ctx.channel and message.author != ctx.me


    message = await self.bot.wait_for('ctx', check=check)
    print(message)

    if message.startswith("https://"):
        print(msg.content)
        await ctx.author.dm_channel.send('Okay, ich erstelle dir jetzt einen QR-Code für ' + msg.content + ' :)')
        time.sleep(3)
        await ctx.author.dm_channel.send('Hier ist dein QR-Code :)')
        await ctx.author.dm_channel.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + msg.content)
        #await ctx.author.dm_channel.send('Willst du noch einen QR-Code? Dann schreib mir einfach "y" (Du hast 60 Sekunden Zeit ⏱ )  :)')
        #msg2 = self.bot.wait_for('y', timeout=60, check=check)

#    try:
 #       if msg2.content == 'y':
  #          await qrcode(ctx, self)
   # except asyncio.exceptions.TimeoutError:
    #    await ctx.author.dm_channel.send(
     #       'Du hast zu lange gebraucht. Schreibe den Befehl wieder, wenn du noch einen Code erstellen willst :)')
      #  return

#    else:
 #       try:
  #          'https://' + ctx.content
   #         await message.author.dm_channel.send('Okay, ich erstelle dir jetzt einen QR-Code für ' + msg.content + ' :)')
    #        time.sleep(3)
     #       await ctx.author.dm_channel.send('Hier ist dein QR-Code :)')
      #      await ctx.author.dm_channel.send('https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + ctx.content)
#
 #       except:
  #          await ctx.author.dm_channel.send('Das ist kein Link. Versuche es nochmal :)')
   #         await qrcode(message , bot)
#
 #       await ctx.author.dm_channel.send('Willst du noch einen QR-Code? Dann schreib mir einfach "y" (Du hast 60 Sekunden Zeit ⏱ )  :)')
  #      msg = self.bot.wait_for('y', timeout=60, check=check)
   #     try:
    #        if msg.content == 'y':
     #           await qrcode(ctx, bot)
      #  except asyncio.exceptions.TimeoutError:
       #     await ctx.author.dm_channel.send('Du hast zu lange gebraucht. Schreibe den Befehl wieder, wenn du noch einen Code erstellen willst :)')
        #    return
