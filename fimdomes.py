dias=int(input("introduz um dia:"))
mes=int(input("introduz um mes:"))
ano=int(input("introduz um ano:"))
if mes in (1,3,5,7,8,10,12):
    faltam=31-dias
elif mes==2:
    if (ano%4==0 and ano%100!=0) or ano%400==0:
        faltam=29-dias
    else:
        faltam=28-dias
elif mes in (4,6,9,11):
    faltam=30-dias
print(f"faltam {faltam} dias para o fim do mes")