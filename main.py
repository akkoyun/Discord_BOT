# Import Libraries
from config.Config import APP_Settings
import discord
from dotenv import load_dotenv

# Load ENV
TOKEN = APP_Settings.DISCORD_TOKEN

# Initialize Bot and Denote The Command Prefix
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
