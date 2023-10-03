#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número para ver seu sucessor e seu antecessor: '))
sucessor = num + 1
antecessor = num - 1

print(f'O sucessor do número {num} é {sucessor}.')
print(f'O antecessor do número {num} é {antecessor}.')