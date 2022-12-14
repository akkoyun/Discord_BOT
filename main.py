# Import Libraries
import os
import random
import discord
from dotenv import load_dotenv

# Load ENV
load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))
GUILD = str(os.getenv('DISCORD_GUILD'))

# Initialize Bot and Denote The Command Prefix
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	
	if message.author == client.user:
		return

	if message.content == 'STF':
		
		await message.channel.send('Yo')



client.run(TOKEN)