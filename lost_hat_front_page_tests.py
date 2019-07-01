import unittest
from selenium import webdriver

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
            expected_min_height = 300
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

