# Média de três notas de três alunos, e o conceito:
# Média      Conceito D
# 0 - 4,9        D
# 5 - 6,9        C
# 7 - 8,9        B
# 9 - 10         A

def solicita_nota():
    nota1 = float(input(f"Insira a primeira nota do(a) aluno(a): "))
    nota2 = float(input(f"Insira a segunda nota do(a) aluno(a): "))
    nota3 = float(input(f"Insira a terceira nota do(a) aluno(a): "))
    media = (nota1 + nota2 + nota3) / 3
    return media

def conceito(media):  
    if 0 <= media <= 4.9:
        return "D"
    elif 5 <= media <=  6.9:
        return "C"
    elif 7 <= media <= 8.9:
        return "B"
    elif 9 <= media <= 10:
        return "A"
    else: 
        return "Inválido"

aluno1 = input("Insira o nome do primeiro aluno: ")
media1 = solicita_nota()

aluno2 = input("Insira o nome do segundo aluno: ")
media2 = solicita_nota()

aluno3 = input("Insira o nome do terceiro aluno: ")
media3 = solicita_nota()

print (f"A média do(a) aluno(a) {aluno1} é: {media1} e o conceito é: {conceito(media1)}")
print (f"A média do(a) aluno(a) {aluno2} é: {media2} e o conceito é: {conceito(media2)}")
print (f"A média do(a) aluno(a) {aluno3} é: {media3} e o conceito é: {conceito(media3)}")