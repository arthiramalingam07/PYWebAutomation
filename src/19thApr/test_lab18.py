import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke
@allure.title("Verify the login page")
@allure.description("TC1 -Login check on Cura")
def test_cura_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment = driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    print(driver.current_url)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login" ,"Assertion fail message -Error matching the url"

    username = driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    submit = driver.find_element(By.ID,"btn-login").click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment","Error 2- Wrong URL"

    #Scrrenshot
    allure.attach(driver.get_screenshot_as_png(),name = "Login",attachment_type=AttachmentType.PNG)



