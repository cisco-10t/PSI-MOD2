numero=int(input("insira o nº a testar:"))

primo=True

for X in range(2,numero):
    if numero % X == 0:
        primo=False
if primo ==True:
    print("o nº", numero, " é primo")
else:
    print("o nº", numero, " nao e primo")