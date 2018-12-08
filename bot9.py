configPrefix = "bot9"



global botList
global channelList
global gameConfig
global TOKEN
global botID
from load import *



TOKEN = botList[configPrefix]
channelID = channelList[configPrefix]



import asyncio
import discord
import re



# Start discord client
client = discord.Client()



async def my_background_task():
	await client.wait_until_ready()
	await asyncio.sleep(5)
	channel = discord.Object(id=channelID)
	botAgent = discord.Object(id=botID)
	while not client.is_closed:
		now = datetime.datetime.now()
		now2 = blue + "[" + str(now.strftime("%Y-%m-%d %H:%M%p")) + "] " + reset
		goodRespone = False
		count = 0
		while goodRespone != True:
			if count > maxRetry:
				print (reachMaxTimeOut)
				break
			await client.send_message(channel, statusCommand)
			responeFromBot = await client.wait_for_message()
			if str(responeFromBot.author.id) == botID and ((text in responeFromBot.content) or (text2 in responeFromBot.content) or (text3 in responeFromBot.content) or (text4 in responeFromBot.content)):
				goodRespone = True
				if text in responeFromBot.content or text2 in responeFromBot.content or text3 in responeFromBot.content:
					if text in responeFromBot.content:
						match = re.match(r"You have completed your dungeon and received \*\*\$(.+)\*\* as well as a new weapon: \*\*(.+)\*\*\. Experience gained: \*\*(.+)\*\*\.", responeFromBot.content)
						print(success)
						print(goldReward.format(match.group(1)))
						print(itemReward.format(match.group(2)))
						print(xpReward.format(match.group(3)))
					if text2 in responeFromBot.content:
						print(charDie)
					if text3 in responeFromBot.content:
						print(charFree)
					await asyncio.sleep(3)
					await client.send_message(channel, dungeonCommand.format(str(dungeonLevel)))
					print(inDungeon.format(str(dungeonLevel)))
					goodRespone2 = False
					maxTimes2 = 3
					count2 = 0
					while (goodRespone2 == False):
						if count2 > maxRetry:
							print(reachMaxTimeOut)
							break
						responeFromBot2 = await client.wait_for_message(content=text5)
						if str(responeFromBot2.author.id) == botID:
							goodRespone2 = True
							print (enteredDungeon.format(str(dungeonLevel)))
							break
						else:
							count2 += 1
							print (timeOut.format(2, str(count2)))
							await asyncio.sleep(respondWaitTime)
					break
				if text4 in responeFromBot.content:
					print(stillAlive)
					break
			else:
				count += 1
				print (timeOut.format(1, str(count)))
		await asyncio.sleep(delay)



# Threading event
@client.event
async def on_message(message):
	now = datetime.datetime.now()
	now2 = blue + "[" + str(now.strftime("%Y-%m-%d %H:%M%p")) + "] " + reset
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	if message.channel.id.strip() != channelID: # phong-chung
		return
	msger = message.content
	if (message.author.id.strip() == botID or allChat == 1) and msger != "":
		print(validMessage.format(message.author.id.strip(), msger))
	if (message.author.id.strip() == botID or allChat == 1) and msger == "":
		print(encryptedMessage)



@client.event
async def on_ready():
	print(successLogin.format(client.user.name, client.user.id))
	print(reset + '------')


client.loop.create_task(my_background_task())
client.run(TOKEN,bot = False)
