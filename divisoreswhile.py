numero=int(input("introduza um numero inteiro:"))
divisor=numero
while divisor>0:
    if numero%divisor==0:
        print(divisor)
    divisor=divisor-1