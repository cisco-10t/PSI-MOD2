n=int(input("insira um numero: "))
soma_divisores=0
for i in range(1,n):
    if n%i==0:
        soma_divisores=soma_divisores+i
if soma_divisores==n:
    print("É perfeito")
else:
    print("Nao é perfeito")