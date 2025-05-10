soma_pares = 0
soma_impares = 0
cont_pares = 0
cont_impares = 0
while True:
    numero = int(input("Digite um número (0 para encerrar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        soma_pares += numero
        cont_pares += 1
    else:
        soma_impares += numero
        cont_impares += 1
if cont_pares > 0:
    media_pares = soma_pares / cont_pares
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Não foram digitados números pares.")
if cont_impares > 0:
    media_impares = soma_impares / cont_impares
    print(f"Média dos números ímpares: {media_impares:.2f}")
else:
    print("Não foram digitados números ímpares.")