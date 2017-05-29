l=float(input("Digite o lado do terreno em metros:"))
c=float(input("Digite o valor do comprimento do terreno em metros:"))
if c==l:
    print("O valor da area deste terreno tem que ter valores diferentes de comprimento e lado")
else:
    print("O valor da area deste terreno em metros quadrados é :",c*l)