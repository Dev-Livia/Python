#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite algo para ver seu tipo primitivo: ')
tipo = type(entrada)

print('O tipo primitivo desse valor é ',type(tipo))
print('Só tem espaços? ',tipo.isspace())
print('é um número? ', tipo.isnumeric())
print('é alfabetico? ', tipo.isalpha())
print('é alfanúmerico? ',tipo.isalnum())
print('Está em maiusculas ?',tipo.isupper())
print('Está em minusculas ?',tipo.islower())
print('Está captalizada ?',tipo.istitle())