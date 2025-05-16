# Funções e Procedimentos - Ex 5:
# Efetuar o cálculo do pagamento salarial considerando a quantidade de horas semanais e o valor por hora de trabalho
# Função construída

# Procedimento 
def titulo_do_sistema():
    print('\n\n*** Cálculo - Pagamento Salarial***')

# Declaração / Construção da Função
def calcular_pagamento(qtd_horas_sem, valor_por_hora):
    horas = qtd_horas_sem
    taxa = valor_por_hora
    if (horas <= 40):
        salario = horas * taxa
    else:
        h_exced = horas - 40
        salario = (40 * taxa) + (h_exced * (1.5 * taxa))
    return salario
def quadrado(parametro_num):
    return (parametro_num * parametro_num)
def dobro(parametro_num):
    return (parametro_num * 2)
def triplo(parametro_num):
    return (parametro_num * 3)

# Início 
titulo_do_sistema() # Título

qtd_horas = int(input("Quantidade de horas da semana: ")) # Entrada
valor_hora = float(input("Valor por hora (v/h): ")) # Entrada

# Sáida e Processamento
print(f"\nO salário bruto é {calcular_pagamento(qtd_horas, valor_hora)}.") 