
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    #driver.maximize_window()

    #row --//table[contains(@id,"cust")]/tbody/tr

    row_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)
    # #columns --//table[contains(@id,"cust")]/tbody/tr[1]/td
    column_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr[2]/td")
    column = len(column_elements)
    print(column)

    # FP > //table[contains(@id,"cust")]/tbody/tr[
    # 2-7 (i)
    #SP >]/td[
    # 1-3 > j value
    #]


    FP = "//table[contains(@id,'cust')]/tbody/tr["
    SP = "]/td["
    TP = "]"
    for i in range(2,row+1): # range (1,10)> 1 ,9+1
        for j in range(1,column+1):
            table_path = f"{FP}{i}{SP}{j}{TP}"
            complete_path = driver.find_element(By.XPATH,table_path)
            print(complete_path)
           # print(complete_path.text,end=" ")
        if "Helen Bennett" in complete_path:
            country_path = f"{table_path}/following-sibling::td"
            country =driver.find_element(By.XPATH,country_path).text
            print(f"Helen Bennett is in {country}")


            









