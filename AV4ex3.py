soma= 0
contador= 0
for numero in range(1, 11):
    dobro = numero * 2
    print(dobro)
    soma= soma + dobro
    contador= contador + 1
media = soma / contador
print()
print("Soma:", soma)
print("Média:", media)
