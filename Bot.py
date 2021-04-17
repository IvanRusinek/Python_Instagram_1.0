#llamando a webdriver, time, 
from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# BotMarta (ver: 0.5). Propietario Ivan Rusinek

#LOGIN
#bot "BotMarta"
BotMarta = webdriver.Chrome(executable_path="chromedriver.exe")
BotMarta.maximize_window()

#web de destino
BotMarta.get("https://www.instagram.com/")
time.sleep(1)

#elementos de la pantalla
usuario = BotMarta.find_element_by_xpath ('//*[@id="loginForm"]/div/div[1]/div/label/input')
contraseña = BotMarta.find_element_by_xpath ('//*[@id="loginForm"]/div/div[2]/div/label/input')
boton = BotMarta.find_element_by_xpath ('//*[@id="loginForm"]/div/div[3]')
time.sleep(1)

#informacion que se coloca en los elementos
usuario.send_keys("lasemanademoda")
contraseña.send_keys("lasemanademoda123456789Nattale")
time.sleep(1)
boton.click()
time.sleep(2)

#no guardar informacion
botonnoguardarinfo = BotMarta.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
botonnoguardarinfo.click()

#no tener notificaciones
botonnotificacion = BotMarta.find_element_by_xpath ('/html/body/div[4]/div/div/div/div[3]/button[2]')
botonnotificacion.click()

# SEGUIR A OTROS USUARIOS ###
#1
BotMarta.get("https://www.instagram.com/zara/")
botonseguir = BotMarta.find_element_by_xpath ('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
botonseguir.click()
time.sleep(1)

#2
BotMarta.get('https://www.instagram.com/gucci/')
botonseguir = BotMarta.find_element_by_xpath ('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
botonseguir.click()
time.sleep(1)

#  DEJAR DE SEGUIR A OTROS USUARIOS
#1
BotMarta.get("https://www.instagram.com/zara/")
botondejardeseguir = BotMarta.find_element_by_xpath ('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
botondejardeseguir.click()
botondejardeseguir = BotMarta.find_element_by_xpath ('/html/body/div[5]/div/div/div/div[3]/button[1]')
botondejardeseguir.click()
time.sleep(1)

#2
BotMarta.get('https://www.instagram.com/gucci/')
botondejardeseguir = BotMarta.find_element_by_xpath ('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
botondejardeseguir.click()
botondejardeseguir = BotMarta.find_element_by_xpath ('/html/body/div[5]/div/div/div/div[3]/button[1]')
botondejardeseguir.click()
time.sleep(1)

#TERMINAR CON BOT
BotMarta.quit()


