import time

from selenium import webdriver


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)