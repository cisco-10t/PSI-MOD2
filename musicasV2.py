musica=1
duraçao_total=0
while musica!=0:
    musica=int(input("duraçao da musica em segundos (0 para terminar):"))
    if musica<0 or musica >=6000:
        print("duraçao nao pode ser inferir a 0 e superior a 6000")
        continue
        duraçao_total=duraçao_total+musica
minutos=duraçao_total//60
segundos=duraçao_total%60
