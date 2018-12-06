# Python version: 3.6
# Import library
import asyncio
import discord
import datetime
import re

# Colorz define

global now
global now2
mag = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
orange = '\033[93m'
red = '\033[91m'
white = '\033[0m'
gray = '\033[1m'
highlight = '\033[4m'
reset = '\033[0;0m'
now = datetime.datetime.now()
now2 = blue + "[" + str(now.strftime("%Y-%m-%d %H:%M%p")) + "] " + reset


# Some extremely useful variable <(")
TOKEN = 'NDIzMzU5OTY2NzI5MDc2NzM3.DryF4Q.eIX4_mijNp1ouhcKzTpG3cfzlqQ'
botID = "424606447867789312" # IdleRPG
channelID = "470648551475511333" # phong-chung
allChat = 1 # 1: collect message from all users/ 0: only BOT message
delay = 600  # (seconds) task runs every *delay seconds
dungeonLevel = "3"  
timeOutConfig = 5 # (seconds) time to wait for bot's respone
text = "You have completed your dungeon and received"
text2 = "You died on your mission. Try again!"
text3 = "You are on no mission yet. Use `!adventure [DungeonID]` to go out on an adventure!"
text4 = "You are currently in the adventure with difficulty"
text5 = "Successfully sent your character out on an adventure. Use `!status` to see the current status of the mission."

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
        maxTimes = 3
        count = 0
        while goodRespone != True or not count >= maxTimes:
        	responeFromBot = await client.wait_for_message()
        	count += 1
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
        			await client.send_message(channel,"!dungeon " + dungeonLevel)
        			print(blue + "Đang đưa nhân vật vào thám hiểm tầng " + mag + dungeonLevel + blue + " ..." + reset)
        			goodRespone2 = False
        			maxTimes2 = 3
        			count2 = 0
        			while (goodRespone2 == False) or (count2 <= maxTimes2):
        				responeFromBot2 = await client.wait_for_message(content=text5)
        				count2 += 1
        				if str(responeFromBot2.author.id) == botID:
        					goodRespone2 = True
        					print (green + "Đã đưa thành công nhân vật vào tầng " + mag + dungeonLevel + green + " !" + reset)
        					break
        				else:
        					print (blue + now2 + red + "Hết thời gian chờ phản hồi từ BOT. Đang thử lại lần " + mag + str(count2) + reset)
        			if count2 >= 3:
        				print (blue + now2 + red + "Quá số lần chờ yêu cầu từ BOT. Có thể BOT đã bị mất kết nối/vô hiệu hóa..." + reset)
        			break
        		if text4 in responeFromBot.content:
        			print (blue + now2 + green + "Nhân vật vẫn còn sống và đang thám hiểm. Chờ tới lần kiểm tra tiếp theo.")
        			break
        	else:
        		print (blue + now2 + red + "Hết thời gian chờ phản hồi từ BOT. Đang thử lại lần " + mag + str(count) + reset)
        if count >= 3:
        	print (blue + now2 + red + "Quá số lần chờ yêu cầu từ BOT. Có thể BOT đã bị mất kết nối/vô hiệu hóa..." + reset)
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
