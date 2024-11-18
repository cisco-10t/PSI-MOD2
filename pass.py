alfabetom="abcdefghijklmnopqrstuvwxyz"
alfabetoM="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="1234567890"
caracteres="!?@€.,;:-_"
TEM_m=False
TEM_M=False
TEM_n=False
TEM_s=False
tamanho=False
passe=input("insira uma palavra_passe pra testar: ")
for letra in alfabetom:
    if letra in passe:
        TEM_m=True
        break
for letra in alfabetoM:
    if letra in passe:
        TEM_M=True
        break
for letra in n:
    if letra in n:
        TEM_n=True
        break
for letra in caracteres:
    if letra in caracteres:
        TEM_s=True
        break
if len(passe)>=8:
    tamanho=True
if TEM_m==True and TEM_M==True and TEM_n==True and TEM_s==True and tamanho==True:
    print("palavra_pass segura")
else:
    print("a palavra_pass nao e segura")