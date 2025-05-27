# Clínica
# Módulo: Principal / Main
# 26/05/2025
# Autor: ti é midia

# Biblioteca
import os
import clinica_pacientes

# Dicionário
pacientes = {} #chave: identificador (id) -> pacientes{"id" = id, "nome" = nome, "celular" = celular}

# Functions
def menu():
    print('\n\n Clínica') # Título
    print('\n\n Menu de opções: ') 
    print('\33[32m 1 - Cadastrar \33[m')
    print('\33[96m 2 - Consulta Rápida\33[m')
    print('\33[93m 3 - Consulta Geral\33[m')
    print('\33[94m 4 - Alterar\33[m')
    print('\33[91m 5 - Excluir\33[m')
    print('\33[95m 0 - Sair\33[m')

def options(select):
    if select == 1: clinica_pacientes.cadastrar()
    elif (select == 2): clinica_pacientes.consultar_rapida()
    elif (select == 3): clinica_pacientes.consultar_geral()
    elif (select == 4): clinica_pacientes.alterar()
    elif (select == 5): clinica_pacientes.excluir()
    elif (select == 0): print('Tchau!')
    else: print('Opção inválida.')

select = None
while (select != 0):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela  

    menu() # Chama a função "menu"
    select = int(input('\033[1;92m Escolha uma opção: \033[m'))
    options(select) # Chama a função "options"

    input('\n \033[0;32;4m Pressione ENTER para continuar. \033[m \n')
 