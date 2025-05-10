soma= 0
for numero in range(1,500+1,1):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print("A soma dos números ímpares e múltiplos de 3 de 1 até 500 é:", soma)
