import json
import datetime

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

configPath = "config\\botconfig.json"
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


text = "You have completed your dungeon and received"
text2 = "You died on your mission. Try again!"
text3 = "You are on no mission yet. Use `!adventure [DungeonID]` to go out on an adventure!"
text4 = "You are currently in the adventure with difficulty"
text5 = "Successfully sent your character out on an adventure. Use `!status` to see the current status of the mission."
