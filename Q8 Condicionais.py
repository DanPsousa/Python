n = int(input("Digite o número:"))
def Maior(n):
    if 0>n:
        return "O numero negativo"
    elif n==0:
        return "O numero é igual a zero"
    else:
        return "O numero positivo"



print(Maior(n))