#ex5
print('Lados de um triângulo: ')
print()
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
print()
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print('é um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('é um triângulo isosceles')
    else:
        print('é um triângulo escaleno')
else:
    print('não é um triângulo')