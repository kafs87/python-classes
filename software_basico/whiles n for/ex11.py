# Estrutura de Repetição - While
# Programa de Simulação de Menu

select = 0
while (select != 5):

    print('\n\n Controle de Produtos') # Título

    print(' 1 - Incluir')
    print(' 2 - Consultar')
    print(' 3 - Alterar')
    print(' 4 - Excluir')
    print(' 5 - Sair')

    select = int(input('Escolha uma opção: '))

    if (select == 1):
        print('Você escolheu Incluir')
    elif (select == 2):
        print('Você escolheu Consultar')
    elif (select == 3):
        print('Você escolheu Alterar')
    elif (select == 4):
        print('Você escolheu Excluir')
    else:
        print('Tchau!')
