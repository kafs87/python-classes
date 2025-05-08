# Exercício 01 - Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na tela. O programa termina quanto a temperatura inserida for menor que -5

print('\n========== EXERCICIO 01 ==========')

temperatura = int(input("Digite uma temperatura em graus Celsius: "))

while (temperatura >= -5):
    fahrenheit = (temperatura * 1.8) + 32
    kelvin = temperatura + 273.15
    print(f'Temperatura em Fahrenheit: {fahrenheit}')
    print(f'Temperatura em Kelvin: {kelvin}')
    temperatura = int(input("Digite outra temperatura em graus Celsius: "))

print(f'Temperatura inserida menor que -5: ({temperatura})')

# Exercício 02 - Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. O programa deve repetir até que o usuário digite um número fora desse intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número inválido”.

print('\n========== EXERCICIO 02 ==========')

num_digitado = int(input("Digite um número de 1 a 7: "))

while (num_digitado >= 1 and num_digitado <= 7):
    if num_digitado == 1:
        print("Segunda-Feira")
    elif num_digitado == 2:
        print("Terça-Feira")
    elif num_digitado == 3:
        print("Quarta-Feira")
    elif num_digitado == 4:
        print("Quinta-Feira")
    elif num_digitado == 5:
        print("Sexta-Feira")
    elif num_digitado == 6:
        print("Sábado")
    elif num_digitado == 7:
        print("Domingo")
    num_digitado = int(input("Digite um novo número de 1 a 7: "))
print("Número inválido.")

# Exercício 03 - Elaborar um programa que deve ler N números. Caso o usuário digite zero (0), o programa deve exibir a somatória e a média dos valores inseridos.

print('\n========== EXERCICIO 03 ==========')

soma_dos_numeros = 0
contador = 0
num_ex3 = int(input("Digite um número: "))

while (num_ex3 != 0):
    soma_dos_numeros += num_ex3
    contador += 1
    num_ex3 = int(input("Digite outro número ou 0 para calcular: "))
    if num_ex3 == 0:
        break

if contador > 0:
    media = soma_dos_numeros / contador
    print(f"A soma dos números é: {soma_dos_numeros}")
    print(f"A média dos números é: {media}")
else:
    print("Nenhum número válido foi inserido.")

# Exercício 04 - Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80, quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário

print('\n========== EXERCICIO 04 ==========')

acima_de_80 = 0
abaixo_de_10 = 0
somatoria = 0
contador_para_media = 0
valor = int(input("Digite um valor: "))

while (valor != 100):
    if (valor >= 80):
        acima_de_80 += 1
    elif (valor <= 10):
        abaixo_de_10 += 1

    somatoria += valor
    contador_para_media += 1
    valor = int(input("Digite outro valor ou 100 para calcular: "))
    if valor == 100:
        break

if contador > 0:
    media_ex4 = somatoria / contador_para_media
    print(f"Números acima de 80: ")
    print(f"Números abaixo de 10: ")
    print(f"A soma dos números é: {somatoria}")
    print(f"A média dos números é: {media_ex4}")
else:
    print("Nenhum valor válido foi inserido.")

# Exercício 05 - Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2 deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até N.

print('\n========== EXERCICIO 05 ==========')



# Exercício 06 - Elaborar um programa que solicita um número (entre 10 a 15). Se o usuário digitar um número diferente, o programa deve mostrar a mensagem “Entrada inválida” e solicitar um número novamente. Se digitar correto o programa deve mostrar a raiz quadrada desse número e termina

print('\n========== EXERCICIO 06 ==========')



# Exercício 07 - Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchida pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o número 1 a repetição termina. Exibir no final todos os elementos da lista.

print('\n========== EXERCICIO 07 ==========')



# Exercício 08 - Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário que digite dois números. Esses números devem corresponder a posições na lista (caso contrário solicite um novo valor). Após inserir os dois números o programa deve exibir a soma dos elementos das duas posições da lista.

print('\n========== EXERCICIO 08 ==========')



# Exercício 09 - Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista

print('\n========== EXERCICIO 09 ==========')


