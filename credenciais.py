email="cisco1234@gamil.com"
palavra_pass="nsei7"
mail="1"
passc="1"
contar_tentativas=0
while mail!=email and passc!=palavra_pass:
    mail=input("insira o email: ")
    passc=input("insira a palavra_pass: ")
    contar_tentativas=contar_tentativas+1
    if contar_tentativas==3:
        break
    if mail!=email and passc!=palavra_pass:
        print("o login falhou")
    elif mail!="cisco1234@gmail.com":
        print("email invalido")
    else:
        print("palavra_pass incorreta")
    