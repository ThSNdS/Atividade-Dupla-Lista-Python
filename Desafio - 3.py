import os
os.system('cls')

vetor_numeros = []
soma = 0
Maiores = 0

for i in range(10):
    numero = int(input('Digite um número: '))
    soma += numero
    if numero > 10:
        Maiores += 1

print(f'\nA soma dos numeros é {soma} e existem {Maiores} números maiores que 10.')