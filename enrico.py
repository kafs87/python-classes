# nome = input('Insira o nome do engenheiro: ')
# salario = float(input('Qual é o salário: '))
# aluguel = 1000
# mercado = 1400
# divida = aluguel + mercado
# salario_final = salario - divida

# if salario_final < 1000:
#     print('salario menor que 1000')
# else:
#     print('salario maior que 1000')

# print(f'O salário final do {nome} é de: {salario_final:.2f}')



# pai = input('Insira o nome do pai: ')
# mae = input('Insira o nome da mãe: ')
# nome_filho1 = input('Insira o nome do primeiro filho: ')
# idade_filho1 = input('Insira quantos anos o primeiro filho tem: ')
# nome_filho2 = input('Insira o nome do segundo filho: ')
# idade_filho2 = input('Insira quantos anos o segundo filho tem: ')
# nome_filho3 = input('Insira o nome do terceiro filho: ')
# idade_filho3 = input('Insira quantos anos o terceiro filho tem: ')
# nome_filho4 = input('Insira o nome do quarto filho: ')
# idade_filho4 = input('Insira quantos anos o quarto filho tem: ')
# nome_filho5 = input('Insira o nome do quinto filho: ')
# idade_filho5 = input('Insira quantos anos o quinto filho tem: ')
# nome_filho6 = input('Insira o nome do sexto filho: ')
# idade_filho6 = input('Insira quantos anos o sexto filho tem: ')
# nome_filho7 = input('Insira o nome do sétimo filho: ')
# idade_filho7 = input('Insira quantos anos o sétimo filho tem: ')

# print(f'\n\nO sr. {pai} e a Sra. {mae} tem os filhos: {nome_filho1} com {idade_filho1} anos; {nome_filho2} com {idade_filho2} anos; {nome_filho3} com {idade_filho3} anos; {nome_filho4} com {idade_filho4} anos; {nome_filho5} com {idade_filho5} anos; {nome_filho6} com {idade_filho6} anos; {nome_filho7} com {idade_filho7} anos;')

nota = int(input('Digite sua nota: '))

if nota < 30:
    print('Reprovado.')
elif nota >= 30:
    print('Recuperação.')
elif nota <= 50:
    print('Aprovado.')
