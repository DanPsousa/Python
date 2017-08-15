def dif(nome, sex):

	if sex.lower() == "masculino":

		return "\nIlmo. Sr. %s [...]" % nome

	elif sex.lower() == "feminino":

		return "\nIlmo. Sra. %s [...]" % nome

	else:

		return "O sexo não pôde ser identificado."

nome, sex = input("Nome: "), input("Sexo: ")

print(dif(nome, sexo))
