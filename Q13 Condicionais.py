def Par(v):
    if (v%2)==0 and (v%3)==0:
        return "O numero é par divisivel por 3"
    else:
        return "O numero não esta entre as condições necessarias"
print(Par(15))