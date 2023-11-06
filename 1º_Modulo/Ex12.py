#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Informe o valor do produto: R$ '))
desconto = produto - (produto * 5 / 100 )

print(f'O produto custava R${produto} e com o desconto de 5%')
print(f'passou a custar R${desconto}')