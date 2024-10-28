orcamento=float(input("quanto dinheiro tenho:"))
peso=float(input("quanto peso posso carregar:"))
while orcamento>0 or peso>0:
    preço=float(input("indique o preço do produto comprado:"))
    peso_produto=float(input("indique o peso do produto comprado:"))
    if preço==0:
        break
    if orcamento<preço or peso<peso_produto:
        print("nao tem dinheiro ou produto muito pesado")
    else:
        orcamento=orcamento-preço
        peso=peso-peso_produto
    print(f"ainda tem {orcamento}$ e ainda pode carregar mais {peso}Kg")

print("acabou as suas compras")