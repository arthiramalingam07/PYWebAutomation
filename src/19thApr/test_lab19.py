# Xpath > //tagname[@attribute ='value']
from selenium import webdriver
from selenium.webdriver.common.by import By


#<input
# type="email"
# class="text-input W(100%)"
# name="username"
# id="login-username"
# data-qa="hocewoqisi"
# fdprocessedid="3ldk6"
# data-gtm-form-interact-field-id="0"
# >

 #//input[@id='login-username']
 #//input[@name='username']
# //input[@class='text-input W(100%)'] Not Recommend
# //input[@type='email'] -Not recommend
# //input[@data-qa='hocewoqisi'] -Recommend > custom attribute added by QA to identify

def test_cura_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment = driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']").click()
    print(driver.current_url)
          
