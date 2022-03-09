import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\Programy\Selenium\chromedriver.exe"
TWITTER_EMAIL = "dawiddawid1811@gmail.com"
TWITTER_PASSWORD = "knt6x6SJhH6HZXy"
TWITTER_USERNAME = "Dawid20342371"
TWITTER_URL = "https://twitter.com/home"
INTERNET_SPEED_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.current_up = 0
        self.current_down = 0

    def get_internet_speed(self):
        self.driver.get(url=INTERNET_SPEED_URL)
        self.driver.maximize_window()
        accept_cookie = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        accept_cookie.click()
        get_internet_speed = self.driver.find_element(By.CSS_SELECTOR, ".start-button a .start-text")
        get_internet_speed.click()
        time.sleep(80)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.current_down = download_speed.text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.current_up = upload_speed.text

    def log_into_twitter(self):
        self.driver.switch_to.new_window('tab')
        self.driver.get(TWITTER_URL)

        time.sleep(3)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                      '/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        go_to_username_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div'
                                                           '/div/div[2]/div[2]/div[1]/div/div/div[6]')
        time.sleep(3)
        go_to_username_button.click()
        time.sleep(3)

        user_name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                       '/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div'
                                                       '/input')
        user_name.send_keys(TWITTER_USERNAME)

        go_to_password_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                                   'div[2]/div/div/div[2]/div[2]/div[2]/div')
        go_to_password_button.click()
        time.sleep(3)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                                      '/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/'
                                                      'div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div'
                                                           '/div/div[2]/div[2]/div[2]/div/div[1]')
        log_in_button.click()
        time.sleep(3)

        all_cookies = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]')
        all_cookies.click()
        time.sleep(2)
        print(f"Current download {self.current_down}\n")
        print(f"Current upload {self.current_up}")

    def tweet_at_provider(self):
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]'
                                                   '/div[3]/a')
        tweet.click()

        message_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                         '/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/'
                                                         'div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/'
                                                         'div/div[2]/div')
        message_box.click()
        message_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.current_down}down / "
                              f"{self.current_up}up when I pay for {self.down}down / {self.up}up?")

        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                          'div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]'
                                                          '/div/div/div[2]/div[4]')
        tweet_button.click()


internet_bot = InternetSpeedTwitterBot()
internet_bot.get_internet_speed()
internet_bot.log_into_twitter()
internet_bot.tweet_at_provider()
