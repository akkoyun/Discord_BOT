# Import Libraries
from config import Schema, log_functions
from config.Config import APP_Settings
from kafka import KafkaConsumer, KafkaProducer
from json import dumps
import json

# Discord Libraries
import discord
from discord.ext import commands
TOKEN = APP_Settings.DISCORD_TOKEN

# Initialize Bot and Denote The Command Prefix
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')



# Kafka Consumer
Kafka_RAW_Consumer = KafkaConsumer('RAW.Discord', bootstrap_servers="165.227.154.147:9092", group_id="Data_Consumer", auto_offset_reset='earliest', enable_auto_commit=False)

async def Discord_Control():

	try:

		for Message in Kafka_RAW_Consumer:

			channel = client.get_channel(1051844419105607781)
			await channel.send('test')

			# handle Message.
#			Kafka_Message = Schema.IoT_Data_Pack_Model(**json.loads(Message.value.decode()))

			# Handle Headers
#			Command = Message.headers[0][1].decode('ASCII')
#			Device_ID = Message.headers[1][1].decode('ASCII')
#			Device_Time = Message.headers[2][1].decode('ASCII')
#			Device_IP = Message.headers[3][1].decode('ASCII')

			# Print LOG
#			log_functions.Log_Kafka_Header(Command, Device_ID, Device_IP, Device_Time, Message.topic, Message.partition, Message.offset)

			# Commit Message
#			Kafka_RAW_Consumer.commit()

#			print("--------------------------------------------------------------------------------")

			client.run(TOKEN)

	finally:
		
		print("Error Accured !!")


# Handle All Message in Topic
#Discord_Control()

