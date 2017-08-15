def quest13(x):

	return x % 2 == 0 and x % 3 == 0

try:

	x = int(input("Forneça um valor inteiro: "))

	print(quest13(x))

except:

	print("Não foi fornecido um valor inteiro.")
