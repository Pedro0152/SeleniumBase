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
START = 'button:contains("Start")'
START2 = 'button[type="Submit"]'
START3 = '/html/body/div/main/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/form/div/button'

# Login
EMAIL_INPUT = 'input[id="email"]'
PASSWORD_INPUT = 'input[id="password"]'
SUBMIT_BUTTON = 'button[type="submit"]'
DAILY_REWARD = 'button:contains("Redeem now")'
DAILY_REWARD2 = 'button:contains("Redeem")'
DAILY_REWARD3 = '/html/body/div/main/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/button'

# Skills
WOODCUTTING = 'https://web.idle-mmo.com/skills/view/woodcutting'

# Logs
SPRUCE_LOG = 'span[class="truncate"]'

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
        sb.cdp.click(DAILY_REWARD3)
        print('Daily Reward2')
        sb.cdp.sleep(2)
    except Exception as e:
        print('Daily Reward fail', e)

def woodcutting(sb):
    sb.cdp.get(WOODCUTTING)
    sb.cdp.sleep(2)
    try:
        sb.cdp.click(SPRUCE_LOG)
        sb.cdp.sleep(1)
        sb.cdp.mouse_click(START3)
        print('Woodcutting')
    except Exception as e:
        print('Start woodcutting fail', e)
        try:
            sb.cdp.sleep(2)
            sb.cdp.mouse_click(START)
            print('Woodcutting')
        except Exception as e:
            print('Start Woodcutting fail2', e)
            try:
                sb.cdp.sleep(2)
                sb.cdp.mouse_click(START2)
                print('Woodcutting')
            except Exception as e:
                print('Start Woodcutting fail3', e)
    sb.cdp.sleep(3)

def main(SB):
    with SB(uc=True,test=True) as sb:
        login(sb)
        get_daily_reward(sb)
        sb.cdp.open(URL_OVERVIEW)
        woodcutting(sb)
        message = 'Idle Mmo Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
        # send_warning_voice_call(sb)

main(SB)
