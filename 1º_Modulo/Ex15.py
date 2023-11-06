#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
from time import sleep
print('Os salarios a partir de hoje terão um ajuste de 15%')
sleep(1)
salario = float(input('Informe sua renda: R$'))
aumento = salario + (salario * 15 / 100)

print(f'Seu salário de R${salario:.2f} com o reajuste passou a ser R${aumento:.2f}')
