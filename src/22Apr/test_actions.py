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
    driver =webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    clickable = driver.find_element(By.ID,"clickable")
    actions = ActionChains(driver)
    actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("Name").key_up(Keys.SHIFT).perform()
    time.sleep(5)

    actions.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("A").perform()

    ActionChains(driver).click(clickable).perform()
    # click > it will go to another on clicking
    # click and hold > will change the colcour of the links ..Hold .. nothing happens

    #ActionBuilder
    # it is used for the mouse >back
    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    actions_builder.perform()

    #Double click
    ActionChains(driver).double_click(clickable)\
    .perform()
    # \ in the line gives continuation the following one

    #Hoverable

    Hover =driver.find_element(By.ID,"hover")
    ActionChains(driver).move_to_element(Hover).perform()

    #Drag and Drop

    Drag = driver.find_element(By.ID,"draggable")
    Drop = driver.find_element(By.ID,"droppable")

    ActionChains(driver).drag_and_drop(Drag,Drop).perform()

    


