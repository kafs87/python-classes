# Clínica
# Módulo: Pacientes
# 26/05/2025
# Autor: Kauan Ferreira

pacientes = {} #chave: identificador (id) -> pacientes{"id": id, "nome": nome, "celular": celular}

# Procedures / Functions
def cadastrar():
    print('\n--- Cadastro de Paciente ---\n')
    id = int(input(f'Identificador do paciente: '))

    # Consultar para inserir
    if id in pacientes: 
        print(f'Paciente {id} já cadastrado.')
    else: 
        nome = input('Nome: ')
        telefone = input('Número de telefone: ')
        email = input('E-mail: ')

        # Insert
        pacientes[id] = {
            "id": id, 
            "nome": nome, 
            "telefone": telefone,
            "email": email
        }
        print('Paciente cadastrado(a) com sucesso!')

def consultar_rapida():
    print('\n--- Consulta rápida do Paciente ---\n')
    print('Nome')
    print('-' * 40)
    for id in pacientes:
        print(pacientes[id].get('nome'))

def consultar_geral():
    print('\n--- Consulta geral do Paciente ---\n')
    print('Id | Nome | Número de telefone | E-mail')
    print('-' * 40)
    for id in pacientes:
        print(pacientes[id].get('id'), "-", pacientes[id].get('nome'), "-", pacientes[id].get('telefone'),  "-", pacientes[id].get('email'))

def excluir():
    print('\n--- Exclusão de Paciente ---\n')
    id = int(input('Identificador do Paciente: '))

    # Consultar para excluir
    while True:
        if id in pacientes:
            resposta = input(f'Você realmente deseja excluir o paciente {id}? (s/n)').strip().lower()

            while resposta not in ['n', 'nao', 'não', 's', 'sim']:
                resposta = input(f'Resposta inválida. Você realmente deseja excluir o paciente {id}? (s/n)')

            if resposta in ['s', 'sim']:
                del pacientes[id]
                print(f'Paciente {id} excluído com sucesso.')
                break
            else:
                print('Paciente não excluído.')
                break
        else: 
            print(f'Paciente {id} não encontrado.')

def alterar():
    print('\n--- Alteração de Paciente ---\n')
    id = int(input('Identificador do paciente: '))

    if id in pacientes:
        paciente = pacientes[id]

        print(f"\nPaciente atual:\nID: {paciente['id']}\nNome: {paciente['nome']}\nTelefone: {paciente['telefone']}\nEmail: {paciente['email']}\n")

        resposta = input('Deseja alterar o nome? (s/n): ').strip().lower()
        if resposta in ['s', 'sim']:
            paciente['nome'] = input('Novo nome: ')

        resposta = input('Deseja alterar o telefone? (s/n): ').strip().lower()
        if resposta in ['s', 'sim']:
            paciente['telefone'] = input('Novo telefone: ')

        resposta = input('Deseja alterar o e-mail? (s/n): ').strip().lower()
        if resposta in ['s', 'sim']:
            paciente['email'] = input('Novo e-mail: ')

        pacientes[id] = paciente  # Atualiza o dicionário
        print(f'\nPaciente {id} alterado com sucesso!')

    else:
        print(f'Paciente {id} não encontrado.')


    