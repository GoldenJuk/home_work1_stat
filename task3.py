# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from functions import combinations, probability

total = 15
painted = 9
take = 3

# Общее число комбинаций
total_combinations = combinations(take, total)

# Число комбинаций извлечения 3-х окрашенных деталей из 9 окрашенных
painted_combinations = combinations(take, painted)

print(
    f'Вероятность того, что 3 детали, случайным образом извлеченные из ящика с 15 деталями из которых 9 окрашенные, будут окрашены = '
    f'{round(((painted_combinations / total_combinations) * 100), 2)} %')
