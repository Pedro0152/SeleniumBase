from seleniumbase import SB
import requests
import random
import os

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
EMAIL = os.environ["EMAIL"]
PASSWORD_IDLE_MMO = os.environ["PASSWORD_IDLE_MMO"]

URL_LOGIN ='https://web.idle-mmo.com/login'
URL_OVERVIEW = 'https://web.idle-mmo.com/@Kresh'
URL_HASH = 'https://2moons.cu/game.php?page=overview'
LOGIN_BUTTON = '/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button'

# Login
EMAIL_INPUT = 'input[id="email"]'
PASSWORD_INPUT = 'input[id="password"]'
SUBMIT_BUTTON = 'button[id="submit"]'
DAILY_REWARD = 'button[class="text-yellow-400"]'

def login(sb):
    sb.activate_cdp_mode(URL_LOGIN)
    try:
        sb.cdp.press_keys(EMAIL_INPUT, EMAIL)
        sb.cdp.press_keys(PASSWORD_INPUT, PASSWORD_IDLE_MMO)
        sb.cdp.click(SUBMIT_BUTTON)
        print('login!')
        sb.cdp.sleep(2)
    except Exception as e:
        print('Login fail', e)

def get_daily_reward(sb):
    try:
        sb.cdp.click(DAILY_REWARD)
        print('Daily Reward')
        sb.cdp.sleep(2)
    except Exception as e:
        print('Daily Reward fail', e)

def main(SB):
    with SB(uc=True,test=True) as sb:
        login(sb)
        get_daily_reward(sb)
        sb.cdp.open(URL_OVERVIEW)
        message = 'Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
        # send_warning_voice_call(sb)


main(SB)
