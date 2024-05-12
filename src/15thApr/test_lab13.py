from selenium import webdriver

import pytest


@pytest.mark.smoke

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")

  #  < a
  #  id = "btn-make-appointment"
  #  href = "./profile.php#login"

   # class ="btn btn-dark btn-lg" >
# Make Appointment
# < / a >

# find by ID,Class, Tagname,name,linktext  and partial link with anchor tag text then if not find by this go for below

# CSS selector and Xpath

