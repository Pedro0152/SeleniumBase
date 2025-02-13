from seleniumbase import SB
import requests
import random
import os

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME_FARM_RPG = os.environ["USERNAME_FARM_RPG"]
PASSWORD_FARM_RPG = os.environ["PASSWORD_FARM_RPG"]

URL_LOGIN ='https://farmrpg.com/index.php#!/login.php'
URL_OVERVIEW = 'https://web.idle-mmo.com/@Kresh'
URL_HASH = 'https://2moons.cu/game.php?page=overview'
LOGIN_BUTTON = '/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button'

RANDOM_SLEEP = random.randint(20,40)/10
RANDOM__EXPLORER_SLEEP = random.randint(8,18)/10

# Options
YES = 'div:contains("Yes")'
NO = 'div:contains("NO")'
OK = 'span:contains("OK")'
READY = 'span:contains("Ready")'

# Login
USERNAME = 'input[name="username"]'
PASSWORD = 'input[name="password"]'
SUBMIT_BUTTON = 'input[type="submit"]'

# Buttons
MY_FARM = 'https://farmrpg.com/index.php#!/xfarm.php?id=767753'
GO_FISHING = 'https://farmrpg.com/index.php#!/fish.php'
GO_INTO_TOWN = 'https://farmrpg.com/index.php#!/town.php'
FARM_SUPPLY = 'https://farmrpg.com/index.php#!/supply.php'
BUY_MORE_SEEDS = 'https://farmrpg.com/index.php#!/store.php?from=farm&id=767753'
EXPLORE_THE_AREA = 'https://farmrpg.com/index.php#!/explore.php'
MARKET = 'https://farmrpg.com/index.php#!/market.php'
HARVEST_ALL_CROPS = 'a[class="button btnorange harvestallbtn"]'
PLANT_ALL_SELECT = 'a[class="button btnblue plantallbtn"]'
BUY_MORE_SEEDS = 'https://farmrpg.com/index.php#!/store.php?from=farm&id=767753'
HOME = 'https://farmrpg.com/index.php#!/index.php'
SELL_UNLOCKS = 'a[class="button btnorange sellallbtn"]'
SELL_CROPS = 'a[class="button btngreenalt sellallcropsbtn"]'
STORE = 'https://farmrpg.com/index.php#!/store.php'

# Seeds
PEPPERS_SEEDS = 'button[data-name="Peppers Seeds"]'
CARROTS_SEEDS = 'button[data-name="Carrot Seeds"]'
PEA_SEEDS = 'button[data-name="Pea Seeds"]'
CUCUMBER_SEEDS = 'button[data-name="Cucumber Seeds"]'
EGGPLANT_SEEDS = 'button[data-name="Eggplant Seeds"]'
RADISH_SEEDS = 'button[data-name="Radish Seeds"]'
ONION_SEEDS = 'button[data-name="Onion Seeds"]'
HOPS_SEEDS = 'button[data-name="Hops Seeds"]'
POTATO_SEEDS = 'button[data-name="Potato Seeds"]'
TOMATO_SEEDS = 'button[data-name="Tomato Seeds"]'
LEEK_SEEDS = 'button[data-name="Leek Seeds"]'
WATERMELON_SEEDS = 'button[data-name="Watermelon Seeds"]'
CORN_SEEDS = 'button[data-name="Corn Seeds"]'
CABBAGE_SEEDS = 'button[data-name="Cabbage Seeds"]'
PINE_SEEDS = 'button[data-name="Pine Seeds"]'

# Explore Area
SMALL_CAVE = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[1]/a/div/div[2]'

def login(sb):
    sb.activate_cdp_mode(URL_LOGIN)
    sb.cdp.sleep(3)
    try:
        sb.cdp.press_keys(USERNAME, USERNAME_FARM_RPG)
        sb.cdp.press_keys(PASSWORD, PASSWORD_FARM_RPG)
        sb.cdp.click(SUBMIT_BUTTON)
        print('login!')
        sb.cdp.sleep(2)
    except Exception as e:
        print('Login fail', e)

def plant_all(sb):
    try:
        sb.cdp.mouse_click(PLANT_ALL_SELECT)
        sb.cdp.sleep(1)
        sb.cdp.mouse_click(YES)
        print('Plant All')
    except Exception as e:
        print('Plant All Fail', e)

def harvest_all(sb):
    try:
        sb.cdp.mouse_click(HARVEST_ALL_CROPS)
        sb.cdp.sleep(1)
        print('Harvest All')
    except Exception as e:
        print('Harvest All Fail', e)

def sell_crop(sb):
    sb.cdp.open(MARKET)
    sb.cdp.refresh()
    try:
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.mouse_click(SELL_UNLOCKS)
        sb.cdp.sleep(1)
        sb.cdp.mouse_click(YES)
        sb.cdp.mouse_click(OK)
        print('Sell Crop')
    except Exception as e:
        print('Sell Crop Fail', e)

def buy_crop(sb, seeds=None):
    sb.cdp.open(STORE)
    sb.cdp.refresh()
    try:
        sb.cdp.mouse_click(seeds)
        sb.cdp.sleep(1)
        sb.cdp.mouse_click(YES)
        sb.cdp.mouse_click(OK)
        print('Buy Crop')
    except Exception as e:
        print('Buy Crop Fail', e)

def farm(sb):
    sb.cdp.open(MY_FARM)
    sb.cdp.refresh()
    sb.cdp.sleep(2)
    harvest_all(sb)
    plant_all(sb)
    sb.cdp.sleep(3)

def go_to_explore_area(sb, explore_area=None):
    sb.cdp.open(HOME)
    sb.cdp.refresh()
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.open(EXPLORE_THE_AREA)
    sb.cdp.refresh()
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.mouse_click(SMALL_CAVE)
    sb.cdp.sleep(RANDOM_SLEEP)

def explore(sb):
    try:
        sb.cdp.mouse_click('div:contains("Continue")')
        sb.cdp.sleep(RANDOM__EXPLORER_SLEEP)
        print('Explore')
    except Exception as e:
        print('Explore Fail', e)

def spend_stamina(sb):
    stm = sb.cdp.get_text('span[id="stamina"]')
    print('stamina: ',stm)
    stamina = int(stm)
    while stamina > 1:
        print('------------')
        explore(sb)
        stamina -= 1
        print('Stamina: ', stamina)
        print('------------')

def harvest_is_ready(sb):
    try:
        sb.cdp.mouse_click(READY)
        print('Harvest is ready')
    except Exception as e:
        print('Harvest is not ready', e)

def harvest(sb):
    if harvest_is_ready(sb):
        harvest_all(sb)
        plant_all(sb)

def main(SB):
    with SB(uc=True,test=True) as sb:
        login(sb)
        farm(sb)
        sell_crop(sb)
        buy_crop(sb, CARROTS_SEEDS)
        go_to_explore_area(sb, SMALL_CAVE)
        spend_stamina(sb)
        harvest(sb)
        message = 'Farm RPG Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
        # send_warning_voice_call(sb)

main(SB)
