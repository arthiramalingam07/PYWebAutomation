import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    time.sleep(5)

    appointment_button = driver.find_element(By.ID, 'btn-make-appointment')
    appointment_button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    username_login = driver.find_element(By.ID, 'txt-username')
    username_login.send_keys("John Doe")
    password_login = driver.find_element(By.ID, 'txt-password')
    password_login.send_keys("ThisIsNotAPassword")

    button_login = driver.find_element(By.ID, 'btn-login')
    button_login.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    title_appt= driver.find_element(By.XPATH,"//div[text()='Make Appointment']")
    assert title_appt == "Make Appointment"





