from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from Config import ZEM
import time
ZEM = ZEM()
# navegador = webdriver.Chrome()


while True:
    print('Bem vindo ao ZEM, vamos usar começar com algo simples')
    print('Primeiro digite a mensagem que você quer mandar')
    #mensagem = input()
    print('Certo, Muito obrigado por ter digitado')

    ZEM.abrir()
    ZEM.maincontactAPI('47999223296')

    ZEM.enviarmensagem('47999227488')

    ZEM.abirnumero('47999227488')

    input()
    