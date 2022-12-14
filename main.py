# Import Libraries
import os
import discord
from dotenv import load_dotenv

# Load ENV
load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))
GUILD = str(os.getenv('DISCORD_GUILD'))

# Initialize Bot and Denote The Command Prefix
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

client.run(TOKEN)
