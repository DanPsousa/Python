def quest17(a, b):

	if a % 2 == 0 and b % 2 == 0:

		return "Os dois são pares"

	elif a % 2 != 0 and b % 2 != 0:

		return "Os dois são ímpares"

	elif a % 2 == 0 and b % 2 != 0:

		return "O primeiro é par e o segundo é ímpar"

	elif a % 2 != 0 and b % 2 == 0:

		return "O primeiro é ímpar e o segundo é par"

try:

	a, b = int(input("Forneça dois números inteiros: ")), int(input())

	print(quest17(a, b))

except:

	print("Não foram fornecidos valores inteiros.")
