nome = input('Insira o nome do engenheiro: ')
salario = float(input('Qual é o salário: '))
aluguel = 1000
mercado = 1400
divida = aluguel + mercado
salario_final = salario - divida

if salario_final < 1000:
    print('salario menor que 1000')
else:
    print('salario maior que 1000')

print(f'O salário final do {nome} é de: {salario_final:.2f}')