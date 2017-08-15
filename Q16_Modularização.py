def Quadrado(l):

	return l * l, l * 4

try:

	l = float(input("Forneça o valor correspondente à medida do lado do quadrado: "))

	a, p = Quadrado(l)

	print("A área desse quadrado é %f. O perímetro, %f." % (a, p))

except:

	print("Você não forneceu um valor real.")
