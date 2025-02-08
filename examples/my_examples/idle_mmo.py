from seleniumbase import SB
import requests
import random
import os

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

URL_OVERVIEW ='https://2moons.cu/game.php?page=overview'
URL_HASH = 'https://2moons.cu/game.php?page=overview'
LOGIN_BUTTON = '/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button'

user = 'input[id="email"]'

def main(SB):
    with SB(uc=True,test=True) as sb:
        login(sb)
        update_officier(sb)
        message = 'Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
        # send_warning_voice_call(sb)


main(SB)
