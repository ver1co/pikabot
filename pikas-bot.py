import discord
from discord import app_commands

Guild = discord.Object(id=1517412425966813205)

class Client (discord.Client):

    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=Guild)
        await self.tree.sync(guild=Guild)

    async def on_ready (self):
        print(f"Logged in as {self.user}")

intents = discord.Intents.default()
bot = Client(intents=intents)

@bot.tree.command(name="lord", description="Sends you.")
async def lord (interaction: discord.Interaction):
    """lord"""
    await interaction.response.send_message(f'https://tenor.com/view/drooling-cat-drooling-cats-meme-memes-sandboxels-gif-7447896350206191042')

@bot.tree.command(name="everyone", description="pings everyone")
async def everyone (interaction: discord.Interaction):
    """everyone"""
    await interaction.response.send_message(f'@everyone')
