from seleniumbase import SB
import random
import os

URL_OVERVIEW ='https://2moons.cu/game.php?page=overview'
URL_HASH = 'https://2moons.cu/game.php?page=overview'
TOKEN = '6198582894:AAF5CoOoqjdtuilFZ-uNi9flh7eqlv_yJBg'
CHAT_ID = '1032943352'

LOGIN_BUTTON = '/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button'

USERNAME = 'Aguacate'
PASSWORD = 'Warehouse*13'

RANDOM_SLEEP = float(random.randint(40,80)/50)

#MAIN BUTTONS:
ESTRUCTURAS = 'span:contains("Estructuras")'
TECNOLOGIAS = 'span:contains("Tecnologías")'
FLOTAS = 'span:contains("Flotas")'
DEFENSA = 'span:contains("Defensas")'
RECURSOS = 'span:contains("Recursos")'


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
    checkLogin(sb)


def main(SB):
    with SB(uc=True,test=True) as sb:
        login(sb)
        send_warning_voice_call(sb)


main(SB)
