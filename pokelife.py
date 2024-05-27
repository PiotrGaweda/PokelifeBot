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
nick = "veyrill"
haslo = "245583lol"
jaki_pokeball = "2"
jaki_pokemon = "1"
jaka_dzicz = "4"
jagody_do_zjedzenia = "1"
energole_do_wypicia = "1"
ile_wisniowek = 5
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
driver.implicitly_wait(0.1)
def petla_expienie():
    while (True):
        try:
            #sprawdzanie PA
            xPA = element = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[1]/div[2]/div[1]/div/div/span')
            text = xPA.text
            PA = int(text.split('/')[0].strip())
            if PA < 5:
                break
            #wybranie pokemona
            element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/div[2]/div['+str(jaki_pokemon)+']/button/img')
            element.click()
            time.sleep(0.4)
        except NoSuchElementException:
            try:
                #pokeball
                element = driver.find_element(By.XPATH, '//*[@id="glowne_okno"]/div/div[2]/form/center/div/label['+str(jaki_pokeball)+']/img')
                element.click()
            except NoSuchElementException:
                try:
                    #dzicz
                    element = driver.find_element(By.XPATH,'//*[@id="pasek_skrotow"]/ul/li['+str(jaka_dzicz)+']/a/img')
                    element.click()
                except NoSuchElementException:
                  time.sleep(999)
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
            
            #klikniecie na stowarzyszenie
            element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[6]/a')
            element.click()
            time.sleep(1)
            
            #wejscie w twoje stowarzyszenie
            element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[6]/ul/li[2]/a')
            element.click()
            time.sleep(1)
            
            #fontanna
            element = driver.find_element(By.XPATH,'//*[@id="mapa_stowarzyszenia"]/img[68]')
            element.click()
            time.sleep(1)
            
            #napij sie z fontanny
            element = driver.find_element(By.XPATH,'//*[@id="opcje-budynku-182423"]/div/div/div[2]/div[2]/div/button')
            element.click()
            time.sleep(1)
            break
        except NoSuchElementException:
                                break                       
def wisniowki():
    for x in range(ile_wisniowek):
        #klikniecie na postać
        time.sleep(1)
        element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[1]/a')
        element.click()
        
        #klikniecie na plecak
        time.sleep(1)
        element = driver.find_element(By.XPATH,'//*[@id="menu-collapse"]/ul/li[1]/ul/li[4]/a')
        element.click()
        time.sleep(1)
        
        #klikniecie na wisnowki
        element = driver.find_element(By.XPATH,'//*[@id="plecaktab-trener"]/div/div[7]/div/img')
        element.click()
        time.sleep(1)
        
        #klikniecie na tabelke z energolami
        element = driver.find_element(By.XPATH,'//*[@id="plecak-duzy_napoj_energetyczny"]/div/div/div[3]/div/div/form/div/input[2]')
        element.click()
        time.sleep(1)
        
        #wpisanie liczby energoli
        element.send_keys("1")
        time.sleep(1)
        element = driver.find_element(By.XPATH,'//*[@id="plecak-duzy_napoj_energetyczny"]/div/div/div[3]/div/div/form/div/span/button')
        element.click()
        
        #zatwierdzenie v2
        element = driver.find_element(By.XPATH,'//*[@id="glowne_okno"]/div/div[2]/div/button[2]')
        element.click()
        time.sleep(1)
        
        petla_expienie()


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

wisniowki()

time.sleep(99999)
