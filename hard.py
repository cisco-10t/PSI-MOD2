anos=int(input("quantos anos tens?:"))
if anos<10:
    print("classe infantil")
elif anos>=10 and anos<14:
    print("classe de iniciados")
elif anos>=14 and anos<18:
    print("class3 de juniores")
elif anos>=18 and anos<40:
    print("classe senior")
elif anos>=40 and anos<=100:
    print("provavelmente esta reformado")
elif anos>100:
    print("foi jogar no vasco")