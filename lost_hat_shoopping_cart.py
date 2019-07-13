from helpers import operational_helpers as oh
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatShoppingCart(BaseTestClass):
    @classmethod
    def setUp(self):
        super().setUp()
        self.ef_driver.implicitly_wait(10)

    @screenshot_decorator
    def test_add_mountain_fox(self):
        xpath_Mountain_fox = '//*[@ src = "https://autodemo.testoneo.com/15-home_default/mountain-fox-vector-graphics.jpg"]'
        xpath_Mountain_fox_adding_to_cart = '//* [@class = "btn btn-primary add-to-cart"]'
        xpath_modal_element = '//*[@id = "myModalLabel"]'
        expected_modal_element_text = 'Product successfully added to your shopping cart'
        driver = self.ef_driver
        driver.get(self.art_url)
        mountain_fox_element = driver.find_element_by_xpath(xpath_Mountain_fox)
        mountain_fox_element.click()
        add_button_element = driver.find_element_by_xpath(xpath_Mountain_fox_adding_to_cart)
        add_button_element.click()
        confirmation_modal_element = oh.visibility_of_element_wait(driver, xpath_modal_element)
        self.assertIn(
            expected_modal_element_text,
            confirmation_modal_element.text,
            f'Expected text differ than acctual for page {driver.current_url} and in {confirmation_modal_element.text}'
        )