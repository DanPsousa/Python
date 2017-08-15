def Verifica(n):

	num = str(n)

	if len(num) == 3:

		return num

	else:

		return 0

n = int(input("Forneça um número de três algarismos: "))

if verifica(n) == 0:

	print("Você não forneceu um número de três algarismos.")

else:

	print(verifica(n)[::-1])
