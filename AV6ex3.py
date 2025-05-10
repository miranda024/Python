def somar_tres(val1, val2, val3):
    return val1 + val2 + val3
if __name__ == '__main__':
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    resultado = somar_tres(n1, n2, n3)
    print("Resultado da soma:", resultado)
