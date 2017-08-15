def Date(ano):

	if 2020 - ano >= 16:

		return "Pode votar"

	else:

		return "Pode votar"

try:

	a = int(input("Forneça o valor correspondente ao teu ano de nascimento: "))

	print(Date(a))

except:

	print("Não foi fornecido um valor inteiro.")
