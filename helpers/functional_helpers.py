def user_login(driver, user_email, user_password):
    """Login user to website using given email and password

    :param driver: webdriver instance
    :param user_email: email address which will be used as login
    :param user_password: password which will be used t login
    """
    login_input_element = driver.find_element_by_xpath('//*[@type ="email"]')
    login_input_element.send_keys(user_email)

    login_input_element = driver.find_element_by_xpath('//*[@type = "password"]')
    login_input_element.send_keys(user_password)

    submmit_button = driver.find_element_by_xpath('//*[@ id = "submit-login"]')
    submmit_button.click()