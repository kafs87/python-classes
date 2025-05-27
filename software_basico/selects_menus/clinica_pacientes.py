# Clínica
# Módulo: Pacientes
# 26/05/2025
# Autor: ti é midia

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

def consultar_especifica():
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
    id = int(input('Identificador do paciente: \n'))

    # Consultar para alterar
    if id in pacientes:
        id = pacientes[id] = {"id": id}
        nome = pacientes[id] = {"nome": nome}
        telefone = pacientes[id] = {"telefone": telefone}
        email = pacientes[id] = {"email": email}

        # Mostra o paciente
        consultar_geral()

        id = id

        resposta = input('Deseja alterar o nome? (s/n):').strip().lower()
        if resposta in ['s', 'sim']:
            nome = input('Nome: ')
            pacientes[id] = {"nome": nome}
            
        resposta = input('Deseja alterar o telefone? (s/n):')
        if resposta in ['s', 'sim']:
            telefone = input('Número de telefone: ')
            pacientes[id] = {"telefone": telefone}

        resposta = input('Deseja alterar o e-mail? (s/n):')
        if resposta in ['s', 'sim']:
            email = input('E-mail: ')
            pacientes[id] = {"email": email}

        pacientes[id] = {
        "id": id, 
        "nome": nome, 
        "telefone": telefone,
        "email": email
        } 

    else: 
        print(f'Paciente {id} não encontrado.')

    