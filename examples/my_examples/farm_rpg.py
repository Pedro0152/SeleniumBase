from seleniumbase import SB
from datetime import datetime
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
HOME = 'https://farmrpg.com/index.php#!/index.php'
SELL_UNLOCKS = 'a[class="button btnorange sellallbtn"]'
SELL_CROPS = 'a[class="button btngreenalt sellallcropsbtn"]'
STORE = 'https://farmrpg.com/index.php#!/store.php'
STOREHOUSE = 'https://farmrpg.com/index.php#!/storehouse.php?id=767753'
DO_SOME_WORK = 'div:contains("Do some Work")'

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
SMALL_CAVE = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[2]/a/div/div[2]'
SMALL_SPRING = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[3]/a/div/div[2]'
HIGHLAND_HILLS = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[4]/a/div/div[2]'
CANE_POLE_RIDGE = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[5]/a/div/div[2]'
MISTY_FOREST = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[6]/a/div/div[2]'
BLACK_ROCK_CANYON = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[7]/a/div/div[2]'
MOUNT_BANON = '/html/body/div[3]/div[3]/div[2]/div[2]/div/div/div[4]/div/div/ul/li[8]/a/div/div[2]'

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

def daily_action(sb, ):
    now = datetime.now()
    if now.hour < 5:
      try:
        increase_max_inventory(sb)
      except:
        print("Daily Action Fail!")

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
        sb.cdp.sleep(2)
        sb.cdp.click(seeds)
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

def increase_max_inventory(sb):
    try:
        sb.cdp.open(STOREHOUSE)
        sb.cdp.refresh()
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.mouse_click(DO_SOME_WORK)
        sb.cdp.sleep(RANDOM_SLEEP)
        sb.cdp.mouse_click(YES)
        print("Max Inventory Increased")
    except Exception as e:
        print('Max Inventory Fail', e)

def go_to_explore_area(sb, explore_area=None):
    sb.cdp.open(HOME)
    sb.cdp.refresh()
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.open(EXPLORE_THE_AREA)
    sb.cdp.refresh()
    sb.cdp.sleep(RANDOM_SLEEP)
    sb.cdp.mouse_click(CANE_POLE_RIDGE)
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
        daily_action(sb)
        farm(sb)
        sell_crop(sb)
        buy_crop(sb, CORN_SEEDS)
        go_to_explore_area(sb, SMALL_SPRING)
        spend_stamina(sb)
        harvest(sb)
        message = 'Farm RPG Github Action Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())
        # send_warning_voice_call(sb)

main(SB)
