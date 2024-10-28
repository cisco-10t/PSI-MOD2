frase=input("insira uma frase")

contar = 0
for letra in frase:
    if letra in "aeiouAEIOU":
        contar = contar + 1
print("A frase indicada tem ", contar, "vogais")