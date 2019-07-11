import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener

class SmokeTestForSearrchBox(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.xpath_search_box = '//*[@class = "ui-autocomplete-input"]'
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    def test_smoke_search_box(self):
        driver= self.ef_driver
        driver.get(self.base_url)
        search_phase = 'mug'
        expected_value = 0
        search_box = driver.find_element_by_xpath(self.xpath_search_box)
        search_box.send_keys(search_phase)
        search_box.send_keys(Keys.ENTER)
        mugs_products = driver.find_elements_by_xpath('//*[contains(@class, "product-miniature")]')
        self.assertLess(expected_value, len(mugs_products), f'Counter of mugs differ than expected for page {driver.current_url}')
        time.sleep(2)

    def test_sanity_search_box(self):
        # driver = self.driver
        self.ef_driver.get(self.base_url)
        search_box = self.ef_driver.find_element_by_xpath('//*[@name="s"]')
        search_box.send_keys('Hummingbird')
        search_box.send_keys(Keys.ENTER)
        tshirt_product = self.ef_driver.find_elements_by_xpath('//*[@class="product-miniature js-product-miniature"]')
        found_elements = 0
        for element in tshirt_product:
            if 'Hummingbird' in element.text:
                found_elements += 1
        self.assertEqual(5, found_elements, f'We expect 1 and actual number of found element item is 1')