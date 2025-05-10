aprovados = 0
reprovados = 0
total_alunos = 0
while True:
    entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
    if entrada == 'sair':
        break
    nota = float(entrada)
    if 0 <= nota <= 10:
        total_alunos += 1
        if nota >= 5:
            aprovados += 1
        else:
            reprovados += 1
print()
print("Resultados:")
print(f"Quantidade de alunos que fizeram a prova: {total_alunos}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")

