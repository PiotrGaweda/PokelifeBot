from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

import time 
import re
import datetime
#==========wypelnic==============
nick = "veyreal" 
haslo = "245583lol"
#==========================
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://pokelife.pl")
time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(0.5)

#logowanie
search = driver.find_element(by=By.NAME, value='login')
search.send_keys(nick)
search = driver.find_element(by=By.NAME, value='haslo')
search.send_keys(haslo)  
element = driver.find_element(By.XPATH, "//button[contains(text(),'Zaloguj')]")  
element.click()
time.sleep(1)



while True:
    #klikniecie na zaslugi
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[8]/a')
    element.click()

    #klikniecie na zaslugi
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[8]/ul/li[3]/a')
    element.click()

    #liczba yen w obiegu
    zaslugi = element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/center/b[1]/big')
    obieg = int(zaslugi.text.strip("§"))
    
    print(obieg)
    
    #limit
    limitZaslug = element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/center/span')
    limit = int(limitZaslug.text)
    
    if limit < obieg:
        element = driver.find_element(By.XPATH, '//*[@id="target0"]')
        element.click()
        time.sleep(1)
        element.send_keys(limit)
        time.sleep(1)
        element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/form[1]/div/div/span[1]/button')
        time.sleep(0.1)
        element.click()
        
    if limit > obieg:
        element = driver.find_element(By.XPATH, '//*[@id="target0"]')
        element.click()
        time.sleep(1)
        element.send_keys(obieg)
        time.sleep(1)
        element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/form[1]/div/div/span[1]/button')
        time.sleep(0.1)
        element.click()
        
        
    

    time.sleep(20)
    
    driver.refresh()
