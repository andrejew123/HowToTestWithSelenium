import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpah was found
    :param driver: driver from webdriver element
    :param xpath: xpath for element
    :param max_seconds_to_wait: maximum time for waiting (default: 5)
    :param number_of_expected_elements: number of minimum expected elements
    :return: list of found elements
    """
    for second in range(max_seconds_to_wait):
        xpath_elements = driver.find_elements_by_xpath(xpath)
        if len(xpath_elements) >= number_of_expected_elements:
            return xpath_elements
        if second == max_seconds_to_wait - 1:
            print('END OF TIME')
            assert len(xpath_elements) >= number_of_expected_elements, f'Expected {number_of_expected_elements} \
            elements but found len {xpath_elements} for xpath not fount in time f {second}s'
        time.sleep(1)


def visibility_of_element_wait(driver, xpath, timeout=10):
    """
    Checking if element specified by xpath is visible on page
    :param driver: webdriver instance
    :param xpath: xpath for element which will be locate
    :param timeout: max time for waiting until element is visible (default: 10)
    :return first element in list of found elements
    """
    timeout_message = f'Element for xpath: {xpath} and url {driver.current_url} not found in {timeout}'
    locator = By.XPATH, xpath
    element_located = EC.visibility_of_element_located(locator) #using EventFireWebDriver
    wait = WebDriverWait(driver.wrapped_driver, timeout) #using pure driver
    return wait.until(element_located, timeout_message)
