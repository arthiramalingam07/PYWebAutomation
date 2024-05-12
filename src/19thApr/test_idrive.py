import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure

@allure.title("Idrive Project")
@pytest.mark.sanity

def test_idrive_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()

    Email_element = driver.find_element(By.ID,"username").send_keys("augtest_040823@idrive.com")
    pass_element = driver.find_element(By.ID,"password").send_keys("123456")

    login = driver.find_element(By.ID,"frm-btn")
    login.click()

    time.sleep(15)
    #current_url = driver.current_url
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true","Assert Error = Login URL error"

    #Trial_error_message = driver.find_element(By.CLASS_NAME,"id-card-title")
    Trial_error_message = driver.find_element(By.XPATH,"//h5[@class='id-card-title']")
    assert Trial_error_message == "Your free trial has expired"
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(),name="Trailscreenshot",attachment_type=AttachmentType.PNG)

   # tag_div_list = driver.find_element(By.TAG_NAME,"div")
   # Trail_error_message2 =tag_div_list[147]




    #<div
    # _ngcontent-slx-c10=""
    # class="id-card-cont"
    # >
    # <i
    # _ngcontent-slx-c10=""
    # class="id-expire-msg-icon"
    # >
    # </i>
    # <h5
    # _ngcontent-slx-c10=""
    # class="id-card-title">
    # Your free trial has expired
    # </h5>
    # <p
    # _ngcontent-slx-c10="">
    # and your account has been canceled.
    # </p>
    # <p _ngcontent-slx-c10="">In order to reactivate your account, upgrade your account and save 25%*.</p></div>

   # < input
    #_ngcontent - ilr - c4 = ""

    #class ="id-form-ctrl ng-untouched ng-pristine ng-valid"
# id="password"
# maxlength="20"
# name="password"
# tabindex="0"
# type="password"
# fdprocessedid="ayq9ib" >

