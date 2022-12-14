# Import Libraries
import os
import random
import discord
from discord.ext import commands
from discord import Status
from dotenv import load_dotenv

# Load ENV
load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))
GUILD = str(os.getenv('DISCORD_GUILD'))

intents = discord.Intents()
intents.members = True
intents.presences = True

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix='!', intents =intents)
#client = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Exploring the archives"))
bot.loop.create_task(Status())

@bot.event
async def on_message(message):
	
	if message.author.id == 1051838176685211699:
		return

	await message.channel.send(message.content)



#client.run(TOKEN)