import os
os.system('cls')

vetor_temperatura = []
soma = 0

for i in range(7):
    temperatura = float(input(f'Digite a temperatura do {i+1}dia: '))
    vetor_temperatura.append(temperatura)
    soma += temperatura
    media = soma / 7
    maior = max(vetor_temperatura)
    menor = min(vetor_temperatura)

print(f'Media = {media}')
print(f'Maior = {maior}')
print(f'Menor = {menor}')