import time

from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
   # driver.implicitly_wait(5)


    #e1,e2
    # tell the webdriver to wait for 5 sec
    #all the elements
    # all the elements are started by 3 the 2 sec is wasted.
    # time.sleep > Python interpret is waiting > bad practice
    # implicit wait is not useful much

    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("Test")

    pass_element = driver.find_element(By.NAME, "password")
    pass_element.send_keys("test")

    submit_element = driver.find_element(By.ID, "js-login-btn")
    submit_element.click()
    time.sleep(10)

    # for error message we have to wait after clicking submit
    #wait with the condition
    #until page is vwo.com
    #until the error is visible > move forwaard
    #Explicit > wait for the condition
    #Untill error is seeen on the DOM
    #EC > Expected condition

    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    time.sleep(10)