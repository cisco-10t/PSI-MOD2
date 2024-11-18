melhor_nota=-1
numero_aluno=-1
nr_alunos=int(input("insira o n de alunos:"))
for i in range(nr_alunos):
    nota=int(input(f"nota do aluno nº {i+1}: "))
    if nota>melhor_nota:
        melhor_nota=nota
        numero_aluno=i+1
print("o aluno com melhor nota é o n",numero_aluno)