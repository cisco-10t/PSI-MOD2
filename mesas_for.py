mesas = 10
lugares = mesas * 50

for mesas_ocupadas in range(mesas):
    clientes =int(input("quantas pessoas entraram:"))
    if clientes>lugares:
        print("nao tem lugares para tantos clientes")
        break
    mesas = mesas - 1
    lugares = lugares - clientes
    print("mesas ocupadas: ",mesas_ocupadas)
    print("lugares disponiveis: ",lugares)
