import unittest
# from selenium import webdriver
# from helpers.wrappers import screenshot_decorator
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
from helpers.wrappers import screenshot_decorator
from helpers.screenshot_listener import ScreenshotListener

class LostHatSmokeTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass
    @classmethod
    def setUpClass(self):
        # self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
        # self.base_url = 'https://autodemo.testoneo.com/en/'
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\Users\andrejew\PycharmProjects\chromedriver")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    @screenshot_decorator
    def test_base_page_title(self):
        expected_title = "Lost Hat"
        self.assert_title(self.base_url, expected_title)

    @screenshot_decorator
    def test_product_clothes_page_title(self):
        url = "https://autodemo.testoneo.com/en/3-clothes"
        expected_title = "Clothes"
        self.assert_title(url, expected_title)

    @screenshot_decorator
    def test_accessories_product(self):
        url = "https://autodemo.testoneo.com/en/6-accessories"
        expected_title = "Accessories"
        self.assert_title(url, expected_title)

    @screenshot_decorator
    def test_art_product(self):
        url = 'https://autodemo.testoneo.com/en/9-art'
        expected_title = "Art"
        self.assert_title(url, expected_title)

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    @screenshot_decorator
    def test_smoke_search_on_main_page(self):
        search_phase = 'mug'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        minimum_expected_elements = 5
        self.ef_driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element_by_xpath(search_input_xpath)
        search_input_element.send_keys(search_phase)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.ef_driver.find_elements_by_xpath(result_element_xpath)
        self.assertGreaterEqual(len(result_elements), minimum_expected_elements,
                                f'Actual number of elements found: \
                                {len(result_elements)}; expected was {minimum_expected_elements} or more')

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title, f'Result differ than expected for page {url}')

