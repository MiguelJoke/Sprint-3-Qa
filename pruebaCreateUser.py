import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")

driver = webdriver.Chrome(executable_path = "C:/Users/Miguel/Desktop/Prueba/chromedriver.exe")
driver.get("https://deliverind.com.ar")
driver.maximize_window()
time.sleep(2)

requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")

linkAccountIcon = driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[2]/i")

time.sleep(4)

linkAccountIcon.click()

time.sleep(3)

CampoMail = driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[1]/input")

time.sleep(2)

CampoMail.click()

time.sleep(2)

CampoMail.send_keys(" ") #"mail de temp mail para demostracion"

time.sleep(2)

buttonAcceder =  driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[3]/button")

time.sleep(2)

buttonAcceder.click()

time.sleep(3)

mensajeError = driver.find_element(By.XPATH, "/html/body/header/ul/li").text

labelObtained = mensajeError

print(mensajeError)

requirement = 'Error: Nombre de usuario requerido.'

compareLabels()

#duda para la profe , al momento de ingresar el mail tengo que 
#"manualmente ingresar al mail y darle click a contraseña 
#para poner la contraseña de la cuenta 
#como automatizo eso ?

driver.close()
