# Clínica
# 19/05/2025
# Autor: ti é midia

# Biblioteca
import os

# Lista
pacientes = []

# Functions
def menu():
    print('\n\n Clínica') # Título
    print('\n\n Opções') 
    print(' 1 - Incluir')
    print(' 2 - Excluir')
    print(' 3 - Consultar')
    print(' 4 - Alterar')
    print(' 5 - Sair')

def options():
   None

def incluir():
   print('---------- Incluir ----------')
   nome = input('Digite o nome do paciente: ')
   pacientes.append(nome)
   print(f'Paciente {nome} incluído(a) com sucesso!')

def excluir():
    print('---------- Excluir ----------')
    print(pacientes)
    nome = input('Digite o nome que deseja excluir: ')
    if nome in pacientes:
       pacientes.remove(nome)
       print(f'Paciente {nome} excluído(a) com sucesso!')
    else: 
       print(f'\033[1;91m Paciente {nome} não encontrado! \033[m')
       

def consultar():
    print('---------- Consultar ----------')
    pacientes.sort()
    print(f'Pacientes incluídos: ')
    for paciente in pacientes:
        print(paciente)

def alterar():
   print('---------- Alterar ----------')

def options(select):
    if select == 1: incluir()
    elif (select == 2): excluir()
    elif (select == 3): consultar()
    elif (select == 4): alterar()
    elif (select == 5): print('Tchau!')
    else: print('Opção inválida.')

select = 0
while (select != 5):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela  

    menu() # Chama a função "menu"
    select = int(input('\033[1;92m Escolha uma opção: \033[m'))
    options(select) # Chama a função "options"

    input('\nPressione * ENTER *\n')
 