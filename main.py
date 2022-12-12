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

	channel = client.get_channel(1051844419105607781)

	# Kafka Consumer
	Kafka_Discord_Consumer = KafkaConsumer('RAW.Discord', bootstrap_servers="165.227.154.147:9092", group_id="Data_Consumer", auto_offset_reset='earliest', enable_auto_commit=False)

	try:

		for Message in Kafka_Discord_Consumer:

			# handle Message.
			#Kafka_Message = Schema.IoT_Data_Pack_Model(**json.loads(Message.value.decode()))

			# Handle Headers
			Command = Message.headers[0][1].decode('ASCII')
			Device_ID = Message.headers[1][1].decode('ASCII')
			Device_Time = Message.headers[2][1].decode('ASCII')
			Device_IP = Message.headers[3][1].decode('ASCII')

			Message = str(Device_ID) + " kodlu cihazdan veri geldi. \n Komut : " + str(Command) + " (" + str(Device_Time) + ") \n" + str(Message.value)

			await channel.send(Message)

			# Commit Message
			Kafka_Discord_Consumer.commit()

			# Log
			print("Message send to discord. \n", Message)

	finally:
		
		print("Error Accured !!")

client.run(TOKEN)

