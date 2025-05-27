# Clínica
# 19/05/2025
# Autor: Kauan Ferreira

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

def confirmar(mensagem):
   resposta = input(mensagem)
   while resposta not in ['n', 'nao', 'não', 's', 'sim']:
      resposta = input('Resposta inválida. ' + mensagem)
   if resposta in ['n', 'nao', 'não']:
      return print('\033[1;91mNenhuma mudança foi realizada.\033[m')
   return resposta in ['s', 'sim']

def incluir():
   print('---------- Incluir ----------')
   nome = input('Digite o nome do paciente: ')
   pacientes.append(nome)
   print(f'Paciente {nome} incluído(a) com \033[1;92msucesso\033[m!')

def excluir():
   print('---------- Excluir ----------')
   print(pacientes)
   if pacientes == []:
      print('\nLista de pacientes vazia.')
   else:
      nome = input('\nDigite o nome que deseja excluir: ')
      if nome in pacientes:
         if confirmar(f'Deseja excluir o paciente {nome}: s/n:'):
            pacientes.remove(nome)
            print('Nome do paciente excluído com \033[1;92msucesso\033[m!')
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
   print(pacientes)
   if pacientes == []:
      print('\nLista de pacientes vazia.')
   else:
      nome = input('\nDigite o nome que deseja alterar: ')

      if nome in pacientes:
         novo_nome = input('Digite o novo nome: ')
         if confirmar(f'Deseja alterar o paciente {nome} para {novo_nome}? (s/n):'):
            alteracao = pacientes.index(nome)
            pacientes[alteracao] = novo_nome
            print('Nome do paciente alterado com \033[1;92msucesso\033[m!')
      else:
         print(f'\033[1;91m Paciente {nome} não encontrado! \033[m')

def options(select):
    if select == 1: incluir()
    elif (select == 2): excluir()
    elif (select == 3): consultar()
    elif (select == 4): alterar()
    elif (select == 5): print('Até mais!')
    else: print('Opção inválida.')

select = 0
while (select != 5):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela  

    menu() # Chama a função "menu"
    select = int(input('\033[1;92m Escolha uma opção: \033[m'))
    options(select) # Chama a função "options"

    input('\n \033[0;32;4m Pressione ENTER para continuar. \033[m \n')
 