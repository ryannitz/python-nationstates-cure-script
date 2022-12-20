from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import cgi


yourNationName = ''
password = ''
infectedNationName = ''
parentPage = "https://www.nationstates.net/"


driver = webdriver.Chrome("./chromedriver") #using chrome
driver.get(parentPage)
driver.find_element_by_css_selector('#loginbannerbox').click()
driver.find_element_by_css_selector('input[name="nation"]').send_keys(yourNationName) #your nation name all lowercase
driver.find_element_by_css_selector('input[name="password"]').send_keys(password) #your password
driver.find_element_by_css_selector('button[name="submit"]').click()

time.sleep(5)
targetPage = parentPage + "nation=" + infectedNationName
driver.get(targetPage)
time.sleep(5)

zombieCountElem = driver.find_element_by_css_selector('#zoverview > table > tbody > tr:nth-child(2) > td:nth-child(2)')
zombieCount = zombieCountElem.text
zombieCount = zombieCount.replace(",", "")
zombieCount = int(zombieCount)
print(zombieCount)

while(zombieCount > 0):
    zombieCountElem = driver.find_element_by_css_selector('#zoverview > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    zombieCount = zombieCountElem.text
    zombieCount = zombieCount.replace(",", "")
    zombieCount = int(zombieCount)
    print(zombieCount)

    cureButton = driver.find_element_by_css_selector('button[name="zsw_cure"]')
    time.sleep(1)
    #EC.element_to_be_clickable((By.css, "myDynamicElement"))
    cureButton.click()
    time.sleep(22)

#end
driver.close()
quit()


