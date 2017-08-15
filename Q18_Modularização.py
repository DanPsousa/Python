def Troca(a, b):

	a, b = b, a

	return a, b

try:

	a, b = float(input("Forneça dois valores reais: ")), float(input())

	c, d = Troca(a, b)

	print("%f\n%f" % (c, d))

except:

	print("Você não forneceu valores reais.")
