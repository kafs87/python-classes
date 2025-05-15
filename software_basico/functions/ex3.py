# Funções e Procedimentos - Ex 3:
#   Cálculo de raiz quadrada
# Função construída

def quadrado(parametro_num):
    return (parametro_num * parametro_num)

# Jeito "errado"
print("\n\nCálculos")
num = int(input("Digite um número: "))
quad = quadrado(num)
print(f"A raiz quadrada do número ({num}) é {quad}")

# Jeito certo
num = int(input("Digite um segundo número: "))
print(f"A raiz quadrada do segundo número ({num}) é {quadrado(num)}")

num = int(input("Digite um segundo número: "))
print(f"A raiz quadrada do segundo número ({num}) é {quadrado(num)}")