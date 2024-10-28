musica=1
tempo=0
while musica>0 or musica<6000:
    musica=int(input("Insere o tempo da musica em segundos:"))
    if musica<=0 or musica>=6000:
        break
    else:
        tempo=tempo+musica
duracao_album=tempo/60
parte_decimal=duracao_album-int(duracao_album)
segundos=60*parte_decimal
print(f"o album tem {int(duracao_album)} minutos e {int(segundos)} segundos")