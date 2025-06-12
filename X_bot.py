PROMISED_DOWN = 1550
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\\Users\\sshuh\\Downloads\\chromedriver_win32\\chromedriver.exe"
TWITTER_EMAIL_OR_USERNAME = ""
TWITTER_PASSWORD = ""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedXBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
        # chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        self.driver.maximize_window()
        # self.driver = webdriver.Chrome(options=chrome_options)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(4)

        accept_button = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[2]/div/div/button")
        accept_button.click()

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(62)

        self.up = self.driver.find_element(By.XPATH,value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.down = self.driver.find_element(By.XPATH,value="/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(9)
        # email = self.driver.find_element(By.XPATH,
        #                                  value='/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')

        email = self.driver.find_element(By.XPATH,
                                         value="//input[@name='text']")
        email.send_keys(TWITTER_EMAIL_OR_USERNAME)

        self.driver.find_element(By.XPATH,value="//button[.//span[text()='Next']]").click()

        time.sleep(3)

        try:
            password = self.driver.find_element(By.XPATH,
                                                value="//input[@name='password']")

            password.send_keys(TWITTER_PASSWORD)
            time.sleep(2)

            self.driver.find_element(By.XPATH,value="//button[@data-testid='LoginForm_Login_Button']").click()
            time.sleep(5)
        except Exception:
            username_tag = self.driver.find_element(By.XPATH,value="//input[@data-testid='ocfEnterTextTextInput']")
            username_tag.send_keys("malabarheaven")

            self.driver.find_element(By.XPATH,value="//button[@data-testid='ocfEnterTextNextButton']").click()

            password = self.driver.find_element(By.XPATH,
                                                value="//input[@type='password' and @autocomplete='current-password']")

            password.send_keys(TWITTER_PASSWORD)

            login_button_tag = self.driver.find_element(By.XPATH,value="//button[@data-testid='LoginForm_Login_Button']")
            login_button_tag.click()

        time.sleep(12)
        tweet_box = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_box.send_keys(tweet)
        time.sleep(8)

        tweet_button = self.driver.find_element(By.XPATH, "//button[@data-testid='tweetButtonInline']")
        tweet_button.click()

        time.sleep(3)
        self.driver.quit()





bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.tweet_at_provider()
