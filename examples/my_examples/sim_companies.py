from datetime import datetime, timezone, timedelta
from github import Auth, Github
from seleniumbase import SB
import subprocess
import requests
import random
import base64
import yaml
import os

URL_OVERVIEW = 'https://www.simcompanies.com/'
URL_MAIN = 'https://www.simcompanies.com/landscape/'
LOGIN = "/html/body/section/div[2]/div/div[2]/div/div[2]/form/div[4]/button"
RANDOM_SLEEP = float(random.randint(100, 200) / 50)

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USERNAME = os.environ["USERNAME_SIM_COMPANIES"]
PASSWORD = os.environ["PASSWORD_SIM_COMPANIES"]
ACTION_TOKEN = os.environ["WORKFLOW_ACTION_TOKEN"]

# Main BUTTONS:
ACCEPT_COOKIE = 'class="css-uyxdsm btn btn-lg btn-secondary"'
WAREHOUSE = "https://www.simcompanies.com/headquarters/warehouse/"
MARKET = "https://www.simcompanies.com/market/resource/1/"
SELL_POWER = "https://www.simcompanies.com/headquarters/warehouse/power/sell/"
UPGRADE = 'button:contains("Upgrade")'
UPGRADE_COST = 'td.css-16vr4dv.evklgu42'

BUILDINGS = [46164635,46210973,46223536,46210975,46084693,46223542,46223589,46167238,46298039]

PRODUCING = '/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]'
UPGRADING = '/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div'

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

def produce_resource(sb, building):
      try:
        sb.cdp.open(f'https://www.simcompanies.com/b/{building}/')
        sb.cdp.sleep(3)
        sb.cdp.click("/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/button[1]")
        sb.cdp.sleep(1)
        sb.cdp.click("/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/form/div/button")
        print("produce_resource!")
      except:
        print("produce_resource fail!")
        pass

def parse_duration_to_seconds(duration_str: str) -> int:
    """
    Calcula los segundos restantes desde ahora (en UTC) hasta una fecha y hora
    específicas indicadas en el string.
    Ejemplo de entrada: 'Finishes at 09/25/25 11:08 PM'
    """
    # --- 1. Limpiar y preparar el string de la fecha ---
    # Quita el texto inicial para quedarnos solo con la fecha y la hora
    try:
        clean_str = duration_str.replace('Finishes at ', '')
    except AttributeError:
        # Si el input no es un string, devuelve 0 para evitar errores
        return 0
    # --- 2. Convertir el string a un objeto de fecha y hora ---
    # '%m/%d/%y %I:%M %p' es el formato para "Mes/Día/Año Hora:Minuto AM/PM"
    try:
        finish_time_naive = datetime.strptime(clean_str, '%m/%d/%y %I:%M %p')
        print(f"Parsed time (naive): {finish_time_naive}")
    except ValueError:
        # Si el formato no coincide, no se puede calcular.
        print(f"Error: El formato de '{duration_str}' no es válido.")
        return 0
    # --- 3. Asignar la zona horaria a la hora de la fábrica ---
    # Asumimos que la hora del juego está en tu zona horaria (Uruguay, UTC-3).
    # ¡IMPORTANTE! Si el juego usa otra zona horaria, debes cambiar timedelta(hours=-3).
    uruguay_tz = timezone(timedelta(hours=-3))
    finish_time_aware = finish_time_naive.replace(tzinfo=uruguay_tz)
    # --- 4. Obtener la hora actual en UTC ---
    # Las GitHub Actions siempre se ejecutan en horario UTC.
    now_utc = datetime.now(timezone.utc)
    # --- 5. Calcular la diferencia y convertir a segundos ---
    time_difference = finish_time_aware - now_utc
    # .total_seconds() devuelve los segundos totales en la diferencia
    remaining_seconds = int(time_difference.total_seconds())
    print(f"Remaining seconds until '{finish_time_aware}' (UTC-3): {remaining_seconds}")
    # Si la fecha ya pasó, los segundos serían negativos. Devolvemos 0 en ese caso.
    return max(600, remaining_seconds)
# --- Ejemplo de uso ---
# Supongamos que la hora actual UTC es 25 de Sep de 2025 a las 06:23 AM
# La hora de la fábrica es a las 11:08 PM en UTC-3, que equivale a las 02:08 AM del 26 de Sep en UTC.

def get_factories_status_and_time(sb):
    """
    # PSEUDOCÓDIGO USADO:
    # Extensión de get_game_state para obtener también los tiempos restantes.
    # Para cada fábrica, obtener su estado (MEJORANDO, PRODUCIENDO) y tiempo_fin_tarea.
    """
    print("Obteniendo estado y tiempos de las fábricas...")
    sb.cdp.open(URL_MAIN)
    sb.cdp.sleep(4)
    factories = []

    for building_id in BUILDINGS:
        try:
            factory_info = {"id": building_id, "status": "LIBRE", "remaining_seconds": 0}
            sb.cdp.open(f'https://www.simcompanies.com/b/{building_id}/')
            sb.cdp.sleep(3)
            if sb.cdp.is_element_visible("p.mt20"):
                status_text = sb.cdp.find_element("p.mt20").text
                print(f"Building {building_id}: {status_text}")
                factory_info["status"] = "Producing"
                factory_info["remaining_seconds"] = parse_duration_to_seconds(status_text)
            
            factories.append(factory_info)
        except Exception as e:
            print(f"No se pudo obtener info de tiempo para el edificio {building_id}. Error: {e}")      
    return factories

def calculate_and_update_schedule(factories):
    """
    Calcula y actualiza la programación basada en el estado de las fábricas
    """
    upgrading_factories = [f for f in factories if f["status"] == "Upgrading"]
    print('upgrading factories:', upgrading_factories)
    producing_factories = [f for f in factories if f["status"] == "Producing"]
    print('producing factories:', producing_factories)

    target_seconds = 0
    
    if upgrading_factories:
        # Prioridad 1: La que termina de mejorar ANTES
        first_to_finish_upgrade = min(upgrading_factories, key=lambda f: f["remaining_seconds"])
        target_seconds = first_to_finish_upgrade["remaining_seconds"]
        print(f"Próxima ejecución basada en la mejora más próxima: {timedelta(seconds=target_seconds)}")
    elif producing_factories:
        # Prioridad 2: La que tarda MENOS en producir
        shortest_production = min(producing_factories, key=lambda f: f["remaining_seconds"])
        target_seconds = shortest_production["remaining_seconds"]
        print(f"Próxima ejecución basada en la producción más corta: {timedelta(seconds=target_seconds)}")
    else:
        print("No hay fábricas activas. No se cambiará la hora.")
    target_seconds += 60
    # Calcular la hora futura en UTC (GitHub Actions usa UTC)
    now_utc = datetime.now(timezone.utc)
    next_run_time_utc = now_utc + timedelta(seconds=target_seconds)
    # Convertir a formato CRON
    new_cron = f"{next_run_time_utc.minute} {next_run_time_utc.hour} {next_run_time_utc.day} {next_run_time_utc.month} *"
    print(f"Nueva hora CRON calculada (UTC): '{new_cron}'")
    update_workflow_file(new_cron)

def update_workflow_file(cron_expression: str):
    # --- Configuración ---
    REPO_NAME = "Pedro0152/SeleniumBase"
    WORKFLOW_FILE = ".github/workflows/sim_companies_github_action.yml"

    # --- Conexión ---
    g = Github(auth=Auth.Token(ACTION_TOKEN))
    repo = g.get_repo(REPO_NAME)

    # --- Leer workflow ---
    file_content = repo.get_contents(WORKFLOW_FILE)
    decoded_content = base64.b64decode(file_content.content).decode("utf-8")
    decoded_content = decoded_content.replace("\non:", "\n'on':")
    data = yaml.safe_load(decoded_content)

    # --- Actualizar cron ---
    if isinstance(data, dict):
        if "on" in data:
            on_section = data["on"] or {}
            if "schedule" in on_section and isinstance(on_section["schedule"], list) and len(on_section["schedule"]) > 0:
                print(f"Cron actual: {on_section['schedule'][0]['cron']}")
                on_section["schedule"][0]["cron"] = cron_expression
                print(f"Nuevo cron: {cron_expression}")
            else:
                raise ValueError("No se encontró ninguna entrada en schedule.")
        else:
            raise ValueError(f"No se encontró la clave 'on' en el YAML. Claves encontradas: {list(data.keys())}")
    else:
        raise ValueError("El YAML no es un dict.")
    # --- Guardar ---
    new_content = yaml.dump(data, sort_keys=False)
    # --- Commit ---
    repo.update_file(
        path=WORKFLOW_FILE,
        message=f"Update cron to {cron_expression}",
        content=new_content,
        sha=file_content.sha,
    )
    print(f"Cron updated!")

def get_game_state(sb):
    """
    # PSEUDOCÓDIGO USADO:
    # DINERO_ACTUAL = Tu dinero inicial
    # MIS_FABRICAS: Lista de [N_FABRICAS] objetos de tipo Fabrica
    # Para cada fábrica, obtener su nivel y estado ("LIBRE", "PRODUCIENDO", etc.)
    #
    # Esta función escanea la página para obtener todos los datos necesarios para tomar decisiones.
    """
    print("Obteniendo estado actual del juego (dinero y fábricas)...")
    sb.cdp.open(URL_MAIN)
    sb.sleep(4)

    # 1. Obtener dinero actual
    try:
        # ¡DEBES BUSCAR EL SELECTOR CORRECTO PARA TU DINERO!
        money_element = sb.cdp.find_element("div.css-q2xpdd")
        # Limpiar el texto para obtener solo el número (ej: "$1,234.56" -> 1234.56)
        current_money = float(money_element.text.replace('$', '').replace(',', ''))
        print(f"Dinero actual: ${current_money}")   
    except Exception as e:
        print(f"Error al obtener el dinero actual. Usando 0. Error: {e}")
        current_money = 0

    # 2. Obtener estado de las fábricas
    factories = []
    for building_id in BUILDINGS:
        try:
            # Construye el selector para cada edificio usando su ID
            # ¡DEBES BUSCAR EL SELECTOR CORRECTO PARA CADA DATO!
            sb.cdp.open(f'https://www.simcompanies.com/b/{building_id}/')
            sb.cdp.sleep(4)
            # Busca el nivel dentro del elemento del edificio
            level_element = sb.cdp.find_element('div.css-2pg1ps')
            level = int(level_element.text.replace('LEVEL ', ''))
            print(f"Edificio ID {building_id}: Nivel {level}")
            if sb.cdp.is_element_present('p.mt20'): # Selector para edificio ocupado
                status = "OCUPADO"
                upgrade_cost = None
            else:
                sb.cdp.click(UPGRADE)
                sb.cdp.sleep(1)
                upgrade_cost_element = sb.cdp.find_element(UPGRADE_COST)
                print(f"Edificio ID {building_id}: Costo de mejora {upgrade_cost_element.text}")
                upgrade_cost = upgrade_cost_element.text.replace('$', '').replace(',', '')
                print(f"Edificio ID {building_id}: Costo de mejora limpio {upgrade_cost}")
                status = "LIBRE"

            factories.append({
                "id": building_id,
                "level": level,
                "status": status,
                "upgrade_cost": upgrade_cost,
            })
        except Exception as e:
            print(f"No se pudo obtener información para el edificio {building_id}. Error: {e}")
            
    game_state = {
        "money": current_money,
        "factories": factories
    }
    # print(f"Estado obtenido: {game_state}")
    return game_state

def decide_and_act_on_factories(sb, game_state):
    """
    # PSEUDOCÓDIGO USADO:
    # MIENTRAS (hay fábricas libres):
    #     fabrica_a_mejorar = encontrar_fabrica_menor_nivel()
    #     RESERVA_DE_SEGURIDAD = (N_FABRICAS - 1) * costo_max_produccion
    #     SI (puedo mejorar Y es la fábrica correcta):
    #         // Decisión: MEJORAR
    #     SINO:
    #         // Decisión: PRODUCIR
    #
    # Implementa la lógica principal de decisión para cada fábrica libre.
    """
    print("Tomando decisiones para las fábricas libres...")
    factories = game_state["factories"]
    money = game_state["money"]
    
    # Filtrar solo las fábricas que están libres
    free_factories = [f for f in factories if f["status"] == "LIBRE"]
    level_factories = [f["level"] for f in factories]
    if not free_factories:
        print("No hay fábricas libres para asignar tareas.")

    # 1. Encontrar la fábrica de menor nivel como candidata a mejora
    non_max_level_factories = [f for f in factories if f["level"] < 20]
    if not non_max_level_factories:
        print("¡Todas las fábricas están a nivel máximo!")
    
    # 2. Calcular la reserva de seguridad
    # Usamos el costo de producción más alto conocido como una estimación segura
    costo_max_produccion = max(level_factories) * 10_000  # Ejemplo: costo aumenta con el nivel
    free_factories_count = len(free_factories)
    if free_factories_count > 1:
        RESERVA_DE_SEGURIDAD = (free_factories_count) * costo_max_produccion
    else:
        RESERVA_DE_SEGURIDAD = 2 * costo_max_produccion
    print(f"Reserva de seguridad calculada: ${RESERVA_DE_SEGURIDAD}")

    # 3. Iterar sobre las fábricas libres y asignarles tareas
    for factory in free_factories:
        factory_id = factory["id"]
        # Comprobar si esta fábrica es la candidata a ser mejorada
        if factory_id in non_max_level_factories:
            costo_mejora_actual = factory["upgrade_cost"]
            print(f"Evaluando mejora para Edificio ID {factory_id} con costo ${costo_mejora_actual}")    
            # Condición para mejorar
            if money >= (costo_mejora_actual + RESERVA_DE_SEGURIDAD):
                print(f"Decisión para ID {factory_id}: MEJORAR. (Dinero: ${money}, Costo: ${costo_mejora_actual})")
                try:
                    # Lógica para hacer clic en el botón de mejora
                    sb.cdp.open(f"https://www.simcompanies.com/b/{factory_id}")
                    sb.cdp.sleep(2)
                    sb.cdp.click('button:contains("Upgrade")') # ¡DEBES BUSCAR EL SELECTOR CORRECTO!
                    sb.cdp.sleep(1)
                    sb.cdp.click('div.modal-footer > button.btn-primary') # Confirmar la mejora
                    money -= costo_mejora_actual # Actualizar dinero localmente
                    # send_telegram_message(f"✅ Fábrica {factory['id']} puesta a mejorar al nivel {factory['level'] + 1}.")
                except Exception as e:
                    print(f"Falló el intento de mejora para {factory['id']}. Se pondrá a producir. Error: {e}")
                    produce_resource(sb, factory_id)
            else:
                print(f"Decisión para ID {factory['id']}: PRODUCIR. (Fondos insuficientes para mejorar)")
                produce_resource(sb, factory_id)
        else:
            # Si no es la candidata a mejora, siempre produce
            print(f"Decisión para ID {factory['id']}: PRODUCIR.")
            produce_resource(sb, factory_id)

def main(SB):
    with SB(uc=True, headless=False) as sb:
#    update_workflow_file() # Ejemplo: todos los días a medianoche UTC
        login(sb)
        get_resources(sb)
        sell_resources(sb)
        current_state = get_game_state(sb) # Tu función existente
        if current_state["factories"]:
            decide_and_act_on_factories(sb, current_state) # Tu función existente
        else:
            print("No se pudo obtener el estado de las fábricas.")

        # --- NUEVA LÓGICA PARA REPROGRAMAR ---
        # Se ejecuta después de actuar, para programar la siguiente ejecución

        factory_statuses = get_factories_status_and_time(sb)
        if factory_statuses:
            calculate_and_update_schedule(factory_statuses)

        message = 'Sim Companies Done!'
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        print(requests.get(url).json())

main(SB)
