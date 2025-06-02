from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

while True:
    print('Bem vindo ao ZEM, vamos usar começar com algo simples')
    print('Primeiro digite a mensagem que você quer mandar')
    #mensagem = input()
    print('Certo, Muito obrigado por ter digitado')

    navegador = webdriver.Chrome()
    navegador.get('https://web.whatsapp.com/')
    navegador.maximize_window()
    input('Por favor digite Escaneie o Códgio QR e tecle enter para continuar')
    time.sleep(2)
    #seucontato = input('Por favor digite seu contato Exemplo: 47999220000\n')
    navegador.switch_to.new_window('tab')
    Apiwhatsapp = navegador.get(f'https://api.whatsapp.com/send?phone=47999223296&text=')
    time.sleep(2)

    
    navegador.find_element(By.ID, 'action-button').click()
    time.sleep(2)
    navegador.find_element(By.LINK_TEXT, 'usar o WhatsApp Web').click()

    espere = WebDriverWait(navegador, 60)
    campodigitar = espere.until(ec.presence_of_element_located((By.XPATH, '//div[@aria-label="Digite uma mensagem"]')))
    
    campodigitar.send_keys('47999223296')
    campodigitar.send_keys(Keys.ENTER)
    


    input()
    