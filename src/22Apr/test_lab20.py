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
    driver.get("https://app.vwo.com/")

    # //*[@id='Wqdgdfji'] - Fast
    #//*[@id='btn-make-appointment'] - this iswildcard
    # finds id = btn-make -app in all tagnames, this is slow path
    #//a[@='btn-make-app'] -2

    # text() finds the text which only works for exact match
    # for partial text match > contains

    driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    # driver.find_element(By.XPATH,"//a[contains(text(),'Make Appointment')]")
    #//a[contains(text(),'Make')]"
    #// a[contains(text(), 'Appointment')]
    #//a[contains(text(),'Appo')]"
    #//a[start-with(text(),'Appo')]"
    #//a[ends-with(text(),'ments')]"

