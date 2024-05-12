import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_actions():
    driver =webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    firstname = driver.find_element(By.NAME,"firstname")
    # to create a object
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname,"Academy").key_up(Keys.SHIFT).perform()
    time.sleep(5)

    dowload_click = driver.find_element(By.XPATH,"//a[contains(text(),'Click here to Download File')]")
    actions.context_click(dowload_click).perform()
    time.sleep(10)

    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions.send_keys("Sleenium")