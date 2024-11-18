saldo=0
escolha=0
while escolha!=4:
    print("ATM\n1. ver o saldo\n2.depositar\n3.levantar\n4.terminar")
    escolha=int(input())
    if escolha==1:
        print(saldo)
    if escolha==2:
        valor=float(input("valor a depositar: "))
        if valor<=0.01 or valor>10000:
            print("o valor nao e valido")
        else:
            saldo=saldo+valor
            print("o seu saldo atualmente é de",saldo)
    if escolha==3:
        valor=float(input("qual o valor a levantar: "))
        if valor<10 or valor>400 or valor>saldo:
            print("valor indicado nao valido")
        else:
            saldo=saldo-valor
            print("o seu saldo atualmente e",saldo)