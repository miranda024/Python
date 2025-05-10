contador = 0
soma = 0
maiores_que_20 = 0
while True:
    valor = float(input("Digite um valor real (ou digite '0' para encerrar): "))
    if valor == 0:
        break
    contador += 1
    soma += valor
    if valor > 20:
        maiores_que_20 += 1
if contador > 0:
    media = soma / contador
else:
    media = 0
print()
print(f"Quantidade de valores digitados: {contador}")
print(f"Soma dos valores digitados: {soma}")
print(f"Média aritmética dos valores digitados: {media:.2f}")
print(f"Quantidade de valores maiores que 20: {maiores_que_20}")