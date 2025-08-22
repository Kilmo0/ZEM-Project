while True:
    print('Digite o peso da primeira prova')
    pesoprova1 = float(input())
    print('Digite o nota da prova')
    nota1 = float(input())
    print('Digite o peso da segunda prova')
    pesoprova2 = float(input())
    print('Digite o nota da prova')
    nota2 = float(input())
    print('Digite o peso da terceira prova')
    pesoprova3 = float(input())
    print('Digite o nota da prova')
    nota3 = float(input())
    print('Digite o peso da prova Presencial')
    pesopresencial = float(input())
    print('Digite o nota da prova')
    nota4 = float(input())

    calculomedia = ((nota1*pesoprova1) + (nota2*pesoprova2) + (nota3*pesoprova3) + (nota4*pesopresencial)) / 10

    print(f'Sua média será {calculomedia}')

    print('Digite 1 para sair')
    siar = input()
    if siar == '1':
        break