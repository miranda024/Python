#ex3
n_um=int(input('primeiro número: '))
n_dois=int(input('segundo número: '))
n_tres=int(input('terceiro número: '))
if n_um >= n_dois and n_um >=n_tres:
    print('o maior valor é:',n_um)
elif n_dois >= n_um and n_dois >= n_tres:
    print('o maior valor é:',n_dois)
else:
    print('o maior valor é:',n_tres)