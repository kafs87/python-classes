# Funções e Procedimentos - Ex 1:
# Função já existente - pré definidas: Exponencial

# Importação de uma biblioteca com funções/procedimentos já existentes.
import math 

print("\n\nCálculo Exponencial")
num = int(input("Digite um número: "))
exponencial = math.exp(num)
print(f"O exponecial do número {num} é {exponencial:.2f}")
