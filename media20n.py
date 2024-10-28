soma = 0
m = 0
for _ in range(20):
    numero=int(input("n:"))
    if numero>=20 and numero <=50:
        soma = soma + numero
        m = m + 1
media = soma / m
print(media)
    
    