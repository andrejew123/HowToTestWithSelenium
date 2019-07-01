from selenium import webdriver
import unittest
from helpers import functional_helpers as fh
from helpers import operational_helpers as oh


class LostHatTests(unittest.TestCase):

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


class LostHatFrontPAgeTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
        self.url_base = 'https://autodemo.testoneo.com/en/'

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_slide_presentation(self):
        driver = self.driver
        driver.get(self.url_base)

    def test_slider_minimum_size(self):
            expected_min_height = 340
            expected_min_width = 600
            driver = self.driver
            slider_xpath = '//*[@ id  = "carousel"]'
            driver.get(self.url_base)
            slider_element = driver.find_element_by_xpath(slider_xpath)
            actual_slider_height = slider_element.size['height']
            actual_slider_width = slider_element.size['width']
            with self.subTest('Element heights'):
                self.assertLess(expected_min_height, actual_slider_height,
                                f'Element height found by xpath {slider_xpath} on page {driver.current_url} is smaller then \
                                expected {expected_min_height}')
            with self.subTest('Element width'):
                self.assertLess(expected_min_width, actual_slider_width,
                                f'Element width found bby xpatf {slider_xpath} on page {driver.current_url}is smaller then \
                                expected {expected_min_width}')

            sliders_elements = driver.find_elements_by_xpath('//*[contains(@ class,"carousel-item")]')
            actual_number_of_sliders = len(sliders_elements)
            self.assertEqual(3, actual_number_of_sliders,
                             f'Expected number of sliders differ from actual for page {driver.current_url}')

    def test_sliders_title_text(self, ):
        driver = self.driver
        driver.get(self.url_base)
        sliders_titles_xpath = driver.find_elements_by_xpath(
            '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]')
        # for title_element in sliders_titles_xpath:
        #     # if (title_element.get_attribute("textContent")).lower() == 'sample':
        #     print(f'Text: {title_element.get_attribute("textContent")}')

        # title_elements_text = title_element.get_attribute("textContent")
        for title_element in sliders_titles_xpath:
            with self.subTest(title_element):
                title_element_text = title_element.get_attribute('textContent')
                title_element_text_lower = title_element_text.lower()
                print(title_element_text_lower)
                self.assertIn("sample", title_element_text_lower,
                              f'Slides does not contain text for page {driver.current_url} ')

    def test_number_of_featured_products(self):
        driver = self.driver
        driver.get(self.url_base)
        product_miniature_xpath = driver.find_elements_by_xpath(
            '//*[@class = "product-miniature js-product-miniature"]')
        expected_number_of_product_on_page = 8
        self.assertEqual(expected_number_of_product_on_page, len(product_miniature_xpath),
                         f'Expected number of product differ then expected for page {driver.current_url}')

