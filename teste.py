from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path

file = Path('Dados/imagens/TESTE.png')

navegador = webdriver.Chrome()
navegador.get('https://google.com/')
upload = navegador.find_element(By.ID, "upload")

pesquisar = navegador.find_element(By.CLASS_NAME, 'gLFyf')
pesquisar.click()
upload.send_keys(file)

input()
