import json
import datetime
import random

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

configPath = "botconfig.json"
def loadConfig(path):
	with open(path) as configFile: # load config file
		data = json.load(configFile)	# save data
	botList = data["botList"]
	channelList = data["channelList"]
	gameConfig = data["gameConfig"]

with open(configPath) as configFile: # load config file
	data = json.load(configFile)	# save data
botList = data["botList"]
channelList = data["channelList"]
gameConfig = data["gameConfig"]

respondWaitTime = gameConfig["respondWaitTime"]
maxRetry = gameConfig["maxRetry"]
delay = gameConfig["delay"]
allChat = gameConfig["allChat"]
botID = "424606447867789312" # IdleRPG
dungeonList = gameConfig["dungeonLevel"]
minDelay = gameConfig["minDelay"]
maxDelay = gameConfig["maxDelay"]

callChannel = "532945506549366784"

text = "You have completed your dungeon and received"
text2 = "You died on your mission. Try again!"
text3 = "You are on no mission yet. Use `!adventure [DungeonID]` to go out on an adventure!"
text4 = "You are currently in the adventure with difficulty"
text5 = "Successfully sent your character out on an adventure. Use `!status` to see the current status of the mission."
reachMaxTimeOut = blue + red + "Quá số lần chờ phản hồi từ BOT. Có thể BOT đã bị mất kết nối/vô hiệu hóa..." + reset
success = green + "Chuyến thám hiểm đã thành công! Nhận được:"
charDie = red + "Nhân vật đã chết trong chuyến thám hiểm." + blue + " Bắt đầu chuyến thám hiểm mới..." + reset
charFree = blue + "Nhân vật hiện đang rảnh rỗi. Bắt đầu chuyến thám hiểm mới..." + reset
exp = " điểm kinh nghiệm"
goldReward = mag + " "* 35 + "{}" + green + " vàng" + reset
itemReward = green + " "* 35 + "Vật phẩm: " + mag + "{}" + reset
xpReward = mag + " "* 35 + "{}" + green + " điểm kinh nghiệm" + reset
stillAlive = blue + green + "Nhân vật vẫn còn sống và đang thám hiểm. Chờ tới lần kiểm tra tiếp theo."
encryptedMessage = blue + "{}" + reset + ": " + red + "Tin nhắn này chứa hình ảnh hoặc đã được mã hóa và gửi từ game bot. Bỏ qua..." + reset
validMessage = blue + "{}" + reset + ": " + "{}"
statusCommand = "!s"
dungeonCommand = "!a {}"
inDungeon = blue + "Đang đưa nhân vật vào thám hiểm tầng " + mag + "{}" + blue + " ..." + reset
enteredDungeon = green + "Đã đưa thành công nhân vật vào tầng " + mag + "{}" + green + " !" + reset
timeOut = blue + red + "Code {}: Hết thời gian chờ phản hồi từ BOT. Đang thử lại lần " + mag + "{}" + reset
successLogin = green + 'Đã đăng nhập thành công vào tài khoản ' + blue + "{}" + reset + " (" + mag + "{}" + reset + ")"
terminalPre = blue + "[" + mag + "{}" + blue + "]: " + reset

bDelay = delay - minDelay
aDelay = delay + maxDelay
delay = random.randint(bDelay,aDelay)
