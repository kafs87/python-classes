
# Exercício 2 -  Elaborar um programa para automatizar o caixa de uma lanchonete. Este programa deve ler o código do item pedido, a quantidade e somar para calcular o valor a ser pago. O programa termina quando o código for 0 (zero). O cardápio da lanchonete é o seguinte:
# 100 = ['Cachorro Quente', R$3.50]
# 101 = ['Bauru Simples', R$3.80]
# 102 = ['Bauru com Ovo', R$4.50]
# 103 = ['Hambúrguer', R$4.70]
# 104 = ['X-burguer', R$5.30]
# 105 = ['Refrigerante', R$4.00]

print('100 = | Cachorro Quente | R$3.50')
print('101 = | Bauru Simples   | R$3.80')
print('102 = | Bauru com Ovo   | R$4.50')
print('103 = | Hambúrguer      | R$4.70')
print('104 = | X-burguer       | R$5.30')
print('105 = | Refrigerante    | R$4.00')

valor_total = 0
while True:
    pedido = int(input('Digite o código do seu pedido de acordo com o cardápio ou 0 para sair: '))
    if pedido == 0: 
        break
    elif pedido == 100: 
        cachorro_quente = 3.50
        quantidade = int(input('Digite a quantidade do pedido: '))
        qntd_pedido = cachorro_quente * quantidade
        valor_total += qntd_pedido
        print(f'O valor a ser pago será de: {qntd_pedido}')

    elif pedido == 101: 
        bauru_simples = 3.80
        quantidade = int(input('Digite a quantidade do pedido: '))
        qntd_pedido = bauru_simples * quantidade
        valor_total += qntd_pedido
        print(f'O valor a ser pago será de: {qntd_pedido}')

    elif pedido == 102: 
        bauru_ovo = 4.50
        quantidade = int(input('Digite a quantidade do pedido: '))
        qntd_pedido = bauru_ovo * quantidade
        valor_total += qntd_pedido
        print(f'O valor a ser pago será de: {qntd_pedido}')

    elif pedido == 103: 
        hamburguer = 4.70
        quantidade = int(input('Digite a quantidade do pedido: '))
        qntd_pedido = hamburguer * quantidade
        valor_total += qntd_pedido
        print(f'O valor a ser pago será de: {qntd_pedido}')

    elif pedido == 104: 
        x_burguer = 5.30
        quantidade = int(input('Digite a quantidade do pedido: '))
        qntd_pedido = x_burguer * quantidade
        valor_total += qntd_pedido
        print(f'O valor a ser pago será de: {qntd_pedido}')

    elif pedido == 105: 
        refrigerante = 4.00
        quantidade = int(input('Digite a quantidade do pedido: '))
        qntd_pedido = refrigerante * quantidade
        valor_total += qntd_pedido
        print(f'O valor a ser pago será de: {qntd_pedido}')

print(f'Obrigado pela preferência! Seu pedido total foi de: {valor_total}')