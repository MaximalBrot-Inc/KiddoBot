from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError
import discord



config_dict = get_default_config()
config_dict['language'] = 'de'
owm = OWM('18bca685e2b3a0f410b5f71a66a8a621', config_dict)
mgr = owm.weather_manager()
mgg = owm.geocoding_manager()
#observation = mgr.weather_at_place('Paris, FR')

def decoder(message):
    ruckgabe = []
    ort = message.content.split(' ')[1:]
    ort = ' '.join(ort)
    list_of_locations = mgg.geocode(ort)
    gps = list_of_locations[0]
    ruckgabe.append(ort)
    ruckgabe.append(gps.lon)
    ruckgabe.append(gps.lat)
    return ruckgabe

def emoji_lookup (status):
    match status:
        case 'Clear':
            emoji = '☀️'
        case 'Clouds':
            emoji = '☁️'
        case 'Rain':
            emoji = '☔'
        case 'Snow':
            emoji = '❄️'
        case 'Thunderstorm':
            emoji = '⛈️'
        case 'Drizzle':
            emoji = '🌧️'
        case 'Mist':
            emoji = '🌫️'
        case 'Smoke':
            emoji = '🔥'
        case 'Haze':
            emoji = '😶‍🌫️'
        case 'Dust':
            emoji = '🌫️'
        case 'Fog':
            emoji = '🌁'
        case 'Sand':
            emoji = '🌫️'
        case 'Ash':
            emoji = '🌋'
        case 'Squall':
            emoji = '💨'
        case 'Tornado':
            emoji = '🌪️'
        case _ :
            emoji = '??'
    return emoji



async def get_weather(message):
    ort = decoder(message)

    try:
        observation = mgr.weather_at_place(ort[0])
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        daten = w.detailed_status
        daten_einfach = w.status
        emoji = emoji_lookup (daten_einfach)

        if (temp <= 0):
            color = 0x34c0eb
        elif (temp >= 30):
            color = 0xeb8334
        else:
            color = 0x36a822

        embedVar = discord.Embed(title="**Wetterbericht**", color=color)
        embedVar.add_field(name="**Wetter**", value=f'In {ort[0]} ist es gerade {daten} {emoji}', inline=False)
        embedVar.add_field(name="**Temperatur**", value=f'In {ort[0]} hat es gerade {temp}°C 🌡', inline=False)

        await message.channel.send(embed=embedVar)
    except NotFoundError:
        await message.channel.send(f'Ich konnte {ort[0]} nicht finden :(')
    except IndexError:
        await message.channel.send('Bitte gib einen Ort an :)')
    except:
         await message.channel.send('Es ist ein Fehler aufgetreten :(')


async def get_weather_forecast(message):
    ort = decoder(message)
    try:
        one_call = mgr.one_call(lon=ort[1], lat=ort[2])
        w = one_call.forecast_daily
        temp = w[0].temperature('celsius')
        daten = w[0].detailed_status
        daten_einfach = w[0].status
        emoji = emoji_lookup (daten_einfach)
        if (temp["min"] <= 0):
            color = 0x34c0eb
        elif (temp["max"] >= 30):
            color = 0xeb8334
        else:
            color = 0x36a822


        embedVar = discord.Embed(title="**Wettervorschau**", color=color)
        embedVar.add_field(name="**Wetter**", value=f'In {ort[0]} gibt es morgen {daten} {emoji}', inline=False)
        embedVar.add_field(name="**Temperatur**", value=f'In {ort[0]} hat es morgen maximal {temp["max"]}°C 🌡'
                                                        f'und minimal {temp["min"]}🌡', inline=False)

        await message.channel.send(embed=embedVar)


    except NotFoundError:
        await message.channel.send(f'Ich konnte {ort[0]} nicht finden :(')
    except IndexError:
        await message.channel.send('Bitte gib einen Ort an :)')
    except:
        await message.channel.send('Es ist ein Fehler aufgetreten :(')

async def get_weather_alert(message):
    try:
        ort = decoder(message)

        one_call = mgr.one_call(lon=ort[1], lat=ort[2])
        w = one_call.national_weather_alerts
        daten = w[0].description
        embedVar = discord.Embed(title="**Wetterwarnung**", color=0xff0000)
        embedVar.add_field(name="**Warnung**", value=f'In {ort[0]} gibt es eine Wetterwarnung: {daten}', inline=False)
        await message.channel.send(embed=embedVar)
    except NotFoundError:
        await message.channel.send(f'Ich konnte {ort[0]} nicht finden :(')
    except AssertionError:
        await message.channel.send('Bitte gib einen Ort an :)')
    except:
        await message.channel.send('Es ist ein Fehler aufgetreten :(')

