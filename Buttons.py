import discord
from discord.ext import commands
from discord import app_commands
from discord import ui




class HL_Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Größer", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.button):

        for button in self.children:
            button.disabled = True
        await interaction.response.edit_message(view=self)

        self.value = "größer"
        self.stop()


    @discord.ui.button(label="Kleiner", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        for button in self.children:
            button.disabled = True
        await interaction.response.edit_message(view=self)


        self.value = "kleiner"
        self.stop()

class Setup_Button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="👍", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.button):
        for button in self.children:
            button.disabled = True
        await interaction.response.edit_message(view=self)

        self.value = "thumbsup"
        self.stop()

    @discord.ui.button(label="👎", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        for button in self.children:
            button.disabled = True
        await interaction.response.edit_message(view=self)

        self.value = "thumbsdown"
        self.stop()

class Switch_Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="An", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.button):
        for button in self.children:
            button.disabled = True
        await interaction.response.edit_message(view=self)

        self.value = "on"
        self.stop()

    @discord.ui.button(label="Aus", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        for button in self.children:
            button.disabled = True
        await interaction.response.edit_message(view=self)

        self.value = "off"
        self.stop()





