
# Exercício 2 -  Elaborar um programa para automatizar o caixa de uma lanchonete. Este programa deve ler o código do item pedido, a quantidade e somar para calcular o valor a ser pago. O programa termina quando o código for 0 (zero). O cardápio da lanchonete é o seguinte:
# 100 = ['Cachorro Quente', R$3.50]
# 101 = ['Bauru Simples', R$3.80]
# 102 = ['Bauru com Ovo', R$4.50]
# 103 = ['Hambúrguer', R$4.70]
# 104 = ['X-burguer', R$5.30]
# 105 = ['Refrigerante', R$4.00]



# ler o código do item pedido, a quantidade e somar para calcular o valor a ser pago
pedido = ''
if pedido not in [100, 101, 102, 103, 104, 105, 0]:
    pedido = int(input('Digite o código do seu pedido de acordo com o cardápio (100 a 105) ou 0 para sair: '))
    quantidade = int(input('Digite a quantidade do pedido: '))

if pedido == 100: 
    cachorro_quente = 3.50
    qntd_pedido = cachorro_quente * quantidade
    print(f'O valor a ser pago será de: {qntd_pedido}')
elif pedido == 101: 
    bauru_simples = 3.80
    qntd_pedido = bauru_simples * quantidade
    print(f'O valor a ser pago será de: {qntd_pedido}')
elif pedido == 102: 
    bauru_ovo = 4.50
    qntd_pedido = bauru_ovo * quantidade
    print(f'O valor a ser pago será de: {qntd_pedido}')
elif pedido == 103: 
    hamburguer = 4.70
    qntd_pedido = hamburguer * quantidade
    print(f'O valor a ser pago será de: {qntd_pedido}')
elif pedido == 104: 
    x_burguer = 5.30
    qntd_pedido = x_burguer * quantidade
    print(f'O valor a ser pago será de: {qntd_pedido}')
elif pedido == 105: 
    refrigerante = 4.00
    qntd_pedido = refrigerante * quantidade
    print(f'O valor a ser pago será de: {qntd_pedido}')
else:
    print('Obrigado pela preferência!')
    exit()