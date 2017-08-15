def Vogal(vog):

	return vog == "a" or vog == "e" or vog == "i" or vog == "o" or vog == "u"

vog = input("Forneça uma letra: ")

if len(vog) == 1:

	print(Vogal(vog))

else:

	print("Somente uma letra deve ser fornecida.")
