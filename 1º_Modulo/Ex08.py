#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = int(input('Digite um número em metros: '))

cent = metros * 100
mili = metros * 1000

print(f'{metros} convertidos em centimetros é igual {cent}.')
print(f'{metros} convertidos em milímetros é igual {mili}.')