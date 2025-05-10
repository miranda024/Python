def exibir_mensagem(mensagem, numero):
    print("Mensagem:", mensagem)
    print("Número:", numero)
if __name__ == '__main__':
    msg = input("Digite uma mensagem: ")
    num = int(input("Digite um número: "))
    exibir_mensagem(msg, num)
