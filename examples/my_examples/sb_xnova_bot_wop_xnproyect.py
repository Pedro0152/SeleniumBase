from seleniumbase import SB
import requests
import random
import os

URL_OVERVIEW = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=overview'
URL_HASH = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=overview'
LOGIN = "/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button"

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

RANDOM_SLEEP = float(random.randint(100, 200) / 50)

# BUTTONS:
ESTRUCTURAS = 'span:contains("Estructuras")'
TECNOLOGIAS = 'span:contains("Tecnologías")'
FLEET = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=fleetTable'
DEFENSE = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=defense'
RESOURCE = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=resources'
HANGAR = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=shipyard'
BONUS = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=bonus&mode=bonushall'
CONTINUE = 'input[value="Continuar"]'

PLANETS = [248,117,267,391,638,1048] #  -> Moon | MOON_PLANET -> 

Metal_Max_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/a"
Crystal_Max_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/a"
Deuterium_Max_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/a"

ENERGY = 'span[class="res_current tooltip"]'

CARGO_SHIP = 'input[name="fmenge[221]"]' 
COLONIZER = 'input[name="fmenge[208]"]'
SATELLITE = 'input[name="fmenge[212]"]'

def checkAttack(sb):
    sb.cdp.get(URL_OVERVIEW)
    print('Buscando ataques...')
    sb.cdp.sleep(RANDOM_SLEEP)
    print('0')
    # alarm = sb.cdp.find_element('span[class="flight attack"]', timeout=3)
    attack_warning = 'span[class="flight attack"]'
    attacks = sb.cdp.select_all(attack_warning, timeout=3)
    if len(attacks) > 0:
        print('Notificar ataque!')
        notificar_ataque(sb)
        # print('Calling...')
        # send_warning_voice_call(sb)
        sb.cdp.get(URL_OVERVIEW)
        sb.sleep(2)
    else:
        print('No hay ataques a la vista!')
        pass


def checkFleet(sb):
    sb.cdp.get(URL_OVERVIEW)
    print('Buscando Fleets...')
    sb.cdp.sleep(RANDOM_SLEEP)
    print('0')
    colonize_warning = 'span[class="flight owndeploy"]'
    colonizes = sb.cdp.select_all(colonize_warning)
    print("cantidad:", len(colonizes))
    if len(colonizes) > 0:
        print('Notificar fleet!')
        notificar_fleet(sb)
        # print('Calling...')
        # send_warning_voice_call(sb)
        sb.cdp.get(URL_OVERVIEW)
        sb.sleep(2)
    else:
        print('No hay fleets a la vista!')
        pass

def notificar_ataque(sb):
    sb.cdp.get(URL_OVERVIEW)
    sb.cdp.sleep(2)
    span_element = sb.cdp.find_element("attack")
    if span_element:
        message = span_element.text
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
    else:
        print("No hay ataques a la vista!")


def notificar_fleet(sb):
    sb.cdp.get(URL_OVERVIEW)
    sb.cdp.sleep(2)
    span_element = sb.cdp.find_element("flight owndeploy")
    if span_element:
        message = span_element.text
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
    else:
        print("No hay fleets a la vista!")


def send_warning_voice_call(sb):
    # 'https://www.callmebot.com/blog/telegram-phone-call-using-your-browser/'
    print('Calling...')
    sb.cdp.sleep(2)
    # sb.cdp.get('https://www.callmebot.com/blog/telegram-phone-call-using-your-browser/')
    # sb.cdp.sleep(3)
    voice_call_url = 'http://api.callmebot.com/start.php?source=web&user=@Forrest01&text=You are under Attack !!!! You Are Under Attack !!!!&lang=en-US-Standard-B'
    sb.cdp.get(voice_call_url)
    sb.cdp.sleep(1)
    print('Call Suscesfully!')


def realistic_browser_history(sb):
    url = "https://google.com/ncr"
    sb.activate_cdp_mode(url)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.sleep(6)
    sb.cdp.send_keys('[title="Search"]', "ogame\n")
    print('ogame Suscesfully!')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('[title="Search"]', "ogame wikipedia\n")
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


def checkLogin(sb, max_retries=3):
    retries = 0
    while retries < max_retries:
        if isLogin(sb):
            message = "Login successful!"
            send_message(message)
            print(message)
            return True
        else:
            retries += 1
            print(f"Attempt {retries} failed. Retrying...")
            login(sb)
    message = "Max retries reached. Login failed."
    send_message(message)
    print(message)
    return False


def isLogin(sb):
    # sb.activate_cdp_mode(URL_OVERVIEW)
    sb.cdp.sleep(RANDOM_SLEEP)
    content = sb.cdp.select("#content")
    if content:
        message = 'IsLogin'
        print(message)
        isLogin = True
    else:
        message = 'Isn`t Login'
        print(message)
        isLogin = False
    return isLogin


def login(sb):
    print("Logueando...")
    sb.activate_cdp_mode("http://srv220118-206152.vps.etecsa.cu/index.php")
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('#username', USERNAME)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.send_keys('#password', PASSWORD)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click_if_visible(LOGIN)
    sb.sleep(4)
    if not checkLogin(sb):
        print("Failed to log in after multiple attempts.")
    else:
        print("Successfully logged in.")


def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    print(requests.get(url).json())


def get_bonus(sb):
    sb.cdp.get(BONUS)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('i[class="far fa-gem"]')
    # href="game.php?page=bonus&mode=bonus"
    sb.cdp.sleep(RANDOM_SLEEP)
    date = sb.get_text('div[style="text-align: center; padding: 10px"]')
    bonus_hour = date.split()[9]
    print(f"Bonus hour: {bonus_hour}")
    send_message(bonus_hour)
    sb.cdp.sleep(2)


def deployFleet(sb):
    sb.cdp.get(FLEET)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('a[href="javascript:maxShips();"]')
    # sb.cdp.type('input[name="ship221"]', 4)
    sb.cdp.click(CONTINUE)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('a:contains("Colonia [1:84:10]")')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('input[value="Continuar"]')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('input[type="radio"][value="4"]')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click(Metal_Max_Button)
    sb.cdp.click(Crystal_Max_Button)
    sb.cdp.click(Deuterium_Max_Button)
    sb.cdp.click(CONTINUE)
    # sb.cdp.assert_text("Flota enviada", 'th[class="success"]')
    print('Fleet deploy!')


def buildShip(sb, ship_xpath):
    sb.cdp.open(HANGAR)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.type(ship_xpath, '2\n')
    sb.cdp.sleep(RANDOM_SLEEP)
    print('Ship build!')


def checkShip(sb, ship_xpath):
    sb.cdp.get(FLEET)
    exist_cargo_ship = sb.cdp.select(ship_xpath)
    if exist_cargo_ship:
        print('Ship exist!')
        return True
    else:
        print('Ship not exist!')
        return False


def deployFleetInAllPlanets(sb):
    print('Deploy Fleet In All Planets!')
    for planet in PLANETS:
        if planet != 1037 and planet != 248:
            sb.cdp.get(f"http://srv220118-206152.vps.etecsa.cu/game.php?page=overview&cp={planet}")
            sb.cdp.sleep(RANDOM_SLEEP)
            checkEnergy(sb)
            sb.cdp.sleep(RANDOM_SLEEP)
            buildShip(sb, CARGO_SHIP)
            sb.cdp.sleep(RANDOM_SLEEP)
            deployFleet(sb)
            sb.cdp.sleep(RANDOM_SLEEP)
        elif planet != 1037:
            sb.cdp.get(f"http://srv220118-206152.vps.etecsa.cu/game.php?page=overview&cp={planet}")
            try:
                sb.cdp.sleep(RANDOM_SLEEP)
                buildShip(sb, CARGO_SHIP)
                sb.cdp.sleep(RANDOM_SLEEP)
                buildShip(sb, COLONIZER)
                sb.cdp.sleep(RANDOM_SLEEP)
                deployFleet(sb)
                # sb.cdp.sleep(RANDOM_SLEEP)
            except Exception:
                print('Error in planet %s, no hay recursos para construir!' % planet)
        else:
            sendFleet(sb)


def sendFleet(sb):
    sb.cdp.get('http://srv220118-206152.vps.etecsa.cu/game.php?page=fleetTable&cp=1037')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.get('http://srv220118-206152.vps.etecsa.cu/game.php?page=fleetTable&galaxy=2&system=177&planet=11&planettype=1&target_mission=7')
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click('a:contains("Todas las naves")')
    sb.cdp.click(CONTINUE)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click(CONTINUE)
    sb.sleep(RANDOM_SLEEP)
    sb.cdp.click(Metal_Max_Button)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click(Crystal_Max_Button)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.click(Deuterium_Max_Button)
    sb.cdp.click(CONTINUE)
    # sb.cdp.assert_text("Flota enviada", 'th[class="success"]')
    print('Fleet send!')


def checkEnergy(sb):
    energy = sb.cdp.find_elements(ENERGY)[3]
    energy_text = energy.text
    print(energy_text)
    energy_text = energy_text.split()[0]
    try:
        energy_number = energy_text.replace(",", ".")
        print(energy_number)
    except ValueError:
        print("Invalid input: cannot convert to float.")
    energy_number = float(energy_number)
    print(energy_number)
    if  energy_number < 0:
        print('Energy is negative!')
        buildSatellite(sb)
    else:
        print('Energy is positive!')


def buildSatellite(sb):
    sb.cdp.open(HANGAR)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.type(SATELLITE, '100\n')
    sb.cdp.sleep(RANDOM_SLEEP)
    print('Satellite build!')


def main(SB):
    with SB(uc=True, test=True) as sb:
        login(sb)
        # get_bonus(sb)
        # checkAttack(sb)
        deployFleetInAllPlanets(sb)
        checkFleet(sb)
        message = 'Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())

main(SB)
