# Import Libraries
import os
import random
import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv

# Load ENV
load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))
GUILD = str(os.getenv('DISCORD_GUILD'))

# Initialize Bot and Denote The Command Prefix
intents = discord.Intents().all()
client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	
	if message.author == client.user:
		return

	await message.channel.send('Yo')

#    if message.content == '99!':


client.run(TOKEN)