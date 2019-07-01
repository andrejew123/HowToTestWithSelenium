import unittest
from selenium import webdriver
from helpers import functional_helpers as fh

class LostHatLoginPageTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')

    def test_checkingHeader(self):
        driver = self.driver
        driver.get(self.login_url)
        xpath = '//*[@class = "page-header"]/h1'
        expected_text = 'Log in to your account'
        self.assert_element_text(driver, xpath, expected_text)

    def test_login_to_my_account(self):
        user_name = 'i.andrejewicz@gmail.com'
        user_password = 'Hefalumpy89'
        driver = self.driver
        driver.get(self.login_url)
        xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        expected_text = 'Iwona Andrejewicz'
        fh.user_login(driver, user_name, user_password)
        self.assert_element_text(driver, xpath, expected_text)

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

    def test_login_failed(self):
        fake_user_name = 'iquqwieu@gmail.com'
        fake_user_password = "blablabla"
        xpath = '//*[@ class = "alert alert-danger"]'
        expected_text = 'Authentication failed.'
        driver = self.driver
        driver.get(self.login_url)
        fh.user_login(driver, fake_user_name, fake_user_password)
        self.assert_element_text(driver, xpath, expected_text)

    # def user_login(self, driver, user_email, user_password):
    #     login_input_element = driver.find_element_by_xpath('//*[@type ="email"]')
    #     login_input_element.send_keys(user_email)
    #
    #     login_input_element = driver.find_element_by_xpath('//*[@type = "password"]')
    #     login_input_element.send_keys(user_password)
    #
    #     submmit_button = driver.find_element_by_xpath('//*[@ id = "submit-login"]')
    #     submmit_button.click()

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

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
    # pass
