#exercício 01

raioEsfera = float(input("Digite o raio:"))

resultadoFormulaVolume = (4 / 3) * 3.14 * (raioEsfera ** 3)

print("Volume da esfera: ", resultadoFormulaVolume)

#exercício 02

massa = float(input("Digite o peso: "))

quantidade_Agua = massa * 0.03

print("quantidade de água por peso: ", quantidade_Agua)

#exerício 04

numero_um = int(input("Primeiro número: "))
numero_dois = int(input("Segundo número: "))

if numero_um > numero_dois:
    print("Ordem crescente: ", numero_um, numero_dois)
else:
    print("Ordem crescente: ", numero_dois,numero_um)

#exercício 05

sexo = input("Digite o sexo (mulher) ou (homem): ")
altura = float(input("Altura (em metros): "))

if sexo == "homem":
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal: ", peso_ideal)
elif sexo == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal: ", peso_ideal)
else:
    print("Sexo inválido! Digite 'mulher' para feminino ou 'homem' para masculino.")