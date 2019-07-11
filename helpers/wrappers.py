from selenium import webdriver
from helpers.screenshot_listener import ScreenshotListener
from helpers.screenshot_listener import make_screenshot
from selenium.common.exceptions import TimeoutException

def screenshot_decorator(test_fun):
    def wrapper(self):
        try:
            return test_fun(self)
        except AssertionError as ex:
            # screenshot_listener = ScreenshotListener()
            # screenshot_listener.on_exception(ex, self.ef_driver)
            make_screenshot(self.ef_driver, 'assert')
            raise ex
        except TimeoutException as ex:
            make_screenshot(self.ef_driver, 'timeout')
            raise ex
    return wrapper

