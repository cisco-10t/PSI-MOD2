peso=0
preço_mala=0
while peso<1000:
    peso_mala=int(input("qual é o peso da mala?:"))
    peso=peso+peso_mala
    preço_mala=preço_mala+20
if peso==1000:
    print("o aviao chegou ao limite de peso.")
elif peso>1000:
    print("ultrapassou o limite de peso do aviao")