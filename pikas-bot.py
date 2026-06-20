import discord
import os
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()

GUILD = discord.Object(id=int(os.environ["GUILD_ID"]))

class Client(discord.Client):

    def __init__(self, *, intents: discord.Intents) -> None:
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

intents: discord.Intents = discord.Intents.default()
bot = Client(intents=intents)

@bot.tree.command(name="lord", description="Sends you.")
async def lord(interaction: discord.Interaction) -> None:
    """lord"""
    await interaction.response.send_message(
        "https://tenor.com/view/drooling-cat-drooling-cats-meme-memes-sandboxels-gif-7447896350206191042"
    )

@bot.tree.command(name="everyone", description="pings everyone")
async def everyone(interaction: discord.Interaction) -> None:
    """everyone"""
    await interaction.response.send_message("@everyone")

bot.run(os.environ["TOKEN"])
