def quest(x):

	if x > 20:

		return "Vá ao cinema"

	else:

		return "Fique vendo TV"

try:

	x = float(input("Quanto dinheiro você tem (em R$): "))

	print(quest(x))

except:

	print("Não foi fornecido um valor real.")
