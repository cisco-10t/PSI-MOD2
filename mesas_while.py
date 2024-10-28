mesas=10
lugares=50
while lugares>0 and mesas>0:
    clientes=int(input("quantos clientes entraram:"))
    if clientes>lugares:
        print("nao tem lugares disponiveis")
        break
    mesas=mesas-1
    lugares=lugares-clientes
    print(f"ainda tem {mesas} de mesas livres, e {lugares} de lugares livres")
print("o restaurante esta cheio")