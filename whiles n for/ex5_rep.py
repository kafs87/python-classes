# Problema - Lista de compras 

print(f"\nLista de Compras\n")

# Inicialização das variáveis
total_de_gastos = 0
valor = 0
limite = 1500

while (total_de_gastos < limite):
    valor = float(input("Digite o valor do gasto: "))
    total_de_gastos = total_de_gastos + valor

print(f"\nLimite: {limite}\n")
print(f"\nTotal de gastos: {total_de_gastos}\n")
print(f"\nDiferença: {total_de_gastos - limite}\n")