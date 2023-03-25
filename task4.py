# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from functions import combinations, probability

total = 100
winning = 2
take = 2

# Общее число комбинаций
total_combinations = combinations(take, total)

# Число благоприятных комбинаций (взять 2 выйгрышных билета из 2-х)
winning_combinations = combinations(take, winning)

print(
    f'Вероятность того, что 2 купленных билета в лотерее из 100 билетов, в котором 2 выйгрышных билета = '
    f'{round(((winning_combinations / total_combinations) * 100), 2)} %')
