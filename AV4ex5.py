valor_inicial= int(input("Digite o valor inicial: "))
contador= 0
for numero in range(valor_inicial, -1, -1):
    print(numero)
    contador= contador + 1
print()
print("Quantidade de números gerados:", contador)
