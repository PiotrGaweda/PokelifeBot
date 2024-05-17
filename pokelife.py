from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import time 
import re
#==========wypelnic==============
nick = "veyreal"
haslo = "245583lol"
jaki_pokeball = "2"
jaki_pokemon = "1"
jaka_dzicz = "4"
jagody_do_zjedzenia = "1"
energole_do_wypicia = "8"
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

#czekanie na logowanie(!!!!!!!!!!!MOZE CRASHOWAĆ PRZY DLUZSZYM UZYCIU BOTA IDKIDK!!!!!!!!!)
driver.implicitly_wait(0.09)

def petla_expienie():
    while (True):
        try:
            #sprawdzanie PA
            xPA = element = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[1]/div[2]/div[1]/div/div/span')
            text = xPA.text
            PA = int(text.split('/')[0].strip())
            if PA < 5:
                break
            #sprawdzenie czy jest Shiny
            Shiny = element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/div[1]/div/div/div[2]/big/strong/i')
            tekst = Shiny.text
            if "Shiny" in tekst:
                time.sleep(999999)
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
def regen():
    while (True):
        try:
            #klikniecie na postać
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[1]/a')
            element.click()
            
            #klikniecie na plecak
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[1]/ul/li[4]/a')
            element.click()
            time.sleep(1)
            
            #klikniecie na niebieskie jagody jako 5 element
            element = driver.find_element(By.XPATH,'//*[@id="plecaktab-trener"]/div/div[9]/div/img')
            element.click()
            time.sleep(1)
            
            #klikniecie na tabelke z jagodami
            element = driver.find_element(By.XPATH,'//*[@id="plecak-niebieskie_jagody"]/div/div/div[3]/div/div/form/div/input[2]')
            element.click()
            time.sleep(1)
            
            #wpisanie liczby jagod
            element.send_keys(jagody_do_zjedzenia)
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="plecak-niebieskie_jagody"]/div/div/div[3]/div/div/form/div/span/button')
            element.click()
            
            #zatwierdzenie
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/div/button[2]')
            element.click()
            
            #klikniecie na postac
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[1]/a')
            element.click()
            
            #klikniecie na plecak
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[1]/ul/li[4]/a')
            element.click()
            time.sleep(1)
            
            #klikniecie na zielone energole jako 1 element
            element = driver.find_element(By.XPATH,'//*[@id="plecaktab-trener"]/div/div[1]/div/img')
            element.click()
            time.sleep(1)
            
            #klikniecie na tabelke z energolami
            element = driver.find_element(By.XPATH,'//*[@id="plecak-zielony_napoj"]/div/div/div[3]/div/div/form/div/input[2]')
            element.click()
            time.sleep(1)
            
            #wpisanie liczby energoli
            element.send_keys(energole_do_wypicia)
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="plecak-zielony_napoj"]/div/div/div[3]/div/div/form/div/input[2]')
            element.click()
            
            #zatwierdzenie
            time.sleep(1)
            element = driver.find_element(By.XPATH,'//*[@id="plecak-zielony_napoj"]/div/div/div[3]/div/div/form/div/span/button')
            element.click()
            time.sleep(1)
            
            #zatwierdzenie v2
            element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/div/button[2]')
            element.click()
            time.sleep(1)
            break
        except NoSuchElementException:
                                break                       

#wejscie w dzicz
element = driver.find_element(By.XPATH,'//*[@id="pasek_skrotow"]/ul/li['+str(jaka_dzicz)+']/a/img')
element.click()
time.sleep(0.2)

petla_expienie()

regen()

#wejscie w dzicz
element = driver.find_element(By.XPATH,'//*[@id="pasek_skrotow"]/ul/li['+str(jaka_dzicz)+']/a/img')
element.click()
time.sleep(0.2)

petla_expienie()

time.sleep(99999)
