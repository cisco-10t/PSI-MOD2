n1=float(input("insira um numero:"))
n2=float(input("insira outro numero:"))
calculos=input("quer fazer adicao, subtracao, divisao ou multiplicacao?:")
if calculos=="adicao":
    adicao=n1+n2
    print(f"a adicao dos numeros e {adicao}")
elif calculos=="subtracao":
    subtracao=n1-n2
    print(f"a subtracao dos numeros e {subtracao}")
elif calculos=="divisao":
    divisao=n1/n2
    print(f"a divisao dos numeros e {divisao}")
elif calculos=="multiplicacao":
    multiplicacao=n1*n2
    print(f"a multiplicacao dos numeros e {multiplicacao}")