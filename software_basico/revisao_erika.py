# Lista de produtos disponíveis na loja
estoque_produtos = ["1 - Celular", "2 - Notebook", "3 - Fones de ouvido", "4 - Câmera"]
carrinho = []  # Lista para armazenar os produtos escolhidos

# Exibir os produtos disponíveis
print(" Produtos disponíveis na loja:")
for produto in estoque_produtos:
    print(f"{produto}")

# Solicitar que o usuário escolha produtos ou pede novamente se valor inserido for inválido
print("\n Adicione produtos ao seu carrinho (de 1 a 4 ou 0 para finalizar):")
while True:
    escolha = ''
    try:
        escolha = int(input("Produto: "))
    except ValueError:
        print('Entrada inválida. Digite um número de 1 a 4 ou 0 para sair.') # Mensagem exibida para valor não numérico
        continue

    nome_do_produto = '' # Para atribuir o número digitado a um produto
    if escolha == 0:
        break  # Sai do loop se o usuário digitar '0'
    elif escolha == 1: nome_do_produto = 'Celular'
    elif escolha == 2: nome_do_produto = 'Notebook'
    elif escolha == 3: nome_do_produto = 'Fones de Ouvido'
    elif escolha == 4: nome_do_produto = 'Câmera'

    if nome_do_produto in ['Celular', 'Notebook', 'Fones de Ouvido', 'Câmera']:
        carrinho.append(nome_do_produto)  # Adiciona o produto ao carrinho
        print(f"{nome_do_produto} adicionado ao carrinho!")
    else:
        print('Produto não encontrado! Escolha um da lista')

# Agrupar e exibir produtos no carrinho
from collections import Counter # import para adicionar um "contador de items"

print("\n Produtos no seu carrinho:")
carrinho_agrupado = Counter(carrinho)

for produto, quantidade in carrinho_agrupado.items():
    print(f"- {produto}: {quantidade}x")

print("\nCompra finalizada! Obrigado por escolher nossa loja. ")
