import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_actions():
    driver =webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.NAME,"nested_scrolling_frame")
    actions = ActionChains(driver)
    actions.scroll_to_element(iframe).perform()

    #scroll to element with offset ,0-50  offset is half inside and hald outside
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(driver).scroll_from_origin(scroll_origin,0,200).perform()
    #it will scroll inside the iframe



