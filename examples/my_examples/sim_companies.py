from seleniumbase import SB
import requests
import random
import os

URL_OVERVIEW = 'https://www.simcompanies.com/'
LOGIN = "/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button"
RANDOM_SLEEP = float(random.randint(100, 200) / 50)

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = os.environ["USERNAME_SIM_COMPANIES"]
PASSWORD = os.environ["PASSWORD_SIM_COMPANIES"]

# Main BUTTONS:
ACCEPT_COOKIE = 'class="css-uyxdsm btn btn-lg btn-secondary"'
WAREHOUSE = "https://www.simcompanies.com/headquarters/warehouse/"
MARKET = "https://www.simcompanies.com/market/resource/1/"
SELL_POWER = "https://www.simcompanies.com/headquarters/warehouse/power/sell/"

def login(sb):
    print("Log in...")
    sb.activate_cdp_mode(URL_OVERVIEW)
    sb.cdp.sleep(6)
    # print("Clicking...")
    # sb.cdp.click('button:contains("Essential Only")')
    # print("Clicked...")
    try:
      sb.cdp.click('a:contains("Sign in")')
    except:
      print("Sign in failed...trying again")
      try:
        sb.cdp.click('a:contains("Iniciar sesión")')
      except:
        print("Iniciar sesión failed")
    print("Signing in...")
    sb.cdp.sleep(4)
    sb.cdp.press_keys('input[name="email"]', 'kresh0152@gmail.com')
    sb.cdp.send_keys('input[name="password"]', 'Warehouse*13\n')
    print("Logged in...")
    sb.cdp.sleep(4)

def get_resources(sb):
    for i in range(1, 12):
        try:
            sb.cdp.click(f'/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div/a[{i}]/div[3]')
            print("Clicked on resources...")
        except:
            print("No resources to click...")
            pass

def sell_resources(sb):
    try:
      print("Selling resources...")
      cheapest_price = get_cheapest_price(sb) - 0.001
      sb.cdp.open('https://www.simcompanies.com/headquarters/warehouse/power/sell/')
      sb.cdp.click('button:contains("All")')
      sb.cdp.send_keys('input[name="price"]', str(cheapest_price) + '\n')
      print("Selled resources at price...", cheapest_price)
      sb.cdp.sleep(3)
    except:
      print("sell_resources Fail!")
      message = 'sell_resources Fail!'
      url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
      print(requests.get(url).json())

def get_cheapest_price(sb):
    try:
      print("Getting cheapest price...")
      sb.cdp.open('https://www.simcompanies.com/market/resource/1/')
      prices = sb.cdp.find_elements('span[class="css-fcl27u"]')
      cheapest_price = prices[0].text
      cheapest_price = float(cheapest_price.replace('$', ''))
      print("Cheapest price...", cheapest_price)
      return cheapest_price
    except:
      print("get_cheapest_price Fail!")

def produce_resource(sb):
    for i in range(1, 12):
      try:
        print("test1")
        sb.cdp.click(f'/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div/a[{i}]')
        print("test2")
        sb.cdp.sleep(5)
        sb.cdp.click("/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/button[1]")
        print("test3")
        sb.cdp.sleep(3)
        sb.cdp.click("/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/button")
        print("produce_resource!")
      except:
        print("produce_resource fail!")
      pass

def main(SB):
    with SB(uc=True) as sb:
        login(sb)
        get_resources(sb)
        sell_resources(sb)
        produce_resource(sb)
        message = 'Sim Companies Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())

main(SB)
