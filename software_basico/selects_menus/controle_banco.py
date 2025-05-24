# Controle bancário - Conta
# 19/05/2025
# Autor: ti é midia

# Biblioteca
import os

# Lista
saldo = []

# Functions
def menu():
    print('\n\n Controle de Conta Bancária') # Título
    print(' 1 - Depósito')
    print(' 2 - Saque')
    print(' 3 - Consultar o Saldo')
    print(' 4 - Extrato')
    print(' 5 - Sair')

def options(select):
    if (select == 1):
        print('---------- Depósito ----------')
        deposito()
    elif (select == 2):
        print('---------- Saque ----------')
        saque()
    elif (select == 3):
        print('---------- Consultar o Saldo ----------')
        consulta()
    elif (select == 4):
        print('---------- Extrato ----------')
        extrato()
    elif (select == 5):
        print('Tchau!')
    else: 
        print('Opção inválida.')

def senha():
    senha = ''
    while senha != 'abc123':
        senha = input('Digite a senha para prosseguir: ')
    else: 
        print('Ação concluída!!')

def deposito():
    valor = float(input('Digite a quantia que deseja depositar: '))
    senha()
    saldo.append(valor)
    print(f'Depósito de R${valor} realizado com sucesso!')

def saque():
    valor = float(input('Digite a quantia que deseja sacar: '))
    if ((sum(saldo)-valor) < 0):
        print ('\033[1;91m ATENÇÃO! Não há limite disponível em sua conta - Saldo negativo \033[m')
    else:
        senha()
        saldo.append(-valor)
        print(f'Saque de R${valor} realizado com sucesso!')

def consulta():
    print(f'Saldo disponível: {sum(saldo)}')

def extrato():
    print(f'Saldo disponível: {sum(saldo)}')
    print(f'Extrato: {saldo}')

select = 0
while (select != 5):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela  

    menu() # Chama a função "menu"
    select = int(input('Escolha uma opção: '))
    options(select) # Chama a função "options"

    input('\nPressione * ENTER *\n')
 