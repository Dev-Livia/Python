#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


temp = float(input('Informe a temperatura em graus Celsius: '))

temp_Fahrenheit = (temp * 1.8) + 32

print(f'A temperatura em Celsius Cº {temp}, passa a ser Fº {temp_Fahrenheit} em Fahrenheit')