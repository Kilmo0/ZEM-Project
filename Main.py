from Config import ZEM
from pathlib import Path
import random
import time
import webbrowser



numerosPE = Path("Dados/Whatsapp/Numeros.txt")
maincontact = Path("Dados/Whatsapp/mainwhatsapp.txt")
mensagemfile = Path("Dados/Whatsapp/mensagem.txt")
imagem = Path('Dados/Imagem/imagem.jpeg').resolve()

print('-'*30)
print('Seja bem vindo ao progrmaa ZEM')
time.sleep(2)
print('='*30)
print('='*30)
print('Você já usou o programa ou é a primeira vez?')

while True:
    inicio = input('Digite 1 Caso já usou o programa\n digite 2 caso nunca usou')
    try:
        match inicio:
            case '1':
                print('Vamos começar')
                time.sleep(1)
                print('='*30)*5
                
                break
            case '2':
                print('Certo, iremos abrir um video ensinando como usar')
                webbrowser.open('https://www.youtube.com/watch?v=ESx_hy1n7HA')
                input('Precione enter para continuar')
                break
    except:
        print('Ops, não consegui entender o que você quis dizer 😥')
        time.sleep(2)
        print('Vamos tentar novamente')
    


ZEM = ZEM()
while True:

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
    