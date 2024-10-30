contar=0
for _ in range(10):
    letra=input("introduz uma letra:")
    letra=letra.strip()
    if len(letra) != 1:
        print("so pode inserir uma letra")
    if letra in "aeiouAEIOU":
        contar=contar+1
print(f"introduziste {contar} vogais")