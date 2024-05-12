import time

from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(20)
    # driver.find_element(By.ID,"btn-make-appointment").click()
    # link text works only with @a tag <a ....  a> anchor tag
    # link text ca be partial or exact match
    # it will always return the first link text
    # not link text , cant find element

    #<a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment</a>

    # make_appointment = driver.find_element(By.LINK_TEXT,"Make Appointment").click()


    # partial text > partial match with only anchor tag
   # make_appointment = driver.find_element(By.PARTIAL_LINK_TEXT, "Make Appointment").click()
# make
#Appointment
    #Appoint
    #Mak all possible matches
    #find the first unique element

    # By Tagname

    list_tags = driver.find_element(By.TAG_NAME, "a")
    make_appointment = list_tags[5] # 6 th element of a is make appointment 0,1,2,3,4,5
    make_appointment.click()


   # assert error_msg_element.text == "Your email, password, IP address or location did not match"
    time.sleep(10)
