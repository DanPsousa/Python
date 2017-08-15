n=11
while n>10 or n<0:
    n=int(input("Digite um numero:"))
    if n>0 and n<10:
        break
    else:
        n=int(input("Numero anterior invalido digite um numero novamente:"))
print("Concluido")
