#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura

qtd_Tinta = area / 2

print(f'Sua parede tem dimensão de {largura}x{altura} e a sua área é de {area}m²')
print(f'A quantidade necessaria de tinta para pintar essa área é de {qtd_Tinta}L')
