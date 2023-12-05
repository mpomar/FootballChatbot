# LOAD MODULES 
import time
import requests
import json
from chatbot import openSocket, sendMessage, joinRoom
from config import RAPIDAPI_URL, RAPIDAPI_HOST, RAPIDAPI_KEY
import schedule

# INITIATE CHAT BOT 
def reload():
    s = openSocket()
    joinRoom(s)
    time.sleep(3)

# API HTTP REQUEST TO API-FOOTBALL 
    headers = {
        'x-rapidapi-host': RAPIDAPI_HOST,
        'x-rapidapi-key': RAPIDAPI_KEY
        }

    sendMessage(s, 'Live football fixtures:')
    response = requests.request("GET", RAPIDAPI_URL, headers=headers)
    jload = json.loads(response.text)
    jload = jload["api"]["fixtures"]

# PARSE JSON RESPONSE 
    for x in range(0, len(jload)):
        y = jload[x]
        hometeam = y['homeTeam']['team_name']
        homescore = y['goalsHomeTeam']
        awayteam = y['awayTeam']['team_name']
        awayscore = y['goalsAwayTeam']
        elapsed = y['elapsed']
        liveresults = hometeam + ' - ' + awayteam + ' ' + str(homescore) + '-' + str(awayscore) + ' (' + str(elapsed) + "')"
        print(liveresults)

# SEND FIXTURES TO CHAT 
        time.sleep(3)
        sendMessage(s, liveresults)

schedule.every(5).minutes.do(reload)

while True:
    schedule.run_pending()
    time.sleep(1)
