def Converte(minu):

	horas = minu // 60
	minuto = minu % 60

	return horas, mins

try: 

	m = int(input("Forneça o valor em minutos: "))

	horas, minuto = Converte(m)

	print("%d minutos é equivalente a %d horas e %d minutos." % (m, horas, minuto))

except:

	print("Você não forneceu um valor inteiro.")  
