import time

from selenium import webdriver


def test_login():
    driver = webdriver.Chrome()
    #fresh copy of browser is opened.
    #new session created with unique 10 digits

    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(5) # pyt interpre wiat for 5 sec not the web driver
    print(driver.title)
    driver.get("https://bing.com")
    #driver.close() # close the current tab , session is not equal to null

    driver.quit() # it closes the session

    #driver navigate and to commands are not used

    driver.back()
    driver.refresh()
    driver.forward()




    assert driver.title == "Login - VWO"

