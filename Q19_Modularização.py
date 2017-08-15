def Var(hh, mm):

	return (hh * 60) + mm

try:

	hh, mm = float(input("Forneça o valor correspondente à hora atual: ")), float(input("Forneça o valor correspondente ao minuto atual: "))

	print("Se passaram %d minutos desde o início do dia." % Var(hh, mm))

except:

	print("Você não forneceu valores reais.")
