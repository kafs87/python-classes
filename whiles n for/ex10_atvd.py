# Estrutura de Repetição - While
# Programa de cálculo de média bimestral

while (True):
    resposta = ''
    print('Programa de cálculo - média bimestral')
    nome_aluno = input('Digite seu nome: ')
    nota1 = int(input('Digite sua primeira nota: '))
    nota2 = int(input('Digite sua segunda nota: '))
    media = (nota1 + nota2) / 2
    print(f'Sua média final é: {media}.')

    if (media >= 5):
        print(f'{nome_aluno}, você foi aprovado(a)!')
    elif (media >= 3):
        print(f'Você ficou de EXAME, {nome_aluno}!')
    else:
        print(f'{nome_aluno}, você foi reprovado!')

    while not ((resposta == 'n') or (resposta == 'nao') or (resposta == 'não') or (resposta == 'N') or (resposta == 's') or (resposta == 'sim') or (resposta == 'S')):
        resposta = input('\n\nVocê deseja recalcular? sim (s) / não (n)?')

    if (resposta == 'n') or (resposta == 'nao') or (resposta == 'não') or (resposta == 'N'):
        break
    else:
        print('Continuando...')