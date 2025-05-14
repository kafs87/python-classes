# Programa de Verificação do Cargo
# 07/04/2025

print('\nPrograma de Verificação do Cargo\n')
nome = input('Insira seu nome: ')
cod = int(input('Digite o código do cargo: '))

if cod == 1:
    cod_s = 'Escriturário'
elif cod == 2:
    cod_s = 'Secretária'
elif cod == 3:
    cod_s = 'Caixa'
elif cod == 4:
    cod_s = 'Gerente'
elif cod == 5:
    cod_s = 'Diretor'
elif cod == 6:
    cod_s = 'Diretor'
else:
    cod_s = 'Inválido'

if cod_s != "Inválido":
    print(f'\n\n{nome}, de acordo com seu código de cargo {cod}, a descrição do seu cargo é {cod_s}.')
else: 
    print('Código inválida!')