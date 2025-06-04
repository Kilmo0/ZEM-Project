from Config import ZEM
from pathlib import Path

ZEM = ZEM()

numerosPE = Path("Dados/Whatsapp/Numeros.txt")
maincontact = Path("Dados/Whatsapp/mainwhatsapp.txt")

while True:
    print('Bem vindo ao ZEM, vamos usar começar com algo simples')
    print('Primeiro digite a mensagem que você quer mandar')
    print('Certo, Muito obrigado por ter digitado')

    dadosnumeros = ZEM.lerdados(numerosPE)
    contactmain = ZEM.lerdados(maincontact)

    print(contactmain)

    ZEM.abrir()
    ZEM.maincontactAPI(contactmain)

    ZEM.enviarmensagem(dadosnumeros)

    ZEM.abirnumero(dadosnumeros)

    input()
    