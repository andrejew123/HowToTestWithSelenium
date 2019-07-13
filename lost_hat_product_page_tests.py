from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatProductPage(BaseTestClass):

    @screenshot_decorator
    def test_checking_tshirt_name(self):
        driver = self.ef_driver
        driver.get(self.sample_product_url)
        xpath = '//*[@ class = "h1"]'
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(
            driver,
            xpath,
            expected_text
        )

    @screenshot_decorator
    def test_check_product_price(self):
        driver = self.ef_driver
        driver.get(self.sample_product_url)
        xpath = '//*[contains(text(), "PLN23.52")]'
        expected_text = 'PLN23.52'
        self.assert_element_text(
            driver,
            xpath,
            expected_text
        )

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver: ebdrive instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(
            expected_text,
            element_text,
            f'Expected result differ from actual on page {driver.current_url}'
        )
