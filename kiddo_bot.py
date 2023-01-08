'''
a friendly Discord bot
Maximilian
08.01.2023
'''

from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.',intents=intents)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run('TOKEN')