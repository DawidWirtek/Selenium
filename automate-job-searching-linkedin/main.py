import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN = "This is a place for your login"
PASSWORD = "This is a place for your password"
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=105076658&keywords=python%20developer&location=Warsaw%2C%20Mazowieckie%2C%20Poland"
CHROME_PATH = "This is a place for your chrome driver path exe file"

driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.get(url=URL)
driver.maximize_window()

cookies = driver.find_element(By.XPATH, '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
cookies.click()

log_in_link = driver.find_element(By.LINK_TEXT, "Zaloguj się")
log_in_link.click()

username = driver.find_element(By.ID, "username")
username.send_keys(LOGIN)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
log_in = driver.find_element(By.CLASS_NAME, "login__form_action_container")
log_in.click()
time.sleep(3)

link = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results__list li div div div .full-width a")
link.click()

save = driver.find_element(By.CSS_SELECTOR, ".display-flex .jobs-save-button")
save.click()
