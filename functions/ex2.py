'''-
Problema: Data a idade de um nadador, classifique-o em uma das categorias
# Data: 07/04/2025
# Autor: Samuel 
'''

print("\n\n Categoria dos atletas \n\n")    
idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")

if (idade < 5): 
    resultado = "idade invalida"
elif (idade <= 7):
    resultado = "infantil A"
elif (idade <= 10):
    resultado = "infantil B"
elif (idade <= 13):
    resultado = "juvenil A"
elif (idade <= 17):
    resultado = "juvenil B"
else:
    resultado = "Adulto"

# "Ana julia, sua idade é 16 e você esta na  categoria Juvenil B."
print(f"{nome}, sua idade é {idade} e você esta na categoria {resultado}")