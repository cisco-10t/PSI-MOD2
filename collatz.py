n=int(input("insira uma numero: "))
contar=0
while n!=1:
    print(int(n))
    if n%2==0:
        n=n/2
    else:
        n=n*3+1
    contar=contar+1
if n==1:
    print(f"1\nForam precisos {contar} passos ate ao 1")