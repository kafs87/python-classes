# Exercício 1 - Supondo que a população de um país A seja da ordem de 98.000.000 de habitantes, com uma taxa anual de crescimento de 3,5% e que um país B tenha uma população de aproximadamente 200.000.000 habitantes com uma taxa anual de crescimento de 1,5%. Escreva um algoritmo que calcule iterativamente, quantos anos serão necessários para que a população do país A, ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_a = 98000000
populacao_b = 200000000
taxa_a = 0.035
taxa_b = 0.015
anos = 0

while populacao_a <= populacao_b:

    crescimento_a = populacao_a * taxa_a
    crescimento_b = populacao_b * taxa_b
    populacao_a = populacao_a + crescimento_a
    populacao_b = populacao_b + crescimento_b

    anos += 1

print(f'\nPara que a população do país A ultrapasse a do país B, vão ser necessários se passar {anos} anos.\n')

print(f'População final do país A: {int(populacao_a)}')
print(f'População final do país B: {int(populacao_b)}\n')
print(f'O Crescimento do país A é de: {int(crescimento_a)}')
print(f'O Crescimento do país B é de: {int(crescimento_b)}')