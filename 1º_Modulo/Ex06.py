#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt


numero = int(input("Digite um número: "))
dobro = (numero * 2)
triplo = (numero * 3)
raiz_quadrada = sqrt(numero)

print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'O raiz quadrada de {numero} é {raiz_quadrada}')