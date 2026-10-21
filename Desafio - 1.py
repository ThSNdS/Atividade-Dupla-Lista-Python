import os
os.system('cls')

numeros = []

for I in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

for i in range(5):
    print(f'{i+1}° Número: {numeros[i]}')

for i in range(5,0,-1):
    print(f'Número: {numeros[i]}')