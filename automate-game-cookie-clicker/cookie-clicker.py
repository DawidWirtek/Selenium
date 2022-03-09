import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "This is a place for your chrome driver exe file"
URL = "https://orteil.dashnet.org/experiments/cookie/"
MINUTES = 20

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

cookie_to_click = driver.find_element(By.ID, "cookie")


def store_items():
    items = []
    for item in store:
        if len(item.text) < 1:
            pass
        else:
            names = item.text.split(" - ")[0]
            prices = int(item.text.split(" - ")[1].replace(",", ""))
            items.append([names, prices])
    return items


def what_to_buy():
    things = store_items()
    money = int(my_money.text.replace(",", ""))
    affordable_prices = [thing[1] for thing in things if money >= thing[1]]
    try:
        to_buy = max(affordable_prices)
        staff_to_buy = [thing[0] for thing in things if to_buy == thing[1]]
    except ValueError:
        return "Cursor"

    return staff_to_buy[0]


timeout = time.time() + MINUTES*60
start_time = time.time()
time_to_check = time.time() + 5

while time.time() < timeout:
    my_money = driver.find_element(By.ID, "money")
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    cookie_to_click.click()

    print(my_money.text)

    if time.time() > time_to_check:
        if time.time() < start_time + 2:
            time_to_check = time.time() + 5
        elif time.time() < start_time + 5:
            time_to_check = time.time() + 10
        else:
            time_to_check = time.time() + 15

        item_to_buy = what_to_buy()
        item = driver.find_element(By.ID, f"buy{item_to_buy}")
        item.click()

