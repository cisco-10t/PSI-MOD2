n=int(input("insira o limite max: "))
for k in range(1,n):
    soma=0
    for i in range(1,k):
        resto=k%i
        if resto==0:
            soma=soma+i
    if soma==k:
        print(f"nº {k} é perfeito")
    else:
        print(f"nº {k} nao é perfeito. A soma dos seus divisores foi",soma)