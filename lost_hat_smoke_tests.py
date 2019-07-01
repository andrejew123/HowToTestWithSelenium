import unittest
from selenium import webdriver


class LostHatSmokeTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
        self.base_url = 'https://autodemo.testoneo.com/en/'

    @classmethod
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_main_webside(self):
        expected_title = "Lost Hat"
        self.assert_title(self.base_url, expected_title)

    def test_art_product(self):
        url = 'https://autodemo.testoneo.com/en/9-art'
        expected_title = "Art"
        self.assert_title(url, expected_title)

    def test_cloths_product(self):
        url = "https://autodemo.testoneo.com/en/3-clothes"
        expected_title = "Clothes"
        self.assert_title(url, expected_title)

    def test_accessories_product(self):
        url = "https://autodemo.testoneo.com/en/6-accessories"
        expected_title = "Accessories"
        self.assert_title(url, expected_title)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title, f'Result differ than expected for page {url}')

