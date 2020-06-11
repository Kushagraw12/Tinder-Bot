from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def fb_login(self):
        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(3)
        self.driver.switch_to_window(base_window)
        sleep(5)
        allow = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow.click()
        accept_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_btn.click()
        not_in = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        not_in.click()
        sleep(5)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)
        op = bot.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div/div[3]/span/button')
        op.click()
        # self.fb_login()
        try:
            self.fb_login()
        except Exception:
            sleep(0.5)
            cross_popup = bot.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[2]/button')
            cross_popup.click()
            login_btn = bot.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_btn.click()
            self.fb_login()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        sleep(0.5)

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):

        t = 0
        while t < 10:
            try:
                sleep(1)
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
            t += 1

    def close_popup(self):
        popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
bot.dislike()
