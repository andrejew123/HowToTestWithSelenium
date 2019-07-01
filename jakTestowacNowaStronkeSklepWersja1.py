import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class MainTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
    # pass

    def test_checkingHeader(self):
        driver = self.driver
        driver.get(self.login_url)
        title_my_account = driver.find_element_by_xpath('//*[@class = "page-header"]/h1')
        self.assertEqual('Log in to your account', title_my_account.text, 'Title is not as expected')

    def test_login_to_my_account(self):
        user_name = 'i.andrejewicz@gmail.com'
        user_password = 'Hefalumpy89'
        driver = self.driver
        driver.get(self.login_url)

        # self.user_login(driver, user_name, user_password)
        credentials_loin = driver.find_element_by_xpath('//*[@type ="email"]')
        credentials_loin.send_keys(user_name)
        credentials_password = driver.find_element_by_xpath('//*[@type = "password"]')
        credentials_password.send_keys(user_password)
        submmit_button = driver.find_element_by_xpath('//*[@ id = "submit-login"]')
        submmit_button.click()
        check_if_my_account = driver.find_element_by_xpath('//a[@class="account"]/*[@class="hidden-sm-down"]')
        self.assertEqual('Iwona Andrejewicz', check_if_my_account.text,
                         f' You didnot loggin in, you aree in:  {check_if_my_account.text}')
        time.sleep(3)

    def test_checking_tshirt_name(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        check_tshirt_name = driver.find_element_by_xpath('//*[@ class = "h1"]')
        self.assertEqual('HUMMINGBIRD PRINTED T-SHIRT', check_tshirt_name.text,
                         f'Fake name of thisrt, please correck it')
    def test_check_product_price(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        check_product_price = driver.find_element_by_xpath('//*[contains(text(), "PLN23.52")]')
        self.assertEqual('PLN23.52', check_product_price.text, f'Checked price differ than expected')

    def test_login_failed(self):
        fake_user_name = 'iquqwieu@gmail.com'
        fake_user_password = "blablabla"
        driver = self.driver
        driver.get(self.login_url)
        # self.user_login(driver, fake_user_name, fake_user_password)
        credentials_login = driver.find_element_by_xpath('//*[@type ="email"]')
        credentials_login.send_keys(fake_user_name)
        credentials_password = driver.find_element_by_xpath('//*[@type = "password"]')
        credentials_password.send_keys(fake_user_password)
        submmit_button = driver.find_element_by_xpath('//*[@ id = "submit-login"]')
        submmit_button.click()
        check_autentication_failed = driver.find_element_by_xpath('//*[@ class = "alert alert-danger"]')
        check_autentication_failed_text = check_autentication_failed.text
        self.assertEqual('Authentication failed.', check_autentication_failed_text,
                         f'Expected text differ from actual for page {self.login_url}')

    # def user_login(self, driver, user_email, user_password):
    #     login_input_element = driver.find_element_by_xpath('//*[@type ="email"]')
    #     login_input_element.send_keys(user_email)
    #
    #     login_input_element = driver.find_element_by_xpath('//*[@type = "password"]')
    #     login_input_element.send_keys(user_password)
    #
    #     submmit_button = driver.find_element_by_xpath('//*[@ id = "submit-login"]')
    #     submmit_button.click()

    @classmethod
    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
    # pass
