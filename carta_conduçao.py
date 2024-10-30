pontos=12
op=0
leve=0
grave=0
mtgrave=0
while op!=4:
    op=int(input("o condutor cometeu uma infração: Muito Grave(1), Grave(2), Leve(3) e se não cometeu nada ou quer terminar, Terminar(4): "))
    if op==1:
        mtgrave=mtgrave+1
        pontos=pontos-6
    elif op==2:
        grave=grave+1
        pontos=pontos-4
    elif op==3:
        leve=leve+1
        if leve>1:
            pontos=pontos-1
    if grave+mtgrave==2 or grave==2 or pontos<=0 :
        print("o condutor perdeu a carta")
    print(f"o condutor esta com {pontos} pontos na carta.")