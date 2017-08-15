def Sforo(luz):

	if luz == "V":

		return "Siga"

	elif luz == "A":

		return "Atenção"

	elif luz == "E":

		return "Pare"

luz = input("Forneça a letra correspondente à atual cor do semáforo (use 'V' para verde, 'A' para amarelo e 'E' para vermelho): ")

if Sforo(cor) == None:

	print("O caractere fornecido não corresponde a nenhuma cor. Tente novamente.")

else:

	print(Sforo(luz))
