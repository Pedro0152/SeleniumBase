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

# Main BUTTONS:
ESTRUCTURAS = "http://srv220118-206152.vps.etecsa.cu/game.php?page=buildings"
TECNOLOGIAS = "http://srv220118-206152.vps.etecsa.cu/game.php?page=research"
FLEET = "http://srv220118-206152.vps.etecsa.cu/game.php?page=fleetTable"
DEFENSE = "http://srv220118-206152.vps.etecsa.cu/game.php?page=defense"
RESOURCE = "http://srv220118-206152.vps.etecsa.cu/game.php?page=resources"
HANGAR = "http://srv220118-206152.vps.etecsa.cu/game.php?page=shipyard"
BONUS = "http://srv220118-206152.vps.etecsa.cu/game.php?page=bonus&mode=bonus"
OFFICER = "http://srv220118-206152.vps.etecsa.cu/game.php?page=officier"
CONTINUE = 'input[value="Continuar"]'

PLANETS = [43,363,364,365,635,638] #  -> Moon 635 | MOON_PLANET 365

Metal_Max_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/a"
Crystal_Max_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/a"
Deuterium_Max_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/a"

# Upgrade Building Buttons
Upgrade_Robots_Button = 'button:contains("Ampliar al nivel")'
Upgrade_Metal_Mine_Button = "/html/body/div[5]/div/div/div[3]/div/div[2]/div[2]/form/button"
Upgrade_Crystal_Mine_Button = "/html/body/div[5]/div/div/div[4]/div/div[2]/div[2]/form/button"
Upgrade_Deuterium_Mine_Button = "/html/body/div[5]/div/div/div[5]/div/div[2]/div[2]/form/button"
Upgrade_Solar_Plant_Button = "/html/body/div[5]/div/div/div[6]/div/div[2]/div[2]/form/button"
Upgrade_Robot_Factory_Button = "/html/body/div[5]/div/div/div[7]/div/div[2]/div[2]/form/button"
Upgrade_Hangar_Button = '/html/body/div[5]/div/div/div[8]/div/div[2]/div[2]/form/button'
Upgrade_Metal_Warehouse_Button = '/html/body/div[5]/div/div/div[9]/div/div[2]/div[2]/form/button'
Upgrade_Crystal_Warehouse_Button = '/html/body/div[5]/div/div/div[10]/div/div[2]/div[2]/form/button'
Upgrade_Deuterium_Warehouse_Button = '/html/body/div[5]/div/div/div[11]/div/div[2]/div[2]/form/button'

# Dark Matter Officers
Dark_Matter_Geologist = 'span[class="res_921_text"]'

# Officers
Upgrade_Geologist_Button = "/html/body/div[5]/div/div/div[13]/div/div[2]/div[2]"

Energy_Button = "/html/body/div[5]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/a"

# Resources
METAL = 'span[id="current_metal"]'
CRYSTAL = 'span[id="current_crystal"]'
DEUTERIUM = 'span[id="current_deuterium"]'
ENERGY = 'span[class="res_current tooltip"]'
DARK_MATTER = 'span[class="res_current tooltip"]'

# Resources quantity
METAL_QUANTITY = 0
CRYSTAL_QUANTITY = 0
DEUTERIUM_QUANTITY = 0
ENERGY_QUANTITY = 0

# Ships
CARGO_SHIP = 'input[name="fmenge[221]"]' 
COLONIZER = 'input[name="fmenge[208]"]'
SATELLITE = 'input[name="fmenge[212]"]'

# Resource costs
Metal_Mine_Metal_cost = "/html/body/div[5]/div/div/div[3]/div/div[2]/div[1]/div[1]/b/span"
Metal_Mine_Crystal_Cost = "/html/body/div[5]/div/div/div[3]/div/div[2]/div[1]/div[2]/b/span"
Crystal_Mine_Metal_Cost = "/html/body/div[5]/div/div/div[4]/div/div[2]/div[1]/div[1]/b/span"
Crystal_Mine_Crystal_Cost = "/html/body/div[5]/div/div/div[4]/div/div[2]/div[1]/div[2]/b/span"
Deuterium_Mine_Metal_Cost = "/html/body/div[5]/div/div/div[5]/div/div[2]/div[1]/div[1]/b/span"
Deuterium_Mine_Crystal_Cost = "/html/body/div[5]/div/div/div[5]/div/div[2]/div[1]/div[2]/b/span"

# Investigation
Tecnologia_de_Computacion = "/html/body/div[5]/div/div/div[2]/div/div[2]/div[2]/form/button"
Tecnologia_de_Blindaje = "/html/body/div[5]/div/div/div[3]/div/div[2]/div[2]/form/button"
Tecnologia_de_Energia = "/html/body/div[5]/div/div/div[4]/div/div[2]/div[2]/form/button"
Tecnologia_de_Combustion = "/html/body/div[5]/div/div/div[5]/div/div[2]/div[2]/form/button"
Tecnologia_de_Impulso = "/html/body/div[5]/div/div/div[6]/div/div[2]/div[2]/form/button"
Tecnologia_de_Metal = "/html/body/div[5]/div/div/div[13]/div/div[2]/div[2]/form/button"
Tecnologia_de_Crystal = "/html/body/div[5]/div/div/div[14]/div/div[2]/div[2]/form/button"
Tecnologia_de_Deuterium = "/html/body/div[5]/div/div/div[15]/div/div[2]/div[2]/form/button"


def goToTheEmpire(sb):
    sb.cdp.get(URL_OVERVIEW)
    sb.cdp.sleep(RANDOM_SLEEP)


def getResourcesOfTheEmpire(sb):
    sb.cdp.get(URL_OVERVIEW)
    sb.cdp.sleep(RANDOM_SLEEP)


def resourceOptimization(sb):
    sb.cdp.get(URL_OVERVIEW)
    sb.cdp.sleep(RANDOM_SLEEP)
    # with the resource of the moon 
    # and the level of the buildings 
    # send the resources needed.


def defensiveMode(sb):
    sb.cdp.get(DEFENSE)
    sb.cdp.sleep(RANDOM_SLEEP)


def upgradeInvestigation(sb):
    sb.cdp.get(TECNOLOGIAS)
    sb.cdp.sleep(RANDOM_SLEEP)
    try_click(sb, Tecnologia_de_Metal, 'Tecnology')
    try_click(sb, Tecnologia_de_Crystal, 'Tecnology')
    try_click(sb, Tecnologia_de_Deuterium, 'Tecnology')


def makeBuilding(sb, metal_qty, crystal_qty, deuterium_qty):
    if not checkEnergy(sb) and crystal_qty > 2_000 and deuterium_qty > 500:
        buildSatellite(sb)
    # sb.cdp.get(URL_OVERVIEW)
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.get(ESTRUCTURAS)
    sb.cdp.sleep(2)
    try_click(sb, Upgrade_Metal_Mine_Button, 'Mine')
    try_click(sb, Upgrade_Crystal_Mine_Button, 'Mine')
    try_click(sb, Upgrade_Deuterium_Mine_Button, 'Mine')
    try_click(sb, Upgrade_Solar_Plant_Button, 'Mine')


def try_click(sb, upgrade_building_button, what_is_been_clicked:str = None):
    try:
        sb.cdp.click(upgrade_building_button)
        clicked = what_is_been_clicked
        print(f"Upgraded {clicked}")
        sb.cdp.sleep(RANDOM_SLEEP)
    except Exception as e:
        print("Exception: ",e)
        print(f"Upgrade {what_is_been_clicked} Fail")
        pass


def checkResource(sb, resource):
    try:
        resource = sb.cdp.find_element(resource)
        resource_text = resource.text
        resource_text = resource_text.split()
        resource_number = resource_text[0]
        print(resource_number)
        resource_letter = resource_text[1]
        print(resource_letter)
        try:
            resource_number = resource_number.replace(",", ".")
            print(resource_number)
        except ValueError:
            print("Invalid input: cannot convert to float.")
        resource_number = float(resource_number)
        if resource_letter == 'M':
            resource_number = resource_number * 1_000_000
            return resource_number
        elif resource_letter == 'K':
            resource_number = resource_number * 1_000
            return resource_number
        else:
            return resource_number
    except Exception as e:
        print("Exception: ",e)
        print("Resource Fail")
        pass

def checkDarkMatter(sb):
    energy = sb.cdp.find_elements(DARK_MATTER)
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


def upgradeOfficer(sb, officer):
    sb.cdp.get(OFFICER)
    sb.cdp.sleep(RANDOM_SLEEP)
    try:
        try_click(sb, officer, "Officer")
        sb.cdp.sleep(RANDOM_SLEEP)
    except Exception as e:
        print("Exception: ",e)
        print("Upgrade Fail")
        print("Not enough dark matter to upgrade officer!")
        pass

def checkAttack(sb):
    sb.cdp.get(URL_OVERVIEW)
    print('Buscando ataques...')
    sb.cdp.sleep(RANDOM_SLEEP)
    # alarm = sb.cdp.find_element('span[class="flight attack"]', timeout=3)
    attack_warning = 'span[class="flight attack"]'
    attacks = sb.cdp.select_all(attack_warning, 4)
    if len(attacks) > 0:
        print('Notificar ataque!')
        notificar_ataque(sb)
        # print('Calling...')
        # send_warning_voice_call(sb)
        sb.cdp.get(URL_OVERVIEW)
        sb.cdp.sleep(2)
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
        sb.cdp.sleep(2)
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
            # send_message(message)
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
        sb.cdp.quit()
    else:
        print("Successfully logged in.")


def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    print(requests.get(url).json())


def get_bonus(sb):
    sb.cdp.get(BONUS)
    print("get Bonus")
    sb.cdp.sleep(RANDOM_SLEEP)


def deployFleet(sb):
    try:
        sb.cdp.get(FLEET)
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.click('a[href="javascript:maxShips();"]')
        # sb.cdp.type('input[name="ship221"]', 4)
        sb.cdp.click(CONTINUE)
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.click('a:contains("Luna(L) [3:186:8]")')
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
    except:
        print('Fleet deploy Fail!')
        pass


def buildShip(sb, ship_xpath):
    try:
        sb.cdp.open(HANGAR)
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.type(ship_xpath, '2\n')
        sb.cdp.sleep(RANDOM_SLEEP)
        print('Ship build!')
    except Exception as e:
        print("Exception: ",e)
        print("Build Fail")
        pass

def checkShip(sb, ship_xpath):
    sb.cdp.get(FLEET)
    exist_cargo_ship = sb.cdp.select(ship_xpath)
    if exist_cargo_ship:
        print('Ship exist!')
        return True
    else:
        print('Ship not exist!')
        return False


def checkAllPlanets(sb):
    print('Deploy Fleet In All Planets!')
    for planet in PLANETS:
        metal_qty = checkResource(sb, METAL)
        print('metal_qty: ', metal_qty)
        crystal_qty = checkResource(sb, CRYSTAL)
        print('crystal_qty: ', crystal_qty)
        deuterium_qty = checkResource(sb, DEUTERIUM)
        print('deuterium_qty: ', deuterium_qty)
        if planet != 635 and planet != 43:
            sb.cdp.get(f"http://srv220118-206152.vps.etecsa.cu/game.php?page=overview&cp={planet}")
            if metal_qty > 8_000 and crystal_qty > 8_000:
                buildShip(sb, CARGO_SHIP)
                sb.cdp.sleep(RANDOM_SLEEP)
            makeBuilding(sb, metal_qty, crystal_qty, deuterium_qty)
            sb.cdp.sleep(RANDOM_SLEEP) 
            deployFleet(sb)
            sb.cdp.sleep(RANDOM_SLEEP)
        elif planet != 635:
            sb.cdp.get(f"http://srv220118-206152.vps.etecsa.cu/game.php?page=overview&cp={planet}")
            try:
                sb.cdp.sleep(RANDOM_SLEEP)
                if metal_qty > 8_000 and crystal_qty > 8_000:
                    buildShip(sb, CARGO_SHIP)
                    sb.cdp.sleep(RANDOM_SLEEP)
                sb.cdp.sleep(RANDOM_SLEEP)
                if metal_qty > 10_000 and crystal_qty > 20_000 and deuterium_qty > 10_000:
                    buildShip(sb, COLONIZER)
                    sb.cdp.sleep(RANDOM_SLEEP)
                makeBuilding(sb, metal_qty, crystal_qty, deuterium_qty)
                sb.cdp.sleep(RANDOM_SLEEP) 
                deployFleet(sb)
                # sb.cdp.sleep(RANDOM_SLEEP)
            except Exception:
                print('Error in planet %s, no hay recursos para construir!' % planet)
        else:
            sendFleet(sb)


def sendFleet(sb):
    planet_id = random.choice([7,8,10])
    try:
        sb.cdp.get('http://srv220118-206152.vps.etecsa.cu/game.php?page=fleetTable&cp=635')
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.get(f'http://srv220118-206152.vps.etecsa.cu/game.php?page=fleetTable&galaxy=3&system=186&planet={planet_id}&planettype=1&target_mission=7')
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
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.click('input[type="radio"][value="4"]')
        sb.cdp.click(CONTINUE)
        # sb.cdp.assert_text("Flota enviada", 'th[class="success"]')
        print('Fleet send!')
    except Exception as e:
        print("Exception: ",e)
        print("Send Fleet Fail")
        pass


def checkEnergy(sb):
    try:
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
            return False
        else:
            print('Energy is positive!')
            return True
    except Exception as e:
        print("Exception: ",e)
        print("Check Energy Fail")
        return False


def buildSatellite(sb):
    try:
        sb.cdp.open(HANGAR)
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.type(SATELLITE, '10\n')
        sb.cdp.sleep(RANDOM_SLEEP)
        print('Satellite build!')
    except Exception as e:
        print("Exception: ",e)
        print("Build Satellite Fail")
        pass


def Resource(sb, resource, position):
    try:
        resource = sb.cdp.find_elements(resource)[position]
        resource_text = resource.text
        resource_text = resource_text.split()
        resource_number = resource_text[0]
        print(resource_number)
        resource_letter = resource_text[1]
        print(resource_letter)
        try:
            resource_number = resource_number.replace(",", ".")
            print(resource_number)
        except ValueError:
            print("Invalid input: cannot convert to float.")
        resource_number = float(resource_number)
        if resource_letter == 'M':
            resource_number = resource_number * 1_000_000
            return resource_number
        elif resource_letter == 'K':
            resource_number = resource_number * 1_000
            return resource_number
        else:
            return resource_number
    except Exception as e:
        print("Exception: ",e)
        print("Resource Fail")
        return 1_000_000


def main(SB):
    with SB(uc=True, test=True) as sb:
        login(sb)
        get_bonus(sb)
        upgradeOfficer(sb, Upgrade_Geologist_Button)
        upgradeInvestigation(sb)
        # makeBuilding(sb)
        # checkAttack(sb)
        checkAllPlanets(sb)
        # METAL_QUANTITY = checkResource(sb, METAL)
        # CRYSTAL_QUANTITY = checkResource(sb, CRYSTAL)
        # DEUTERIUM_QUANTITY = checkResource(sb, DEUTERIUM)
        # checkResource(sb, ENERGY)
        # checkFleet(sb)
        message = 'Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())

main(SB)
