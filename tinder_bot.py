from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)

        more_op = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button')
        # sleep(3)
        more_op.click()

        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('kush12092001@gmail.com')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('8800049870vfx9205104557')

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
