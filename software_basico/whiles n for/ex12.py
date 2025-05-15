# Cálculo de IMC
# Autor: Kauan Ferreira da Silva
# Data: 13/05/2025

# Bibliotecas
import os

# Funções
def classificar_imc(idade, sexo, imc):
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

    # Processamento
    sexo = sexo.lower()

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
    
    if idade < 6 or idade > 17:
        return "Idade fora da faixa (6 a 17 anos para IMC infantil)."

    p50, p85, p97 = tabela_imc[sexo][idade]

    if imc < p50:
        return "Abaixo do peso"
    elif imc < p85:
        return "Peso normal"
    elif imc < p97:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Loop principal do cálculo
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))

        # Validação do sexo
        while True:
            sexo = input("Digite seu sexo (masculino ou feminino): ").strip().lower()
            if sexo in ["masculino", "feminino"]:
                break
            print("Digite um sexo válido (masculino ou feminino).")

        peso = float(input("Digite seu peso em kg: ").replace(',', '.'))
        altura = float(input("Digite sua altura em metros: ").replace(',', '.'))

        imc = peso / (altura ** 2)
        print(f"\nOlá {nome}! Seu IMC é: {imc:.2f}")
        resultado = classificar_imc(idade, sexo, imc)
        print(f"Classificação: {resultado}\n")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.\n")
        input("Pressione Enter para tentar novamente...")
        continue
    
    # Pergunta se deseja repetir
    while True:
        repetir = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if repetir in ['s', 'sim']:
            break  # Sai do loop e recomeça
        elif repetir in ['n', 'nao', 'não']:
            print("Encerrando o programa. Até mais!")
            exit()
        else:
            print("Resposta inválida. Digite 's' ou 'n'.")