# Data completa
# 07/04/2025

print('\n*** Data completa ***')

def meses(p_mes):
    if p_mes == 1:
        return 'Janeiro'
    elif p_mes == 2:
        return 'Fevereiro'
    elif p_mes == 3:
        return 'Março'
    elif p_mes == 4:
        return 'Abril'
    elif p_mes == 5:
        return 'Maio'
    elif p_mes == 6:
        return 'Junho'
    elif p_mes == 7:
        return 'Julho'
    elif p_mes == 8:
        return 'Agosto'
    elif p_mes == 9:
        return 'Setembro'
    elif p_mes == 10:
        return 'Outubro'
    elif p_mes == 11:
        return 'Novembro'
    elif p_mes == 12:
        return 'Dezembro'
    else:
        return None

nome = input('\nDigite seu nome: ')
dia = int(input('Digite o dia de hoje (dd): '))
mes = int(input('Digite o mês de hoje (mm): '))
ano = int(input('Digite o ano de hoje (aaaa): '))


if meses(mes) is not None:
    print(f'\n\n{nome}, hoje é dia {dia} de {meses(mes)} de {ano}.')
else: 
    print('Data inválida!')