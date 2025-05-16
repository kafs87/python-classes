# Funções e Procedimentos - Ex 4:
# Cálculo de raiz quadrada, dobro e triplo
# Função construída

import ex6_imp

# Início 
ex6_imp.titulo_do_sistema() # Título

num = int(input("Digite um número: ")) # Entrada

# Sáida e Processamento
print(f"A raiz quadrada do número ({num}) é {ex6_imp.quadrado(num)}") 
print(f"O dobro do número ({num}) é {ex6_imp.dobro(num)}")
print(f"O triplo do número ({num}) é {ex6_imp.triplo(num)}")