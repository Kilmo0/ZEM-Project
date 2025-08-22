from Config import ZEM
from pathlib import Path
import random
import time
import webbrowser



numerosPE = Path("Dados/Whatsapp/Numeros.txt")
maincontact = Path("Dados/Whatsapp/mainwhatsapp.txt")
mensagemfile = Path("Dados/Whatsapp/mensagem.txt")
imagem = Path('Dados/Imagem/Imagem.jpeg').resolve()



ZEM = ZEM()
while True:

    dadosnumeros = ZEM.lerdados(numerosPE).rsplit()
    contactmain = ZEM.lerdados(maincontact)
    mensagem = ZEM.lerdados(mensagemfile)

    print(contactmain)
    ZEM.abrir()
    ZEM.maincontactAPI(contactmain)
    for enviar in dadosnumeros:
        ZEM.enviarmensagem(enviar)
        time.sleep(random.randint(1,3))
        ZEM.abirnumero(enviar)
        time.sleep(random.randint(1,3))
        ZEM.enviarmensagem(mensagem)
        time.sleep(random.randint(1,3))
        ZEM.contact()
        time.sleep(random.randint(1,3))
        ZEM.backmain('+55 47 9922-3296')
    time.sleep(random.randint(1,8))

    input('Digite Enter para finalizar o programa')
    break
    