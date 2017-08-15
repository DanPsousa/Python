n = int(input("Digite o primeiro número"))
m = int(input("Digite o segundo número"))
def Maior(m,n):
    if m>n:
        return "O numero maior é",m
    else:
        return "O numero maior é",n



print(Maior(m,n))