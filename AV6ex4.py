def maior_valor(a, b):
    if a > b:
        return a
    else:
        return b
if __name__ == '__main__':
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    maior = maior_valor(numero1, numero2)
    print("O maior valor é:", maior)
