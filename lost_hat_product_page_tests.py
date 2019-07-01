import unittest
from selenium import  webdriver
from helpers import functional_helpers as fh

class LostHatProductPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')


    def test_checking_tshirt_name(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        xpath = '//*[@ class = "h1"]'
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(driver, xpath, expected_text)

    def test_check_product_price(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        xpath = '//*[contains(text(), "PLN23.52")]'
        expected_text = 'PLN23.52'
        self.assert_element_text(driver, xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver: ebdrive instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected result differ from actual on page {driver.current_url}')

    @classmethod
    def tearDown(self):
        self.driver.quit()