#Faça	uma	função	que	recebe	três	números	por	parâmetro	e	imprime	na	tela	em	ordem	crescente.
def imprimeOrdemcrescente(a,b,c):
    if a < b and a < c :
        if b < c :
           print(a,b,c)
        else:
            print(a,b,c)
    elif (b < a) and (b < c) :
        if a < c :
            print(b,a,c)
        else:
            print(b,c,a)
    else: #C e o menor
        if a < b:
            print(c,a,b)
        else:
            print(c,b,a)
imprimeOrdemcrescente(30,20,10)
