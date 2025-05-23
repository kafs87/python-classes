# Cálculo de IMC
# Autor: Kauan Ferreira da Silva
# Data: 13/05/2025

# Importa a biblioteca 'os' para comandos do sistema (como limpar a tela)
import os

# Função que classifica o IMC com base na idade, sexo e valor do IMC
def classificar_imc(idade, sexo, imc):
    # Tabela com os valores de referência para IMC infantil por idade e sexo
    tabela_imc = {
        "feminino": {
            6:  (15.3, 17.1, 18.9),
            7:  (15.4, 17.4, 19.4),
            8:  (15.7, 17.8, 20.2),
            9:  (16.1, 18.4, 21.1),
            10: (16.6, 19.1, 22.1),
            11: (17.2, 20.0, 23.2),
            12: (18.0, 20.9, 24.4),
            13: (18.8, 21.9, 25.6),
            14: (19.6, 22.9, 26.7),
            15: (20.2, 23.7, 27.6),
            16: (20.7, 24.2, 28.2),
            17: (21.0, 24.7, 28.6)
        },
        "masculino": {
            6:  (15.3, 16.8, 18.3),
            7:  (15.5, 17.1, 18.8),
            8:  (15.7, 17.5, 19.4),
            9:  (16.0, 18.0, 20.1),
            10: (16.4, 18.6, 21.0),
            11: (16.9, 19.3, 22.0),
            12: (17.5, 20.1, 23.1),
            13: (18.2, 20.9, 24.2),
            14: (19.0, 21.9, 25.3),
            15: (19.8, 22.8, 26.4),
            16: (20.5, 23.7, 27.3),
            17: (21.1, 24.4, 28.0)
        }
    }

    # Converte o sexo para minúsculo para evitar erro de comparação
    sexo = sexo.lower()

    # Classificação para adultos (18 anos ou mais)
    if idade >= 18:
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        elif imc < 35:
            return "Obesidade grau 1"
        elif imc < 40:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"
    
    # Verifica se a idade está fora da faixa da tabela infantil
    if idade < 6 or idade > 17:
        return "Idade fora da faixa (6 a 17 anos para IMC infantil)."

    # Obtém os valores de referência (percentis) para o IMC infantil
    p50, p85, p97 = tabela_imc[sexo][idade]

    # Classifica com base nos percentis
    if imc < p50:
        return "Abaixo do peso"
    elif imc < p85:
        return "Peso normal"
    elif imc < p97:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Loop principal do programa para calcular o IMC de múltiplas pessoas
while True:
    # Limpa o terminal antes de cada novo cálculo
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        # Coleta o nome do usuário
        nome = input("Digite seu nome: ")
        # Coleta e converte a idade para inteiro
        idade = int(input("Digite sua idade: "))

        # Validação do sexo: aceita apenas "masculino" ou "feminino"
        while True:
            sexo = input("Digite seu sexo (masculino ou feminino): ").strip().lower()
            if sexo in ["masculino", "feminino"]:
                break
            print("Digite um sexo válido (masculino ou feminino).")

        # Coleta e converte o peso (permite vírgula como separador decimal)
        peso = float(input("Digite seu peso em kg: ").replace(',', '.'))
        # Coleta e converte a altura (permite vírgula como separador decimal)
        altura = float(input("Digite sua altura em metros: ").replace(',', '.'))

        # Cálculo do IMC
        imc = peso / (altura ** 2)

        # Exibe o resultado formatado com 2 casas decimais
        print(f"\nOlá {nome}! Seu IMC é: {imc:.2f}")
        # Chama a função de classificação e exibe o resultado
        resultado = classificar_imc(idade, sexo, imc)
        print(f"Classificação: {resultado}\n")

    # Captura erros caso o usuário insira valores inválidos
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.\n")
        input("Pressione Enter para tentar novamente...")
        continue  # Retorna ao início do loop principal
    
    # Pergunta se o usuário deseja fazer outro cálculo
    while True:
        repetir = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if repetir in ['s', 'sim']:
            break  # Reinicia o loop principal
        elif repetir in ['n', 'nao', 'não']:
            print("Encerrando o programa. Até mais!")
            exit()  # Encerra o programa
        else:
            print("Resposta inválida. Digite 's' ou 'n'.")
 