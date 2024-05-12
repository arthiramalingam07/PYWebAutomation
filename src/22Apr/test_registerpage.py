import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import time
import allure

@allure.title("Register page validation")
@allure.description("Error Validation for Username")
def test_register_username_error_validation():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()

    assert driver.current_url == "https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage"
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(),name="Register",attachment_type="AttachmentType.PNG")
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    #Username Error Validation

    username_field = driver.find_element(By.XPATH,"//input[@id='username']")
    username_field.send_keys("")

    #email_field = driver.find_element(By.XPATH,"//input[@id='email']")
    email_field = driver.find_element(By.ID,"email")
    email_field.send_keys("test123@gmail.com")

    password_field = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Test12233")
    #conpass= password_field.send_keys("Test123")

    confirm_password_field = driver.find_element(By.XPATH,"//input[@id='password2']")
    confirm_password_field.send_keys("Test12233")
    time.sleep(10)
    #print(password_field)
    submit_field = driver.find_element(By.XPATH,"//*[text()='Submit']")
    submit_field.click()
    time.sleep(10)

    username_error1_msg = driver.find_element(By.XPATH,"//*[text() ='Username must be at least 3 characters']/following::small")
    assert username_error1_msg == True
    time.sleep(10)





