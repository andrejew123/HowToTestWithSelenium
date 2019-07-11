import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener

class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.url_base = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.url_base + 'login'
        self.sample_product_url = self.url_base + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.art_url = self.url_base + '9-art'
        driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass
