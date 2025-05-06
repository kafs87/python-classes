# Funções e Procedimentos - Ex 4:
# Função construída

import functions.ex9 as ex9

# Início 
ex9.titulo_do_sistema() # Título

num = int(input("Digite um número: ")) # Entrada

# Sáida e Processamento
print(f"A raiz quadrada do número ({num}) é {ex9.quadrado(num)}") 
print(f"O dobro do número ({num}) é {ex9.dobro(num)}")
print(f"O triplo do número ({num}) é {ex9.triplo(num)}")