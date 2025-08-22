from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--log-level=3")
service = Service(log_path='NUL')


options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/115.0.0.0 Safari/537.36")



class ZEM():
    def __init__(self):
        self.navegador = webdriver.Chrome(options=options, service=service)
        self.wait = WebDriverWait(self.navegador, 60)
        self.wait5 = WebDriverWait(self.navegador, 5)


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
        try:
            self.wait5.until(ec.element_to_be_clickable((By.LINK_TEXT, 'use WhatsApp Web')))
            self.navegador.find_element(By.LINK_TEXT, 'use WhatsApp Web').click()
        except:
            self.wait5.until(ec.element_to_be_clickable((By.LINK_TEXT, 'usar o WhatsApp Web')))
            self.navegador.find_element(By.LINK_TEXT, 'usar o WhatsApp Web').click()

    def enviarmensagem(self, mensagem):
        self.wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")))
        campodigitar = self.navegador.find_element(By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
        campodigitar.click()
        campodigitar.send_keys(mensagem)
        campodigitar.send_keys(Keys.ENTER)
    
    def abirnumero(self, ultimonumero):
        self.wait.until(ec.presence_of_all_elements_located((By.LINK_TEXT, ultimonumero)))
        numero = self.navegador.find_element(By.LINK_TEXT, ultimonumero)
        time.sleep(1)
        numero.click()
        self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//span[@aria-hidden="true" and @data-icon="chat-refreshed"]')))
        self.navegador.find_element(By.XPATH, '//span[@aria-hidden="true" and @data-icon="chat-refreshed"]').click()
        time.sleep(2)

    def lerdados(self, dado):
        with open(dado, 'r', encoding='UTF-8') as filename:
            filename = filename.read()
            return filename 
    
    def backmain(self, seunumero):
        # seunumero = str(seunumero)
        self.wait5.until(ec.presence_of_all_elements_located((By.XPATH, '//span[@data-icon="search-refreshed-thin"]')))
        pesquisar = self.navegador.find_element(By.XPATH, '//span[@data-icon="search-refreshed-thin"]')
        pesquisar.click()
        pesquisar1 = self.navegador.find_element(By.XPATH, '//div[@aria-autocomplete="list"]')
        pesquisar1.click()
        pesquisar1.send_keys('você')
        self.wait5.until(ec.presence_of_all_elements_located((By.XPATH, f'//span[@dir="auto" and @title="{seunumero}"]')))
        self.navegador.find_element(By.XPATH, f'//span[@dir="auto" and @title="{seunumero}"]').click()
        
    def sendimage(self, figura):
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '//span[@data-icon="plus"]').click()
        self.wait5.until(ec.presence_of_all_elements_located((By.XPATH, '//span[@class="xdod15v xzwifym x6ikm8r x10wlt62 xlyipyv xuxw1ft"]')))
        # self.navegador.find_element(By.XPATH, '//span[@class="xdod15v xzwifym x6ikm8r x10wlt62 xlyipyv xuxw1ft"]').click()
        time.sleep(1)
        upload_input = self.navegador.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        upload_input.send_keys(str(figura))
        self.wait5.until(ec.presence_of_all_elements_located((By.XPATH, '//span[@data-icon="send"]')))
        self.navegador.find_element(By.XPATH, '//span[@data-icon="send"]').click()

    def contact(self):
        """Its just a test"""
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//span[@data-icon="plus-rounded"]').click()
        time.sleep(1)
        self.navegador.find_element(By.XPATH, '//span[@data-icon="person-filled-refreshed"]').click()
        # self.wait5.until(ec.presence_of_all_elements_located((By.XPATH, '//div[@aria-autocomplete="list"]')))
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//div[@aria-autocomplete="list"]').send_keys('Anton')
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//span[@title="Anton"]').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//span[@aria-label="Enviar contatos selecionados"]').click()
        time.sleep(2)
        self.navegador.find_element(By.XPATH, '//span[@data-icon="wds-ic-send-filled"]').click()




        
