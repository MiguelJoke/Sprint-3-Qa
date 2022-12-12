import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-loggin'])
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")

driver = webdriver.Chrome(executable_path="C:/Users/Miguel/Desktop/Prueba/chromedriver.exe")
driver.get("https://deliverind.com.ar")
driver.maximize_window()
time.sleep(2)

linkAccountIcon = driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[2]/i")

time.sleep(4)

linkAccountIcon.click()

time.sleep(3)

campoEmail = driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[1]/input")

time.sleep(2)

campoEmail.click()

time.sleep(2)

campoEmail.send_keys("letojav138")

time.sleep(2)

campoContraseña = driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[2]/input")

time.sleep(2)

campoContraseña.click()

time.sleep(2)

campoContraseña.send_keys("123contraseña85")

time.sleep(2)

buttonAcceder = driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[3]/button")

time.sleep(2)

buttonAcceder.click()

time.sleep(4)

driver.close()