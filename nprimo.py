primo=int(input("primo:"))
for i in range(2,primo):
    if primo %i== 0:
        print("nao e primo")
        break
    else:
        print("e primo")
        break