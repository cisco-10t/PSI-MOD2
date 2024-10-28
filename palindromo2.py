palavra=input("insira uma palavra:")
palavra_invertida=""
for i in range(len(palavra)-1, -1, -1):
    palavra_invertida = palavra_invertida + palavra[i]
print(palavra_invertida)
if palavra_invertida == palavra:
    print("e um palindromo")
else:
    print("nao e um palindromo")