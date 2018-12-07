global botList
global channelList
global gameConfig
global TOKEN
global botID
from load import *


TOKEN = "NDIzMzU5OTY2NzI5MDc2NzM3.DryF4Q.eIX4_mijNp1ouhcKzTpG3cfzlqQ"
botID = "424606447867789312" # IdleRPG
channelID = channelList["main"]
allChat = gameConfig["allChat"]
delay = gameConfig["delay"]
dungeonLevel = 6
maxRetry = gameConfig["maxRetry"]
respondWaitTime = gameConfig["respondWaitTime"]


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
		await client.send_message(channel, "!status")
		goodRespone = False
		count = 0
		while goodRespone != True:
			if count > maxRetry:
				print (blue + now2 + red + "Quá số lần chờ yêu cầu từ BOT. Có thể BOT đã bị mất kết nối/vô hiệu hóa..." + reset)
				break
			responeFromBot = await client.wait_for_message()
			await asyncio.sleep(respondWaitTime) 
			if str(responeFromBot.author.id) == botID and ((text in responeFromBot.content) or (text2 in responeFromBot.content) or (text3 in responeFromBot.content) or (text4 in responeFromBot.content)):
				goodRespone = True
				if text in responeFromBot.content or text2 in responeFromBot.content or text3 in responeFromBot.content:
					if text in responeFromBot.content:
						match = re.match(r"You have completed your dungeon and received \*\*\$(.+)\*\* as well as a new weapon: \*\*(.+)\*\*\. Experience gained: \*\*(.+)\*\*\.", responeFromBot.content)
						print(green + "Chuyến thám hiểm đã thành công! Nhận được:")
						print(mag + " "* 35 + match.group(1) + green + " vàng" + reset)
						print(green + " "* 35 + "Vật phẩm: " + mag + match.group(2) + reset)
						print(mag + " "* 35 + match.group(3) + green + " điểm kinh nghiệm" + reset)
					if text2 in responeFromBot.content:
						print(red + "Nhân vật đã chết trong chuyến thám hiểm." + blue + " Bắt đầu chuyến thám hiểm mới..." + reset)
					if text3 in responeFromBot.content:
						print(blue + "Nhân vật hiện đang rảnh rỗi. Bắt đầu chuyến thám hiểm mới..." + reset)
					await asyncio.sleep(3)
					await client.send_message(channel,"!dungeon " + str(dungeonLevel))
					print(blue + "Đang đưa nhân vật vào thám hiểm tầng " + mag + str(dungeonLevel) + blue + " ..." + reset)
					goodRespone2 = False
					maxTimes2 = 3
					count2 = 0
					while (goodRespone2 == False):
						if count2 > maxRetry:
							print (blue + now2 + red + "Quá số lần chờ phản hồi từ BOT. Có thể BOT đã bị mất kết nối/vô hiệu hóa..." + reset)
							break
						responeFromBot2 = await client.wait_for_message(content=text5)
						if str(responeFromBot2.author.id) == botID:
							goodRespone2 = True
							print (green + "Đã đưa thành công nhân vật vào tầng " + mag + str(dungeonLevel) + green + " !" + reset)
							break
						else:
							count2 += 1
							print (blue + now2 + red + "Code 2: Hết thời gian chờ phản hồi từ BOT. Đang thử lại lần " + mag + str(count2) + reset)
							await asyncio.sleep(respondWaitTime)
					break
				if text4 in responeFromBot.content:
					print (blue + now2 + green + "Nhân vật vẫn còn sống và đang thám hiểm. Chờ tới lần kiểm tra tiếp theo.")
					break
			else:
				count += 1
				print (blue + now2 + red + "Code 1: Hết thời gian chờ phản hồi từ BOT. Đang thử lại lần " + mag + str(count) + reset)
				await client.send_message(channel, "!status")
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
		print(blue + now2 + message.author.id.strip() + reset + ": " + msger)
	if (message.author.id.strip() == botID or allChat == 1) and msger == "":
		print(blue + now2 + message.author.id.strip() + reset + ": " + red + "Tin nhắn này chứa hình ảnh hoặc đã được mã hóa và gửi từ game bot. Bỏ qua..." + reset)

        
@client.event
async def on_ready():
	print(green + 'Đã đăng nhập thành công vào tài khoản ' + blue + client.user.name + reset + " (" + mag + client.user.id + reset + ")")
	print(reset + '------')

    
client.loop.create_task(my_background_task())
client.run(TOKEN,bot = False)
