def fibonacci(n):
    a, b = 0, 1

    for i in range (n):
        a,b = b, a+b

    return a

n = int(input("Digite o numero: "))
l=fibonacci(n)
print("O valor de fibonacci do numero %d eh %d" %(n,l))

