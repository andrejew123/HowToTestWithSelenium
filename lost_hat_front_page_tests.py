from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatFrontPAgeTests(BaseTestClass):

    @screenshot_decorator
    def test_slide_presentation(self):
        driver = self.ef_driver
        driver.get(self.url_base)

    @screenshot_decorator
    def test_slider_minimum_size(self):
            expected_min_height = 300
            expected_min_width = 600
            driver = self.ef_driver
            slider_xpath = '//*[@ id  = "carousel"]'
            driver.get(self.url_base)
            slider_element = driver.find_element_by_xpath(slider_xpath)
            actual_slider_height = slider_element.size['height']
            actual_slider_width = slider_element.size['width']
            with self.subTest('Element heights'):
                self.assertLess(expected_min_height, actual_slider_height,
                                f'Element height found by xpath {slider_xpath} on page {driver.current_url} is smaller\ '
                                f'then expected {expected_min_height}')
            with self.subTest('Element width'):
                self.assertLess(expected_min_width, actual_slider_width,
                                f'Element width found bby xpatf {slider_xpath} on page {driver.current_url}is smaller\ '
                                f' then expected {expected_min_width}')

            sliders_elements = driver.find_elements_by_xpath('//*[contains(@ class,"carousel-item")]')
            actual_number_of_sliders = len(sliders_elements)
            self.assertEqual(3, actual_number_of_sliders,
                             f'Expected number of sliders differ from actual for page {driver.current_url}')

    @screenshot_decorator
    def test_sliders_title_text(self, ):
        driver = self.ef_driver
        driver.get(self.url_base)
        sliders_titles_xpath = driver.find_elements_by_xpath(
            '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]')
        for title_element in sliders_titles_xpath:
            with self.subTest(title_element):
                title_element_text = title_element.get_attribute('textContent')
                title_element_text_lower = title_element_text.lower()
                print(title_element_text_lower)
                self.assertIn("sample", title_element_text_lower,
                              f'Slides does not contain text for page {driver.current_url} ')

    @screenshot_decorator
    def test_number_of_featured_products(self):
        driver = self.ef_driver
        driver.get(self.url_base)
        product_miniature_xpath = driver.find_elements_by_xpath(
            '//*[@class = "product-miniature js-product-miniature"]')
        expected_number_of_product_on_page = 8
        self.assertEqual(expected_number_of_product_on_page, len(product_miniature_xpath),
                         f'Expected number of product differ then expected for page {driver.current_url}')

    @screenshot_decorator
    def test_pln_in_price(self):
        driver = self.ef_driver
        driver.get(self.url_base)
        price_element = driver.find_elements_by_xpath('//*[@class = "price"]')
        for element in price_element:
            price_element_text = element.get_attribute("textContent")
            with self.subTest(price_element_text):
                self.assertIn("PLN", price_element_text, f'Price of product is not in PLN for {element}')

