# Funções e Procedimentos - Ex 4:
# Cálculo de raiz quadrada, dobro e triplo
# Função construída

import ex6

# Início 
ex6.titulo_do_sistema() # Título

num = int(input("Digite um número: ")) # Entrada

# Sáida e Processamento
print(f"A raiz quadrada do número ({num}) é {ex6.quadrado(num)}") 
print(f"O dobro do número ({num}) é {ex6.dobro(num)}")
print(f"O triplo do número ({num}) é {ex6.triplo(num)}")