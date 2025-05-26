#Exercício 3 - Elaborar um algoritmo que simule o jogo de adivinhação: o jogador 1 escolhe um número entre 1 e 10; o jogador 2 insere números na tentativa de acertar o número escolhido pelo jogador 1. Quando ele acertar, o algoritmo deve informar que ele acertou o número escolhido pelo jogador 1 em x tentativas (quantidade de tentativas do jogador 2).

import os

while True:
    escolha = int(input('\nJogador 1, escolha um número de 1 a 10: '))

    while escolha <= 0 or escolha > 10:
        print('Número inválido.')
        escolha = int(input('\nDigite outro valor, de 1 a 10: '))

    chute = None
    tentativas = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    while chute != escolha:
        chute = int(input('\nJogador 2, adivinhe o número escolhido de 1 a 10: '))
        if chute <= 0 or chute > 10:
            print('Número inválido, digite um número de 1 a 10.')
        elif chute < escolha:
            print('Errou! O número escolhido é maior.')
        elif chute > escolha:
            print('Errou! O número escolhido é menor.')

        tentativas += 1
    print(f'Parabéns, você descobriu o número com {tentativas} tentativa(s).')

    resposta = input('\nVocê deseja jogar novamente? (s/n):').lower().strip()
    while resposta not in ['s', 'sim', 'n', 'nao', 'não']:
        resposta = input('Resposta inválida. Deseja jogar novamente? (s/n):').lower().strip()

    if resposta in ['n', 'nao', 'não']:
        print('Encerrando o jogo, até mais!')
        break
    else:
        print('Recomeçando...')