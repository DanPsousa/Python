d = []
soma = 0

x = int(input("Forneça números inteiros e positivos (0 encerra): "))

if x == 0:

	pass

else:
 
	while x != 0:
	 
	    if x == 0:
	 
	        break
	 
	    x = int(input())
	 
	    if x % 3 == 0:
	 
	        d.append(x)
	 
	for c in range(len(y)):
	 
	    soma += d[c]
	 
print("A média dos números múltiplos de três dentre os fornecidos (0 não considerado) é: %d" % (soma / int(len(y) - 1)))
