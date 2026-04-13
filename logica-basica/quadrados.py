# Crie uma função que receba 4 parâmetros inteiros e retorne a soma do quadrado desses números.


def soma_quadrados(num1, num2, num3, num4):
    quadrado1 = num1 ** 2
    quadrado2 = num2 ** 2
    quadrado3 = num3 ** 2
    quadrado4 = num4 ** 2

    soma = quadrado1 + quadrado2 + quadrado3 + quadrado4
    
    print(f"Números digitados: {num1}, {num2}, {num3}, {num4}")  
    print(f"O quadrado dos números: {quadrado1}, {quadrado2}, {quadrado3}, {quadrado4}")
    print(f"A soma dos quadrados: {soma}")
    
    return soma

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))
n4 = int(input("Insira o quarto número: "))

soma_quadrados(n1, n2, n3, n4)
    


   