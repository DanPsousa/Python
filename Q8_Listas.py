num=[int(input("Digite um numero:")),int(input("Digite um numero:")),int(input("Digite um numero:")),int(input("Digite um numero:")),int(input("Digite um numero:"))]
i=0
c=0
multi=1
while (i<5) :
  c+=num[i]
  multi*=num[i]
  i+=1
print("A soma é", c ,"e a multiplicação é",multi ,"os numeros são", num)
