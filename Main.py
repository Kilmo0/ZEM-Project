from Config import ZEM
from pathlib import Path
import random
import time


ZEM = ZEM()

numerosPE = Path("Dados/Whatsapp/Numeros.txt")
maincontact = Path("Dados/Whatsapp/mainwhatsapp.txt")
mensagemfile = Path("Dados/Whatsapp/mensagem.txt")
imagem = Path('Dados/Imagem/imagem.jpeg').resolve()


while True:
    print('Bem vindo ao ZEM, vamos usar começar com algo simples')
    print('Primeiro digite a mensagem que você quer mandar')
    print('Certo, Muito obrigado por ter digitado')

    dadosnumeros = ZEM.lerdados(numerosPE).rsplit()
    contactmain = ZEM.lerdados(maincontact)
    mensagem = ZEM.lerdados(mensagemfile)

    contactmain1 = contactmain[4:]
    contactmain2 = contactmain1[2:3]
    contactmain1 = contactmain1.replace(contactmain2, '9')
    contactmain2 = contactmain1[7:8]
    contactmain1 = contactmain1.replace(contactmain2, '')

    ZEM.abrir()
    ZEM.maincontactAPI(contactmain1)
    for enviar in dadosnumeros:
        ZEM.enviarmensagem(enviar)
        time.sleep(random.randint(1,3))
        ZEM.abirnumero(enviar)
        time.sleep(random.randint(1,3))
        ZEM.sendimage(imagem)
        time.sleep(random.randint(1,3))
        ZEM.enviarmensagem(mensagem)
        time.sleep(random.randint(1,3))
        ZEM.backmain(contactmain)
        time.sleep(random.randint(1,8))

    input('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    