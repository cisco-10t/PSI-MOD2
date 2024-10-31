numero=float(input("insira um numero:"))
soma=0
numero=numero+0.5
for i in range(10):
    print(numero,end=" , ")
    soma=soma+numero
    numero=numero+0.5
print(f"a soma dos numeros é {soma}")
