n1=int(input("insira um numero:"))
n2=int(input("insira um numero:"))
if n1==n2:
    print("iguais")
else:
    print("diferentes")
    diferenca=n1-n2
    if diferenca<0:
        diferenca=diferenca*(-1)
    print(diferenca)