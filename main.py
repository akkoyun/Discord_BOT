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
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '99!':
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')

@bot.command(name='Help', help='Tells the bot to join the voice channel')
async def help(message):

    if message.author == client.user:
        return

    if message.content == '99!':
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')

client.run(TOKEN)