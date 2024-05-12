import time

from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    time.sleep(20)

    # Priority   id> name >class>tagname >Linktext,partial > CSS selector > Xpath

    # // *[ @ id = "login-username"]

   # < input
   # type = "email"

   # class ="text-input W(100%)"
# name="username"
# id="login-username"
# data-qa="hocewoqisi" fdprocessedid="3ldk6" >

    email_element = driver.find_element(By.NAME,"username")
    email_element.send_keys("Test")

    pass_element = driver.find_element(By.NAME,"password")
    pass_element.send_keys("test")

    submit_element = driver.find_element(By.ID,"js-login-btn")
    submit_element.click()
    time.sleep(10)

    error_msg_element =driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    time.sleep(10)
