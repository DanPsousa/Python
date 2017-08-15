def quest7(x, y):

	return (x + y) / (x - y)

try:

	x = float(input("Forneça dois valores reais: "))
	y = float(input())

	print(expr(x, y))

except:

	print("Você não forneceu valores reais.")
