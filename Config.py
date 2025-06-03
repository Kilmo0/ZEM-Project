from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

# navegador = webdriver.Chrome

class ZEM():
    def __init__(self):
        self.navegador = webdriver.Chrome()
        # self.newtab = self.navegador.switch_to.new_window('tab') 
        self.wait = WebDriverWait(self.navegador, 60)


    def abrir(self):
        self.navegador.get('https://web.whatsapp.com/')
        time.sleep(1)
        self.navegador.maximize_window()
        input('Pressione enter para continuar')

    def maincontactAPI(self, principalcontato):
        principalcontato = str(principalcontato)
        self.navegador.switch_to.new_window('tab')
        self.navegador.get(f'https://api.whatsapp.com/send?phone={principalcontato}&text=')
        self.wait.until(ec.presence_of_all_elements_located((By.ID, 'action-button')))
        self.navegador.find_element(By.ID, 'action-button').click()
        self.wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'use WhatsApp Web')))
        self.navegador.find_element(By.LINK_TEXT, 'use WhatsApp Web').click()

    def enviarmensagem(self, numero):
        numero = str(numero)
        self.wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")))
        campodigitar = self.navegador.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
        campodigitar.click()
        campodigitar.send_keys(numero)
        campodigitar.send_keys(Keys.ENTER)
    
    def abirnumero(self, ultimonumero):
        self.wait.until(ec.presence_of_all_elements_located((By.LINK_TEXT, ultimonumero)))
        numero = self.navegador.find_element(By.LINK_TEXT, ultimonumero)
        numero.click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//div[@aria-label="Conversar com "]').click()

    


        

        
