valor_final= int(input("Digite o valor final: "))
contador= 0
for numero in range(1, valor_final + 1):
    print(numero)
    contador= contador + 1
print()
print("Quantidade de números gerados:", contador)
