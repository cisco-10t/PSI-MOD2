numero=int(input("introduza um numero inteiro:"))
for i in range(numero,0,-1):
    if numero%i==0:
        print(i)