from seleniumbase import SB
import random
import os

URL_OVERVIEW = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=overview'
URL_HASH = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=overview'
LOGIN = "/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button"

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

RANDOM_SLEEP = float(random.randint(40, 80) / 50)

# MAIN BUTTONS:
ESTRUCTURAS = 'span:contains("Estructuras")'
TECNOLOGIAS = 'span:contains("Tecnologías")'
FLOTAS = 'span:contains("Flotas")'
DEFENSA = 'span:contains("Defensas")'
RECURSOS = 'span:contains("Recursos")'


def realistic_browser_history(sb):
    url = "https://www.google.com/"
    sb.activate_cdp_mode(url)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.sleep(6)
    sb.cdp.send_keys("APjFqb", "ogame\n")
    print('ogame Suscesfully!')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys("APjFqb", "ogame wikipedia\n")
    print('ogame wikipedia Suscesfully!')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('h3:contains("OGame - Wikipedia, la enciclopedia libre")')
    print('History Suscesfully!')
    sb.cdp.sleep(RANDOM_SLEEP)


def antibot_detection(sb):
    url = "https://seleniumbase.io/antibot/login"
    sb.activate_cdp_mode(url)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.press_keys("input#username", "demo_user")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.press_keys("input#password", "secret_pass")
    x, y = sb.cdp.get_gui_element_center("button#myButton")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.uc_gui_click_x_y(x, y)
    sb.sleep(1.5)
    x, y = sb.cdp.get_gui_element_center("a#log-in")
    sb.uc_gui_click_x_y(x, y)
    sb.assert_text("Welcome!", "h1")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.set_messenger_theme(location="bottom_center")
    sb.post_message("SeleniumBase wasn't detected!")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.sleep(15)
    print("Bot detected!")
    sb.cdp.sleep(15)


def browser_scan(sb):
    url = "https://www.browserscan.net/bot-detection"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.cdp.flash("Test Results", duration=4)
    sb.sleep(5)
    sb.cdp.assert_element('strong:contains("Normal")')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.flash('strong:contains("Normal")', duration=4, pause=4)
    sb.sleep(5)
    print('Bot detected!')
    sb.cdp.sleep(RANDOM_SLEEP)


def fingerprint(sb):
    url = "https://demo.fingerprint.com/playground"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.cdp.highlight('a[href*="browser-bot-detection"]')
    bot_row_selector = 'table:contains("Bot") tr:nth-of-type(3)'
    print(sb.cdp.get_text(bot_row_selector))
    sb.cdp.assert_text("Bot Not detected", bot_row_selector)
    sb.cdp.highlight(bot_row_selector)
    sb.sleep(2)
    print('Bot detected!')
    sb.cdp.sleep(RANDOM_SLEEP)


# driver.close()
def checkLogin(sb):
    sb.cdp.sleep(6)
    if isLogin(sb):
        pass
    else:
        login(sb)


def isLogin(sb):
    sb.activate_cdp_mode(URL_OVERVIEW)
    content = sb.cdp.find_element("#content")
    if content:
        print('IsLogin')
        return True
    else:
        print('Isn`t Login')
        return False
    print('Isn`t Login')
    return False


def login(sb):
    print("Logueando...")
    sb.activate_cdp_mode("http://srv220118-206152.vps.etecsa.cu/index.php")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('#username', USERNAME)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('#password', PASSWORD)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click_if_visible(LOGIN)
    sb.sleep(6)
    print("Logueado!")
    print("Try login again!")
    sb.sleep(5)
    checkLogin(sb)
    print('Try login again!')
    sb.sleep(5)
    checkLogin(sb)


def main(SB):
    with SB(uc=True, test=True) as sb:
        # login(sb)
        realistic_browser_history(sb)


main(SB)
