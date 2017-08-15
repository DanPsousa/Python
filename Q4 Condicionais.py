def Ordem(a,b,c):
    if a>b and a>c and c>b:
        return b,c,a
    elif b>a and b>c and a>c:
        return c,a,b
    elif c > a and c > b and b > a:
        return  a,b,c
    elif c > a and c > b and a >b:
        return b,a,c
    elif b > a and b > c and c > a:
        return a,c,b
    elif  a>b and a>c and b>c:
        return c,b,a
print(Ordem(3,32,100))

