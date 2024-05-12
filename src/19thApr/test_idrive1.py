import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_drive_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    email_element = driver.find_element(By.XPATH, "//input[@id='username']")
    email_element.send_keys("augtest_040823@idrive.com")
    pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
    pass_element.send_keys("123456")
    sign_element = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    sign_element.click()
    time.sleep(5)
    current_url = driver.current_url
    time.sleep(10)
    header_message = driver.find_element(By.XPATH, "//h5[@class='id-card-title']").text
    print(header_message)
    assert header_message == "Your free trial has expired", "Error - Invalid message"
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"