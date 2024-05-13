from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import time 
#==========wypelnic==============
nick = "veyreal"
haslo = "245583lol"
jaki_pokeball = "2"
jaki_pokemon = "1"
#================================
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://pokelife.pl")
time.sleep(2)
driver.maximize_window()


#logowanie
search = driver.find_element(by=By.NAME, value='login')
search.send_keys(nick)
search = driver.find_element(by=By.NAME, value='haslo')
search.send_keys(haslo)  
element = driver.find_element(By.XPATH, "//button[contains(text(),'Zaloguj')]")  
element.click()

#czekanie na logowanie
driver.implicitly_wait(1)

element = driver.find_element(By.XPATH,'//*[@id="pasek_skrotow"]/ul/li[2]/a/img')
element.click()
time.sleep(0.2)

while True:
    try:
        #wybranie pokemona
        element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/div[2]/div['+str(jaki_pokemon)+']/button/img')
        element.click()
        time.sleep(0.5)
    except NoSuchElementException:
        try:
            #kontynuuj
            element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/div[2]/div/div/button[2]')
            element.click()
        except NoSuchElementException:
            try:
                #pokeball
                element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/form/center/div/label['+str(jaki_pokeball)+']/img')
                element.click()
            except NoSuchElementException:
                try: 
                    #kontynuj po trenerze
                    element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/div[6]/div/div/button[2]')
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    element.click()
                except NoSuchElementException:
                    try: 
                        #kontynuj po walce z pokemonem z za duzym poziomem
                        element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/div[4]/div/div/button[2]')
                        element.click()
                    except NoSuchElementException:
                        try:
                            element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/div/div/div/button[2]')
                            element.click()
                        except NoSuchElementException:
                            break