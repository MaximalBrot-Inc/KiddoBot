import discord
from discord.ext import commands
from discord.ui import Button, View

class HelpCommand(commands.DefaultHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()

        select = discord.ui.Select(placeholder="Wähle eine Kategorie", options=[discord.SelectOption(label="Fun", value="Fun"),
                                                                    discord.SelectOption(label="Spiele", value="Spiele"),
                                                                    discord.SelectOption(label="Musik", value="Musik"),
                                                                    discord.SelectOption(label="Moderation", value="Moderation"),
                                                                    discord.SelectOption(label="Wetter", value="Wetter"),
                                                                    discord.SelectOption(label="Sonstiges", value="Sonstiges")])


        async def select_callback(interaction):
            match select.values[0]:
                case "Fun":
                    embedVar = discord.Embed(title="Hier sind alle Fun Commands:", color=0xff00ff)
                    embedVar.set_thumbnail(url="https://media.tenor.com/QtKRO6woYGMAAAAC/dance-emoji.gif")
                    embedVar.add_field(name="/hallo", value="Kiddo sagt Hallo", inline=False)
                    embedVar.add_field(name="/dance", value="Kiddo tanzt", inline=False)
                    embedVar.add_field(name="/hug", value="Gibt dir die Möglichkeit jemanden zu umarmen", inline=False)
                    embedVar.add_field(name="/kiss", value="Gibt dir die Möglichkeit jemanden zu küssen", inline=False)
                    embedVar.add_field(name="/hit", value="Gibt dir die Möglichkeit jemanden zu schlagen", inline=False)
                    embedVar.add_field(name="/witz", value="Kiddo erzählt dir einen Witz", inline=False)

                    await interaction.response.edit_message(embed=embedVar)
                case "Spiele":
                    embedVar = discord.Embed(title="Hier sind alle Spiele Commands:", color=0xff00ff)
                    embedVar.set_thumbnail(url="https://media.tenor.com/QWyWIOqKRNYAAAAC/cat-playing-games.gif")
                    embedVar.add_field(name="/roll_dice", value="Würfelt eine Zahl", inline=False)
                    embedVar.add_field(name="/higherlower", value="Kiddo spielt mit dir Higher Lower", inline=False)

                    await interaction.response.edit_message(embed=embedVar)
                case "Musik":
                    embedVar = discord.Embed(title="Hier sind alle Musik Commands:", color=0xff00ff)
                    embedVar.set_thumbnail(url="https://media.tenor.com/Yg9cr-N09a4AAAAC/music.gif")

                    await interaction.response.edit_message(embed=embedVar)
                case "Moderation":
                    embedVar = discord.Embed(title="Hier sind alle Moderations Commands:", color=0xff00ff)
                    embedVar.set_thumbnail(url="https://media.tenor.com/W56Ik4e1Cb0AAAAC/gumball-discord-mod.gif")
                    embedVar.add_field(name="/details", value="Zeigt dir die Konfigurationen des Channels", inline=True)
                    embedVar.add_field(name="/details2", value="Zeigt dir die Konfigurationen des Servers", inline=False)
                    embedVar.add_field(name="/ABFAHRT", value="KIDDO FÄHRT DAVON!!", inline=False)
                    embedVar.add_field(name="/loesche", value="Löscht eine bestimmte Anzahl an Nachrichten", inline=False)
                    embedVar.add_field(name="/setup", value="Macht Kiddo einsatzbereit", inline=False)
                    embedVar.add_field(name="/switchpls", value="Legt den Schalter um", inline=False)

                    await interaction.response.edit_message(embed=embedVar)
                case "Wetter":
                    embedVar = discord.Embed(title="Hier sind alle Wetter Commands:", color=0xff00ff)
                    embedVar.set_thumbnail(url="https://media.tenor.com/EDNfprqR2oMAAAAC/clouds-raining.gif")
                    embedVar.add_field(name="/wetter", value="Zeigt dir das Wetter in einer bestimmten Stadt", inline=False)
                    embedVar.add_field(name="/morgen", value="Zeigt dir das Wetter in einer bestimmten Stadt für morgen", inline=False)
                    embedVar.add_field(name="/alarm", value="Überprüft ob es in einer bestimmten Stadt eine Wetterwarnung gibt", inline=False)

                    await interaction.response.edit_message(embed=embedVar)
                case "Sonstiges":
                    embedVar = discord.Embed(title="Hier sind alle Sonstige Commands:", color=0xff00ff)
                    embedVar.set_thumbnail(url="https://media.tenor.com/Pb1TfZhr-OQAAAAC/spy-x-family-anya.gif")
                    embedVar.add_field(name="/hilfe", value="Zeigt dir alle Commands", inline=False)
                    embedVar.add_field(name="/qrcodepls", value="Kiddo erstellt dir einen QR-Code", inline=False)
                    embedVar.add_field(name="/pingr", value="Misst die Zeit welche Kiddo braucht um zu reagieren", inline=False)
                    embedVar.add_field(name="/sync", value="Synchronisiert Kiddos Erinnerungen", inline=False)
                    embedVar.add_field(name="/shorten", value="Kiddo kürzt dir einen Link", inline=False)
                    embedVar.add_field(name="/Geburtstag", value="Kiddo hat vielleicht eine Geburtstagsüberraschung für dich vorbereiter", inline=False)

                    await interaction.response.edit_message(embed=embedVar)

        select.callback = select_callback

        view = View()
        view.add_item(select)

        embedVar = discord.Embed(title="Hier sind alle Commands:", color=0xff00ff)
        embedVar.add_field(name="Wähle einfach unten eine Kategorie aus und Kiddo zeigt dir gerne die dazugehörigen Commands an", value="", inline=False)
        
        await destination.send(embed=embedVar, view=view)




