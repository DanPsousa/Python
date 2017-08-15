def Dezenas(n):

	num = str(n)

	if len(num) == 3:

		c = n // 100 
		d = (n - (c * 100)) // 10
		
		return d

	else:

		return 71

n = int(input("Forneça um número inteiro com três algarismos: "))

if Dezenas(n) == 71:

	print("Você não forneceu um número com três algarismos.")

else:

	print("O algarismo das dezenas é %d." % (Dezenas(n)))
