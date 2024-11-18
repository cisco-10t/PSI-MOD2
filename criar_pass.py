import random
A_M="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ppasse=""
for i in range(2):
    pos=random.randint(0, len(A_M))
    ppasse=ppasse+A_M[pos]