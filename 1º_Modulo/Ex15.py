#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
from time import sleep
print('Carros alugados custam R$60 por dia e R$0,15 por Km rodado ')
sleep(1)
km_Rodado = int(input('Qual a quantidade de Km percorrido:Km '))
qtd_Dias = int(input('Informe qual foi a quantidade de dias em que o carro foi alugado: '))
sleep(1)
total = (60 * qtd_Dias) + (0.15 * km_Rodado)
print(f'Você precisara pagar R${total}')


