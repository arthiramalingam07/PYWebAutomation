import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")

    main_window_handle = driver.current_window_handle
    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles) #print the number of windows

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source
            print("Found the Text")
            break;



