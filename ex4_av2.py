#ex4
num_1=float(input('digite o primeiro numero: '))
num_2=float(input('digite o segundo numero: '))
print()
print('escolha as operações: ')
print('+ para adição')
print('- para subtração')
print('* para multiplicação')
print('/ para divisão')
print()
operacao=input('digite a operação desejada: ')
print()
if operacao == '+':
    resultado =  num_1 + num_2
    print('resultado da soma = ',resultado)
elif operacao == '-':
    resultado = num_1 - num_2
    print('resultado da subtração = ',resultado)
elif operacao == '*':
    resultado = num_1 * num_2
    print('resultado da multiplicação = ',resultado)
elif operacao == '/':
    if num_2 != 0:
        resultado = num_1 / num_2
        print('resultado da divisão = ',resultado)
    else:
        print('Erro!Não foi possível dividir por zero')
else:
    print('operação inválida. Escolha +,-,* ou /')


