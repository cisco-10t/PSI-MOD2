maior=0
for i in range(10):
    numero=int(input("insira um numero:"))
    if i==0:
        maior=numero
else:
    if numero>maior:
        maior=numero
print("o maior e ",maior," e foi o ",pos_maior,"numero a ser inserido")