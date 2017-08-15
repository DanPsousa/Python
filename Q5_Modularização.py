def Metro(m):

	return m * 3.6

try:

	m = float(input("Forneça o valor correspondente à medida em m/s: "))

	print("%f m/s correspondem a %f km/h." % (m, Metro(m)))

except:

	print("Você não forneceu um valor real.")
