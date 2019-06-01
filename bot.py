configPrefix = "main"


upperPrefix = configPrefix.upper()


global botList
global channelList
global gameConfig
global TOKEN
global botID
from load import *


terminalPrefix = terminalPre.format(upperPrefix)
TOKEN = botList[configPrefix]
channelID = channelList[configPrefix]
dungeonLevel = dungeonList[configPrefix]


import asyncio
import discord
import re



# Start discord client
client = discord.Client()



async def my_background_task():
	await client.wait_until_ready()
	await asyncio.sleep(5) # wait for everything loads properly
	channel = discord.Object(id=channelID)
	botAgent = discord.Object(id=botID)
	YuiID = "577141901690667019" # Yui
	levelYui = discord.Object(id=YuiID)
	while not client.is_closed:
		try:
			now = datetime.datetime.now()
			now2 = blue + "[" + str(now.strftime("%Y-%m-%d %H:%M%p")) + "] " + reset
			await client.send_message(channel, "!s")
			await asyncio.sleep(4)
			await client.send_message(channel, "!a 1")
			await client.send_message(levelYui, ">exchange")
			await asyncio.sleep(1810)
		except Exception as e:
			pass


async def yui():
	await client.wait_until_ready()
	await asyncio.sleep(5)
	YuiID = "577141901690667019" # Yui
	levelYui = discord.Object(id=YuiID)
	while not client.is_closed:
		try:
			await client.send_message(levelYui, ">chop")
			await client.send_message(levelYui, ">fish")
			await client.send_message(levelYui, ">mine")
			await asyncio.sleep(6.5)
		except Exception as e:
			pass
		
async def yuidaily():
	await client.wait_until_ready()
	await asyncio.sleep(5)
	YuiID = "577141901690667019" # Yui
	levelYui = discord.Object(id=YuiID)
	while not client.is_closed:
		try:
			await client.send_message(levelYui, ">daily")
			await client.send_message(levelYui, ",daily")
			await asyncio.sleep(3)
			await client.send_message(levelYui, ",dailygacha")
			await client.send_message(levelYui, ",dailykeys")
			await asyncio.sleep(2)
			await client.send_message(levelYui, "!daily")
			await asyncio.sleep(42305)
		except Exception as e:
			pass


# Threading event
@client.event
async def on_message(message):
	now = datetime.datetime.now()
	now2 = blue + "[" + str(now.strftime("%Y-%m-%d %H:%M%p")) + "] " + reset
	msger = message.content
	gChannel2 = discord.Object(id=gChannel)
	if message.channel.id.strip() == callChannel and msger.lower() == ">rush" and (message.author.id.strip() == "530422225510072320" or message.author.id.strip() == "423359966729076737"):
		await client.send_message(gChannel2, "guild adventure join")
		print(terminalPrefix + guildSuccess)
		await asyncio.sleep(10)
	if message.author == client.user:
		return
	if message.channel.id.strip() != channelID: # phong-chung
		return
	if (message.author.id.strip() == botID or allChat == 1) and msger != "":
		print(validMessage.format(message.author.id.strip(), msger))
	if (message.author.id.strip() == botID or allChat == 1) and msger == "":
		print(encryptedMessage.format(message.author.id.strip()))



@client.event
async def on_ready():
	print(successLogin.format(client.user.name, client.user.id))
	print(reset + '------')


client.loop.create_task(my_background_task())
client.loop.create_task(yui())
client.loop.create_task(yuidaily())
while True:
	try:
		client.loop.run_until_complete(client.start(TOKEN,bot = False))
	except BaseException:
			time.sleep(5)
#client.run(TOKEN,bot = False)
