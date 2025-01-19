from seleniumbase import SB
import requests
import random
import os

URL_OVERVIEW ='https://2moons.cu/game.php?page=overview'
URL_HASH = 'https://2moons.cu/game.php?page=overview'
LOGIN_BUTTON = '/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button'

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

RANDOM_SLEEP = float(random.randint(40,80)/50)

#MAIN BUTTONS:
ESTRUCTURAS = 'span:contains("Estructuras")'
TECNOLOGIAS = 'span:contains("Tecnologías")'
FLOTAS = 'span:contains("Flotas")'
DEFENSA = 'span:contains("Defensas")'
RECURSOS = 'span:contains("Recursos")'
OFICIAL_BUTTON = 'button:contains("Oficial")'
RECLUTAR_BUTTON = '/html/body/div[6]/div/div[4]/div[1]/form/button'

def send_warning_voice_call(sb):
    #'https://www.callmebot.com/blog/telegram-phone-call-using-your-browser/'
    print('Calling...')
    sb.cdp.sleep(2)
    #sb.cdp.get('https://www.callmebot.com/blog/telegram-phone-call-using-your-browser/')
    #sb.cdp.sleep(3)
    voice_call_url = 'http://api.callmebot.com/start.php?source=web&user=@Forrest01&text=You are under Attack !!!! You Are Under Attack !!!!&lang=en-US-Standard-B'
    sb.cdp.get(voice_call_url)
    sb.cdp.sleep(1)
    print('Call Suscesfully!')
        

def checkLogin(sb):
    sb.cdp.sleep(6)
    if isLogin(sb):
        pass
    else:
        login(sb)


def isLogin(sb):
    sb.activate_cdp_mode(URL_OVERVIEW)
    content = sb.cdp.find_element("#contentPlanet")
    if content:
        print('IsLogin')
        return True
    else:
        print('Isn`t Login')
        return False


def login(sb):
    print("Logueando...")
    sb.activate_cdp_mode("https://2moons.cu/index.php")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('#username', USERNAME)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('#password', PASSWORD)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click_if_visible('[type="submit"]')
    #checkLogin(sb)


def update_officier(sb):
    sb.get("https://2moons.cu/game.php?page=officier")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click_if_visible(OFICIAL_BUTTON)
    reclutar_buttons = sb.cdp.find_elements(RECLUTAR_BUTTON)
    if check_MO(sb):
        reclutar_buttons[0].click()
        print('Officier updated!')
    else:
        pass


def check_MO(sb):
    mo_quantity = sb.cdp.get_text('div[class="res-text-921"]')
    officer_required_mo = sb.cdp.find_elements('span[class="c-921"]')
    geology_required_mo = float(officer_required_mo[0].text)
    mo_quantity = float(get_numbers_from_string(mo_quantity) * 1000)
    if mo_quantity >= geology_required_mo:
        print('MO quantity is enough!')
        return True
    else:
        print('MO quantity is not enough!')
        return False
    
    
def get_numbers_from_string(s):
    return ''.join([char for char in s if char.isdigit()])


def main(SB):
    with SB(uc=True,test=True) as sb:
        login(sb)
        update_officier(sb)
        send_warning_voice_call(sb)


main(SB)
