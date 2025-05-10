#ex1
numero_um=int(input('digite o primeior número:'))
numero_dois=int(input('digite o segundo número'))
print()
if numero_um > numero_dois:
    print(f'{numero_um} maior que {numero_dois}')
elif numero_dois > numero_um:
    print(f'{numero_dois} maior que {numero_um}')
else:
    print('valores iguais')
