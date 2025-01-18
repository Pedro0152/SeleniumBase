from seleniumbase import SB
import requests
import keyboard
import random
import csv
import os

URL_OVERVIEW ='http://srv220118-206152.vps.etecsa.cu/game.php?page=overview'
URL_HASH = 'http://srv220118-206152.vps.etecsa.cu/game.php?page=overview'

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


#options = uc.ChromeOptions()
#options.add_argument("start-maximized")
# options.add_argument("--password-store=basic")
# options.add_argument("user-data-dir=C:/Users/Android/AppData/Local/Google/Chrome/User Data/Default")
# options.add_experimental_option(
#     "prefs",
#     {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False,
#     },
# ) 
# options.add_argument("--headless")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options)

# driver = uc.Chrome(
#     options=options,
#     headless=False,
# )

def send_warning_voice_call(sb):
    #'https://www.callmebot.com/blog/telegram-phone-call-using-your-browser/'
    try:
        print('Calling...')
        sb.cdp.sleep(2)
        #sb.cdp.get('https://www.callmebot.com/blog/telegram-phone-call-using-your-browser/')
        #sb.cdp.sleep(3)
        voice_call_url = 'http://api.callmebot.com/start.php?source=web&user=@Forrest01&text=You are under Attack !!!! You Are Under Attack !!!!&lang=en-US-Standard-B'
        sb.cdp.get(voice_call_url)
        sb.cdp.sleep(1)
        print('Call Suscesfully!')
    except:
        print('Call fail!')
        
def realistic_browser_history(sb):
    try:
        sb.cdp.get("https://www.google.com/")
        sb.sleep(RANDOM_SLEEP)
        sb.cdp.send_keys("APjFqb", "ogame\n")
        sb.sleep(RANDOM_SLEEP)
        sb.cdp.send_keys("APjFqb", "ogame wikipedia\n")
        sb.sleep(RANDOM_SLEEP)
        sb.cdp.click('h3:contains("OGame - Wikipedia, la enciclopedia libre")')
        print('History Suscesfully!')
        sb.sleep(RANDOM_SLEEP)
    except:
        print('History fail!')
        sb.sleep(RANDOM_SLEEP)
        pass
        
def antibot_detection(sb):
    try:
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
        sb.sleep(1.5)
    except:
        print("Bot detected!")
        sb.cdp.sleep(RANDOM_SLEEP)
        pass

def browser_scan(sb):
    try:
        url = "https://www.browserscan.net/bot-detection"
        sb.activate_cdp_mode(url)
        sb.sleep(1)
        sb.cdp.flash("Test Results", duration=4)
        sb.sleep(5)
        sb.cdp.assert_element('strong:contains("Normal")')
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.flash('strong:contains("Normal")', duration=4, pause=4)
        sb.sleep(5)
    except:
        print('Bot detected!')
        sb.cdp.sleep(RANDOM_SLEEP)

def fingerprint(sb):
    try:
        url = "https://demo.fingerprint.com/playground"
        sb.activate_cdp_mode(url)
        sb.sleep(1)
        sb.cdp.highlight('a[href*="browser-bot-detection"]')
        bot_row_selector = 'table:contains("Bot") tr:nth-of-type(3)'
        print(sb.cdp.get_text(bot_row_selector))
        sb.cdp.assert_text("Bot Not detected", bot_row_selector)
        sb.cdp.highlight(bot_row_selector)
        sb.sleep(2)
    except:
        print('Bot detected!')
        sb.cdp.sleep(RANDOM_SLEEP)

#driver.close()
def checkLogin(sb):
    sb.cdp.sleep(6)
    if isLogin(sb):
        pass
    else:
        login(sb)

def isLogin(sb):
    try:
        sb.activate_cdp_mode(URL_OVERVIEW)
        content = sb.cdp.find_element("#content")
        if content:
            print('IsLogin')
            return True
        else:
            print('Isn`t Login')
            return False
    except:
        print('Isn`t Login')
        return False

def login(sb):
    try:# Navigate to the login page
        print("Logueando...")
        sb.activate_cdp_mode("http://srv220118-206152.vps.etecsa.cu/index.php")
        sb.cdp.sleep(RANDOM_SLEEP)
        try:
            sb.cdp.send_keys('#username', USERNAME)
            sb.cdp.sleep(RANDOM_SLEEP)
            sb.cdp.send_keys('#password', PASSWORD)
            sb.cdp.sleep(RANDOM_SLEEP)
            sb.cdp.click_if_visible("/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button")
            sb.sleep(6)
            print("Logueado!")
        except:
            print("Try login again!")
            sb.sleep(5)
            checkLogin(sb)
    except:
        print('Try login again!')
        sb.sleep(5)
        checkLogin(sb)

def sendExpeditions(sb):
    try:
        print("Enviando expedicion...")
        # Navigate to the expedition page
        sb.cdp.get("https://xnovawop.com/game.php?page=MultiExpe")
        print('Multi Expeditions page!')
        sb.cdp.sleep(2)
        # Wait for the page to load
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "expeditionSlots")))
        # Check if there are any available expedition slots
        slots_Available = slotsAvailable(sb)
        print('slots availables: ', slots_Available)
        if slots_Available == False:
            print('pass1')
            pass
        else:
            try:
                print('Send Expedition try1')
                sb.cdp.click_if_visible('/html/body/div[5]/div/form/div[1]/div[2]/div[2]/input')
                sb.cdp.find_element('/html/body/div[5]/div/form/div[1]/div[2]/div[2]/input').clear()
                print('successful try1')
            except:
                try:
                    print('Send Expedition try2')
                    sb.cdp.find_element('/html/body/div[6]/div/form/div[1]/div[2]/div[2]/input').clear()
                    print('successful try2')
                except:
                    try:
                        print('Send Expedition try3')
                        sb.cdp.find_element('//[@id="page"]/div/form/div[1]/div[2]/div[2]/input').clear()
                        print('successful try3')
                    except:
                        try:
                            print('Send Expedition try34')
                            sb.cdp.find_element('//*[@id="page"]/div/form/div[1]/div[2]/div[2]/input').clear()
                            print('successful try34')    
                        except:
                            try:
                                print('Send Expedition try4')
                                sb.cdp.find_element('#page > div > form > div.rf-info-head > div.rf-info-right > div:nth-child(4) > input[type=number]').clear()
                                print('successful try4')
                            except:
                                try:
                                    print('Send Expedition try5')
                                    sb.cdp.find_element('expecount').clear()
                                    print('successful try5')
                                except:
                                    pass
            try:
                print('Send Expedition try6')
                sb.cdp.find_element('/html/body/div[5]/div/form/div[1]/div[2]/div[2]/input').send_keys(int(slots_Available))
                print('successful try6')
            except:
                try:
                    print('Send Expedition try7')
                    sb.cdp.find_element('/html/body/div[6]/div/form/div[1]/div[2]/div[2]/input').send_keys(int(slots_Available))
                    print('successful try7')
                except:
                    print('pass2')
                    pass
            try:
                sb.cdp.find_element('/html/body/div[6]/div/form/div/div[2]/div[3]/div/a[2]/button').click()
                # driver.find_element(By.ID, 'ship210_input').clear()
                # driver.find_element(By.ID, 'ship210_input').send_keys('12')
            except:
                sb.cdp.find_element('ship206_input').clear()
                sb.cdp.find_element('ship206_input').send_keys('12')
            try:
                print('Send Expedition try8')
                sb.cdp.find_element('/html/body/div[5]/div/form/div[2]/div[3]/button').click()
            except:
                try:
                    print('Send Expedition last try')
                    sb.cdp.find_element('/html/body/div[6]/div/form/div[2]/div[3]/button').click()
                except:
                    print('pass3')
                    pass            
            print('Expedicion enviada!')
            sb.cdp.sleep(2)
    except:
        print('Algo salio mal!')
        pass
    
def slotsAvailable(sb):
    try:
        print('Slot Available Try1')
        slots_flot = sb.cdp.find_element("/html/body/div[6]/div/form/div[1]/div[2]/button[1]").text
        slots_exp = sb.cdp.find_element("/html/body/div[6]/div/form/div[1]/div[2]/button[2]").text
        print('Finish Try1')
        print('slots_flot', slots_flot)
        print('slots_exp', slots_exp)
        slots_flotas = slots_flot.split()
        print('slots_flotas: ', slots_flotas)
        flotas_actuales = slots_flotas[0]
        print('flotas_actuales: ', flotas_actuales)
        flotas_maximas = slots_flotas[2]
        print('flotas_maximas: ', flotas_maximas)
        flotas_posibles = int(flotas_maximas) - int(flotas_actuales)
        print('flotas_posibles: ', flotas_posibles)
        
        slots_expediciones = slots_exp.split()
        print('slots_expediciones: ', slots_expediciones)
        expediciones_actuales = slots_expediciones[0]
        print('expediciones_actuales: ', expediciones_actuales)
        expediciones_maximas = slots_expediciones[2]
        print('expediciones_maximas: ', expediciones_maximas)
        expediciones_posibles = int(expediciones_maximas) - int(expediciones_actuales)
        print('expediciones_posibles: ', expediciones_posibles)
        
        if expediciones_posibles == 0:
            print("No hay slots de expediciones disponibles!")
            return False
        elif flotas_posibles == 0:
            print("No hay slots de flotas disponibles!")
            return False
        elif flotas_posibles >= expediciones_posibles:
            print('Expediciones posibles!')
            return expediciones_posibles
        else:
            print('Flotas posibles!')
            return flotas_posibles
    except:
        try:
            print('Slot Available Try2')
            slots_flot = sb.cdp.find_element("/html/body/div[5]/div/form/div[1]/div[2]/button[1]").text
            slots_exp = sb.cdp.find_element("/html/body/div[5]/div/form/div[1]/div[2]/button[2]").text
            print('Finish Try2')
        except:
            print('Slots Available Error!')
            pass

def checkAttack(sb, TOKEN, CHAT_ID):
    try:
        sb.cdp.get(URL_OVERVIEW)
        print('Buscando ataques...')
        sb.cdp.sleep(4)
        # Refresh the overview page
        alert = []
        print('0')
        alarm = sb.cdp.find_elements('span[class="flight attack"]')  # Update this selector as necessary
        sb.sleep(1)
        if alarm:
            print('Notificar ataque!')
            notificar_ataque(sb, TOKEN, CHAT_ID)
            print('Calling...')
            sb.sleep(5)
            send_warning_voice_call(sb)
            sb.cdp.get(URL_OVERVIEW)
        else:
            print('No hay ataques a la vista!')
            sb.cdp.sleep(1)
            pass
    except:
        print('No hay ataques a la vista!')
        sb.cdp.sleep(1)
        pass
        
    #     for row in rows:
    #         if "owndeploy" in row.get_attribute('class'):
    #             #row.find_element((By.CLASS_NAME, "owndeploy"))
    #         # Wait 60 seconds before checking again
    #             print('Estas bajo ataque!')
    #             notificar_ataque(driver, TOKEN, CHAT_ID)
    #             print('Alerta enviada!')
    #         else:
    #             print('skip')
    # except:
    #     print('No hay ataques a la vista!')

def notificar_ataque(sb, TOKEN, CHAT_ID):
    try:
        sb.cdp.get(URL_OVERVIEW)
        sb.cdp.sleep(2)
        span_element = sb.cdp.find_element("attack")
        message = span_element.text
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json()) # this sends the message
    except:
        print("No hay ataques a la vista!")
        pass

def makeBuilding(sb):
    # Get all the planets
    planets = sb.find_elements("#planetList .smallplanet")

    # Loop through all the planets
    for planet in planets:
        # Get the planet ID
        planet_id = planet.get_attribute("id")

        # Check if there are enough resources to build a building
        if checkPlanetResource(sb, planet_id) and checkPlanetBuilding(sb, planet_id):
            # Build the building
            buildBuilding(sb, planet_id)

def checkPlanetResource(sb, planet_id):
    # Get the planet's resources
    resources = sb.cdp.find_elements(f"#{planet_id} .resources li")

    # Check if there are enough resources to build a building
    if int(resources[0].text) >= 1000 and int(resources[1].text) >= 1000 and int(resources[2].text) >= 500:
        return True
    else:
        return False

def checkPlanetBuilding(sb, planet_id):
    # Get the planet's buildings
    buildings = sb.cdp.find_elements(f"#{planet_id} .buildings li")

    # Check if the planet has enough buildings
    if len(buildings) < 6:
        return True
    else:
        return False

def buildBuilding(sb, planet_id):
    # Get the building menu
    building_menu = sb.cdp.find_element(f"#{planet_id} .buildingMenu")

    # Click on the building menu
    building_menu.click()

    # Get the build button
    build_button = sb.cdp.find_element(f"#{planet_id} .buildingMenu .buildButton")

    # Click on the build button
    build_button.click()

def find_players_info(sb, galaxy, system):
    #driver.get("https://uni4.2moons.cu/game.php?page=galaxy&x=1&y=267")
    # Find all rows in the table
    #sb.cdp.sleep(3)
    rows = sb.cdp.find_elements("tr")
    if rows is None or len(rows) < 13:
        print("Not enough rows found.")
        return []
    coordinates = rows[9].text
    
    rows = rows[12:25]
    # Initialize lists to store player info
    players = []

    # Iterate over each row
    for i in range(len(rows)):
        row = rows[i].text
        print('row:', row)
        row_length = row.split()
        print('row_length', row_length)
        if len(row_length) > 2:
            print('#####################################################')
            #row = str(row)    
            #print('str row:', row)
            print('#####################################################')
            players.append({"Row_Info": coordinates + ' ' + row})
                
    print("Players: ",players)    
    return players

def find_inactive_players_info(sb):
    #driver.get("https://uni4.2moons.cu/game.php?page=galaxy&x=1&y=267")
    # Find all rows in the table
    #sb.cdp.sleep(3)
    rows = sb.find_elements("//table[@class='striped']/tbody/tr")
    
    # Initialize lists to store player info
    inactive_players = []

    # Iterate over each row
    for row in rows:
        # Check if the row contains inactive player info
        if "galaxy-username-inactive" in row.cdp.get_attribute("galaxy-username-inactive", "innerHTML"):
            # Extracting player name, planet name, and position
            columns = row.find_elements("./td")
            player_name = columns[5].cdp.get_text("galaxy-username-inactive")
            planet_name = columns[1].cdp.get_attribute("a", "data-tooltip-content").split("<th colspan='3'>")[1].split(" [")[0].strip()
            position = columns[0].text.strip()
            spy = columns[7].cdp.find_element("fa-eye-slash")
            # Add player info to the list
            inactive_players.append({"Position": position, "Planet Name": planet_name, "Player Name": player_name})
            sb.cdp.gui_hover_and_click(spy, spy)
            sb.cdp.sleep(1)
    print("Inactive Players: ",inactive_players)    
    return inactive_players

#Add player info to the csv
def add_player_info(player_dict):
    try:
        with open('players_info.csv', 'r') as file:
            reader = csv.reader(file)
            existing_players = {row[0]: row[1:] for row in reader}
    except FileNotFoundError:
        existing_players = {}

    with open('players_info.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        for name, coords in player_dict.items():
            if name not in existing_players:
                writer.writerow([name] + coords)
            else:
                if not existing_players[name]:
                    writer.writerow([name] + coords)

    print("Player information updated successfully.")

def exploreUniverse1(sb):
    # Create a dictionary to store the galaxy map
    galaxyMap = {}

    # Loop through all the selected galaxies from Solar System 1 to Solar System 400
    for solar_system in range(1, 401):
        # Get the galaxy page
        sb.cdp.get(f"https://ogame.org/game/index.php?page=galaxy&session={sb.session_id}&galaxy={solar_system}")

        # Wait for the page to load
        #WebDriverWait(sb, 10).until(ec.presence_of_element_located((By.ID, "galaxyContent")))

        # Get all the players in the galaxy
        players = sb.cdp.find_elements("#galaxyContent .playername")

        # Loop through all the players in the galaxy
        for player in players:
            # Get the player's name
            player_name = player.text

            # Get the player's planet
            player_planet = player.cdp.find_element("./../..").get_text("planet-name")

            # Add the player's name and planet to the galaxy map
            galaxyMap[player_name] = {"Planet": f"{solar_system}:{player_planet}"}

    # Create a list of dictionaries with the name of the player and the information of all the planets
    player_planets = []
    for player_name, planet_info in galaxyMap.items():
        player_planets.append({"Player": player_name, "Planet 1": planet_info["Planet"]})

    # Export the data to a CSV file
    with open("galaxy_map.csv", "w", newline="") as csvfile:
        fieldnames = ["Position", "Planet Name", "Player Name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(player_planets)

def spyPlanet(sb):
    # Get all the planets in the solar system
    planets = sb.find_elements("#planetList .smallplanet")

    # Loop through all the planets
    for planet in planets:
        # Get the planet ID
        planet_id = planet.get_attribute("id")

        # Check if there are available spy slots
        if checkSpySlots(sb, planet_id):
            # Spy on the planet
            spyPlanet(sb, planet_id)
        else:
            # Wait 60 seconds
            sb.cdp.sleep(60)

def attackPlanet(sb, planets):
    # Loop through all the planets
    for planet in planets:
        # Check if there are available attack slots
        if checkAttackSlots(sb):
            # Send an attack
            sendAttack(sb, planet)
        else:
            # Wait 60 seconds
            sb.cdp.sleep(60)

def checkAttackSlots(sb):
    pass

def sendAttack(sb):
    pass

def checkSpySlots(sb):
    pass

def exploreTheUniverse(sb):
    galaxy_number = 0
    system_number = 1
    galaxy_button = '/html/body/div[4]/div[3]/a[8]'
    checkLogin(sb)
    try:
        was_q_pressed = False
        players_info = []  # Initialize players_info before the loop
        #url_galaxy = "http://srv220118-206152.vps.etecsa.cu/game.php?page=galaxy"
        sb.cdp.click(galaxy_button)
        sb.sleep(4)
        while not was_q_pressed:
            for _ in range(3):  # Scan galaxies 1 to 3
                galaxy_number += 1
                print(f"Start scanning!")
                sb.cdp.type('/html/body/div[5]/div/div/div[2]/form/div/span[1]/input[2]','e')
                print(f"Scanning galaxy {galaxy_number}")
                sb.cdp.mouse_click('/html/body/div[5]/div/div/div[2]/form/div/span[2]/input[3]')
                sb.cdp.type('/html/body/div[5]/div/div/div[2]/form/div/span[2]/input[2]','e')
                print("Scanning systems")
                #sb.cdp.click('/html/body/div[5]/div/div/div[2]/form/div/span[2]/input[3]') 
                print("Now galaxy 1 and system 1")
                if not was_q_pressed:
                    for _ in range(400):  # Scan systems 1 to 400
                        system_number += 1
                        sb.cdp.mouse_click('/html/body/div[5]/div/div/div[2]/form/div/span[2]/input[3]')
                        print(f"Clicking on system {system_number}")
                        sb.cdp.sleep(RANDOM_SLEEP)
                        # Add code to scan the current planet and gather information
                        info = find_players_info(sb, galaxy_number, system_number)  # Assuming this function returns a list of dicts
                        players_info.extend(info)  # Collect all player info
                        
                        if keyboard.is_pressed("`"):
                            print(" ` pressed, ending loop")
                            was_q_pressed = True
                            break
                if was_q_pressed:
                    break
            print(f"Player`s info: ", players_info)
            # Moved CSV writing inside the loop but after breaking condition check
            csv_file = "players_info.csv"
            with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
                fieldnames = ["Row_Info"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(players_info)
                print(f"Player's planets data exported to {csv_file}")

    except Exception as e:
        print(f'An error occurred: {e}')
        csv_file = "players_info.csv"
        with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
            fieldnames = ["Row_Info"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(players_info)
            print(f"Player's planets data exported to {csv_file}")
        print('Try again...')

#OpenAI code:
def update_players_info(players_dict):
    # Define the CSV file name
    csv_file = 'players_info.csv'

    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        # Create the file with headers if it does not exist
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'coordinates'])  # Add any additional columns if needed

    # Read existing players and their coordinates into a dictionary
    existing_players = {}
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            coordinates = row['coordinates'].split(';')
            existing_players[name] = coordinates

    # Update the existing players information with the new data
    for player_name, new_coordinate in players_dict.items():
        if player_name in existing_players:
            if new_coordinate not in existing_players[player_name]:
                existing_players[player_name].append(new_coordinate)
        else:
            existing_players[player_name] = [new_coordinate]

    # Write the updated player information back to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'coordinates'])
        for player_name, coordinates in existing_players.items():
            writer.writerow([player_name, ';'.join(coordinates)])

def exploreUniverse(sb):
    try:
        was_q_pressed = False
        while not was_q_pressed:
            for galaxy in range(1, 3):  # Scan galaxies 1 to 9
                if not was_q_pressed:
                    for system in range(1, 400):  # Scan systems 1 to 499
                        #for planet in range(1, 15):  # Scan planets 1 to 15
                        url = f"https://xnovawop.com//game.php?page=galaxy&x={galaxy}&y={system}"
                        sb.cdp.get(url)
                        sb.cdp.sleep(1)
                        # Add code to scan the current planet and gather information
                        players_info = find_inactive_players_info(sb)
                        # Export data to CSV file
                        sb.cdp.sleep(1)
                        if keyboard.is_pressed("`"): 
                            print(" ` pressed, ending loop")
                            was_q_pressed = True
                            # csv_file = "inactive_players_info.csv"
                            # with open(csv_file, mode='w', newline='') as file:
                            #     fieldnames = ["Position", "Planet Name", "Player Name"]
                            #     writer = csv.DictWriter(file, fieldnames=fieldnames)
                            #     writer.writeheader()
                            #     writer.writerows(players_info)
                            #     print(f"Player's planets data exported to {csv_file}")
                            break
                    csv_file = "inactive_players_info.csv"
                    with open(csv_file, mode='w', newline='') as file:
                        fieldnames = ["Position", "Planet Name", "Player Name"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(players_info)

                    print(f"Player's planets data exported to {csv_file}")
                else:
                    break
    except:
        print('Algo salio mal al explorar el universo!')
        print('Try again...')
        exploreUniverse(sb)
        
def exploreUniverse2(sb):
    player_planets = []  # List to store player's planets information
    for galaxy in range(1, 10):  # Scan galaxies 1 to 9
        for system in range(1, 400):  # Scan systems 1 to 499
            for planet in range(1, 15):  # Scan planets 1 to 15
                url = f"https://xnovawop.com//game.php?page=galaxy&x={galaxy}&y={system}"
                sb.cdp.get(url)
                sb.cdp.sleep(2)
                # Extract planet information
                planet_name = sb.cdp.get_text("planetName")
                player_name = sb.cdp.get_text("status_abbr_ally")
                player_rank = sb.cdp.get_text("rank")
                player_points = sb.cdp.get_text("score")

                # Add planet information to the list
                player_planets.append({
                    "Galaxy": galaxy,
                    "System": system,
                    "Planet Name": planet_name,
                    "Player Name": player_name,
                    "Player Rank": player_rank,
                    "Player Points": player_points
                })

    # Export data to CSV file
    csv_file = "player_planets.csv"
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["Galaxy", "System", "Planet Name", "Player Name", "Player Rank", "Player Points"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for planet_info in player_planets:
            writer.writerow(planet_info)

    print(f"Player's planets data exported to {csv_file}")

def checkEmpireResource():
    # Go to empire page and get total amount of metal, crystal, deuterium
    total_metal = get_total_metal()
    total_crystal = get_total_crystal()
    total_deuterium = get_total_deuterium()
    # Get the lowest level building among MetalMine, CrystalMine, DeuteriumSyntetiser, RobotsFactory, Hangar
    lowest_level_building = get_lowest_building_level()
    # Loop through all planets and send resources to the planet with the lowest level building
    for planet in get_all_planets():
        if planet.buildings[lowest_level_building] < 10:  # Assuming level 10 is the lowest level
            send_resources(planet, lowest_level_building, total_metal, total_crystal, total_deuterium)

# Helper functions
def get_total_metal():
    # Implementation to get total metal
    pass

def get_total_crystal():
    # Implementation to get total crystal
    pass

def get_total_deuterium():
    # Implementation to get total deuterium
    pass

def get_lowest_building_level():
    # Implementation to get the lowest level building
    pass

def get_all_planets():
    # Implementation to get all planets
    pass

def send_resources(planet, building, total_metal, total_crystal, total_deuterium):
    # Implementation to send resources from all planets to the planet with the lowest level building
    pass

def main(SB):
    with SB(uc=True,test=True) as sb:
        # realistic_browser_history(sb)
        # antibot_detection(sb)
        # browser_scan(sb)
        # fingerprint(sb)
        # checkLogin(sb)
        login(sb)
        while True:
            user_input  = input("Que quieres hacer: \n 0. send Expeditions! \n 1. Explore! \n 2. Explore the Universe! \n 3. Exit \n")
            try:
                number = int(user_input)
            except ValueError:
                print("Opción inválida. Inténtalo de nuevo.")
                continue
            if number == 0:
                while True:
                    checkAttack(sb, TOKEN, CHAT_ID)
                    #sendExpeditions(sb)
                    checkLogin(sb)
                    sb.cdp.sleep(54)
                    print('Press ` if want exit the send exploration menu!')
                    sb.cdp.sleep(3)
                    if keyboard.is_pressed("`"): #This key are before the 1 above the Tab
                        print(" ` pressed, ending loop")
                        break
            elif number == 1:
                while True:
                    inactive_players_info = find_inactive_players_info(sb)
                    print(inactive_players_info)
                    if keyboard.is_pressed("`"):#This key are before the 1 above the Tab
                        print(" ` pressed, ending loop")
                        break
            elif number == 2:
                while True:
                    checkAttack(sb, TOKEN, CHAT_ID)
                    exploreTheUniverse(sb)
                    break
            elif number == 3:
                inactive_players_info = find_inactive_players_info(sb)
                update_players_info(inactive_players_info)
                sb.cdp.quit()
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")
                
main(SB)
