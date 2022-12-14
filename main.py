# Import Libraries
from config.Config import APP_Settings
import discord
from dotenv import load_dotenv

# Load ENV
TOKEN = APP_Settings.DISCORD_TOKEN
GUILD = APP_Settings.DISCORD_GUILD


# Initialize Bot and Denote The Command Prefix
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)
