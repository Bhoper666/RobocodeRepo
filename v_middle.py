print('')
print('Програма для пошуку Vсер на Python. Copyright 2024 Herobrine Studios. All rights reserved.')

l1 = int(input('Введіть l1 - км(впишіть 0 якщо пусто) >>> '))
l2 = int(input('Введіть l2 - км(впишіть 0 якщо пусто) >>> '))
l3 = int(input('Введіть l3 - км(впишіть 0 якщо пусто) >>> '))
t = int(input('Введіть t - год(впишіть 0 якщо пусто) >>> '))

print(f'Результат: Vсер = {(l1 + l2 + l3) / t} км/год')
