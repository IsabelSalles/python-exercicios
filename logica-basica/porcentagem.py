#Algoritmo para ler a quantidade de votos brancos, votos nulos e votos válidos de um município. 
#Calcular o número total de eleitores com base na soma dos votos informados
#Escrever o percentual que cada tipo de voto representa em relação ao total de eleitores.

votos_brancos = int(input("Insira o número de votos brancos: "))
votos_nulos = int(input("Insira o número de votos nulos: "))
votos_validos = int(input("Insira o número de votos válidos: "))
total_eleitores = votos_brancos + votos_nulos + votos_validos

porcentagem1 = (votos_brancos / total_eleitores) * 100
porcentagem2 = (votos_nulos / total_eleitores) * 100
porcentagem3 = (votos_validos / total_eleitores) * 100

print (f"Total de eleitores: {total_eleitores}")
print (f"A porcentagem dos votos brancos é: {porcentagem1}%")
print (f"A porcentagem dos votos nulos é: {porcentagem2}%")
print (f"A porcentagem dos votos válidos é: {porcentagem3}%")


