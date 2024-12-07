import discord
import requests
from discord.ext import commands

api_key = open("data.txt", "r").readlines()[17]
units = 'metric'
lang = 'de'


def decoder(ort):
    api_data = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?limit=5&q={ort}&appid={api_key}').json()
    return api_data[0]['lon'], api_data[0]['lat']


def emoji_lookup(status):
    emoji_list = {'Clear': '☀️', 'Clouds': '☁️', 'Rain': '☔', 'Snow': '❄️', 'Thunderstorm': '⛈️', 'Drizzle': '🌧️',
                  'Mist': '🌫️', 'Smoke': '🔥', 'Haze': '😶‍🌫️', 'Dust': '🌫️', 'Fog': '🌁', 'Sand': '🌫️', 'Ash': '🌋',
                  'Squall': '💨', 'Tornado': '🌪️'}

    if status not in emoji_list:
        return '??'
    else:
        return emoji_list[status]


class Weather(commands.Cog):

    @commands.hybrid_command(name="wetter", aliases=['Wetter', 'heute'], brief='Gibt das aktuelle Wetter aus',
                             description='Frage Kiddo nach dem Wetter :)')
    async def get_weather(self, ctx, location):
        try:
            gps = decoder(location)

            api_data = requests.get(
                f'https://api.openweathermap.org/data/3.0/onecall?lat={gps[1]}&lon={gps[0]}&exclude=current,minutely,'
                f'daily,alerts&appid={api_key}&units={units}&lang={lang}').json()

            api_data = api_data['hourly'][0]
            temp = api_data['temp']
            daten = api_data['weather'][0]['description']
            emoji = emoji_lookup(api_data['weather'][0]['main'])

            if temp <= 0:
                color = 0x34c0eb
            elif temp >= 30:
                color = 0xeb8334
            else:
                color = 0x36a822

            embedVar = discord.Embed(title="**Wetterbericht**", color=color)
            embedVar.add_field(name="**Wetter**", value=f'In {location} ist es gerade {daten} {emoji}', inline=False)
            embedVar.add_field(name="**Temperatur**", value=f'In {location} hat es gerade {temp}°C 🌡', inline=False)

            await ctx.send(embed=embedVar)
        except IndexError:
            await ctx.send('Bitte gib einen echten Ort an :)')

    @commands.hybrid_command(name="morgen", aliases=['Wettervorhersage'], brief='Gibt die Wettervorhersage aus',
                             description='Wie wird denn wohl das Wetter morgen?')
    async def get_weather_forecast(self, ctx, location):
        try:
            gps = decoder(location)

            api_data = requests.get(
                f'https://api.openweathermap.org/data/3.0/onecall?lat={gps[1]}&lon={gps[0]}&exclude=current,minutely,'
                f'&appid={api_key}&units={units}&lang={lang}').json()

            api_data = api_data['daily'][1]
            temp = api_data['temp']
            daten = api_data['weather'][0]['description']
            emoji = emoji_lookup(api_data['weather'][0]['main'])
            if temp["min"] <= 0:
                color = 0x34c0eb
            elif temp["max"] >= 30:
                color = 0xeb8334
            else:
                color = 0x36a822

            embedVar = discord.Embed(title="**Wettervorschau**", color=color)
            embedVar.add_field(name="**Wetter**", value=f'In {location} gibt es morgen {daten} {emoji}', inline=False)
            embedVar.add_field(name="**Temperatur**", value=f'In {location} hat es morgen minimal {temp["min"]}°C 🌡'
                                                            f'und maximal {temp["max"]}🌡', inline=False)

            await ctx.send(embed=embedVar)

        except IndexError:
            await ctx.send('Bitte gib einen echten Ort an :)')

    @commands.hybrid_command(name="alarm", aliases=['Wetterwarnung', 'warnung'], brief='Gibt die Wetterwarnung aus',
                             description='Frage nach, ob es in deiner Umgebung gerade eine Wetterwarnung gibt')
    async def get_weather_alert(self, ctx, location):
        try:
            gps = decoder(location)

            api_data = (requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={gps[1]}&lon={gps[0]}'
                                     'f&exclude=current,minutely,hourly,daily&appid={api_key}&units={units}'
                                     'f&lang={lang}').json())

            try:
                embedVar = discord.Embed(title="**Wetterwarnung**", color=0xff0000)
                embedVar.add_field(name="**Warnung**",
                                   value=f'In {location} gibt es eine Wetterwarnung: '
                                         f'{api_data["alerts"][0]["description"]}', inline=False)
            except KeyError:
                embedVar = discord.Embed(title="**Wetterwarnung**", color=0x36a822)
                embedVar.add_field(name="**Warnung**", value=f'In {location} gibt es keine Wetterwarnung.',
                                   inline=False)

            await ctx.send(embed=embedVar)

        except IndexError:
            await ctx.send('Bitte gib einen echten Ort an :)')
