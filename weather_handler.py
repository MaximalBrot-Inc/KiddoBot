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
    ort = message.content.split(' ')[1:]
    ort = ' '.join(ort)
    return ort

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
        observation = mgr.weather_at_place(ort)
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
        embedVar.add_field(name="**Wetter**", value=f'In {ort} ist es gerade {daten} {emoji}', inline=False)
        embedVar.add_field(name="**Temperatur**", value=f'In {ort} hat es gerade {temp}°C 🌡', inline=False)

        await message.channel.send(embed=embedVar)
    except NotFoundError:
        await message.channel.send(f'Ich konnte {ort} nicht finden :(')
    except IndexError:
        await message.channel.send('Bitte gib einen Ort an :)')
    except:
         await message.channel.send('Es ist ein Fehler aufgetreten :(')


async def get_weather_forecast(message):
    ort = decoder(message)
    try:
        list_of_locations = mgg.geocode(ort)
        gps = list_of_locations[0]  # taking the first London in the list

        one_call = mgr.one_call(lon=gps.lon, lat=gps.lat)
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


        embedVar = discord.Embed(title="**Wettervorschaut**", color=color)
        embedVar.add_field(name="**Wetter**", value=f'In {ort} gibt es morgen {daten} {emoji}', inline=False)
        embedVar.add_field(name="**Temperatur**", value=f'In {ort} hat es morgen maximal {temp["max"]}°C 🌡'
                                                        f'und minimal {temp["min"]}🌡', inline=False)

        await message.channel.send(embed=embedVar)


    except NotFoundError:
        await message.channel.send(f'Ich konnte {ort} nicht finden :(')
    except IndexError:
        await message.channel.send('Bitte gib einen Ort an :)')
    except:
        await message.channel.send('Es ist ein Fehler aufgetreten :(')