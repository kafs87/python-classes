# Exercício 01 - Como podemos criar uma lista em Python com cinco nomes de frutas e exibi-la na tela?

print('\n========== EXERCICIO 01 ==========')

lista_frutas = ['Laranja', 'Banana', 'Uva', 'Morango', 'Abacate']
print(lista_frutas)

# Exercício 02 - Como acessar o primeiro e o último elemento de uma lista em Python?

print('\n========== EXERCICIO 02 ==========')

print('Acesso pelo índice positivo.')
print(lista_frutas[3])
print('Acesso pelo índice negativo.')
print(lista_frutas[-4])

# Exercício 03 - Como adicionar um novo item a uma lista em Python?

print('\n========== EXERCICIO 03 ==========')

# .append() - Para adicionar no fim da lista
lista_frutas.append('Maçã')
print(lista_frutas,)
# .insert() - Para adicionar em uma posição desejada
lista_frutas.insert(2, 'Manga')
print(lista_frutas)
# .extend() - Para adicionar vários itens de uma vez
lista_frutas.extend(['Kiwi', 'Melancia'])
print(lista_frutas)

# Exercício 04 - Como descobrir quantos elementos existem dentro de uma lista em Python?

print('\n========== EXERCICIO 04 ==========')

print('Tamanho da lista: ', len(lista_frutas))

# Exercício 05 - Como substituir um elemento específico da lista por outro valor?

print('\n========== EXERCICIO 05 ==========')

lista_frutas[0]='Abacaxi'
print(lista_frutas)

# Exercício 06 - Como criar uma lista contendo os números de 1 a 10?

print('\n========== EXERCICIO 06 ==========')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_numeros)

# Exercício 07 - Como calcular a soma de todos os elementos da lista?

print('\n========== EXERCICIO 07 ==========')

soma = sum(lista_numeros)
print(soma)

# Exercício 08 - Como encontrar o maior e o menor valor da lista?

print('\n========== EXERCICIO 08 ==========')

maior = max(lista_numeros)
menor = min(lista_numeros)
print('Maior: ', maior)
print('Menor: ', menor)

# Exercício 09 - Como unir duas listas diferentes em uma terceira lista?

print('\n========== EXERCICIO 09 ==========')

juncao_das_listas = lista_frutas + lista_numeros
print(juncao_das_listas)

# Exercício 10 - Como substituir um elemento específico da lista por outro valor?

print('\n========== EXERCICIO 10 ==========')

lista_numeros[5]='SEIS'
print(lista_numeros)