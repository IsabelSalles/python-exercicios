#Elabore um algoritmo para ler o salário base e a gratificação de um funcionário.
#Calcular o salário bruto, somando o salário base com a gratificação.
#Se o salário bruto for menor que 1000, descontar 15% de imposto de renda (IR).
#Caso contrário, descontar 20% de imposto de renda (IR).

salario_base = float(input("Insira o salário base: R$ "))
gratificacao = float(input("Insira o valor da gratificação: R$ "))
salario_bruto = salario_base + gratificacao

if salario_bruto < 1000:
    ir = (salario_bruto * 15) / 100
else:
    ir = (salario_bruto * 20) / 100

salario_liquido = salario_bruto - ir

print (f"Salário bruto: R$ {salario_bruto:.2f}")
print (f"Salário Base: R$ {salario_base}")
print (f"Imposto de renda: R$ {ir}")
print (f"Salario líquido: R$ {salario_liquido}")
