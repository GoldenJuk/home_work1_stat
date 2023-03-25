# Из колоды в 52 карты извлекаются случайным образом 4 карты.
#   a) Найти вероятность того, что все карты – крести.
#   б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from functions import combinations, probability

total = 52
take = 4
kresty = 13
ace = 4

# Общее число комбинаций
total_combinations = combinations(take, total)

# В колоде из 52 карт - крести 13 штук, тогда число комбинаций 4 из 13:
kresty_combinations = combinations(take, kresty)

print(
    f'Вероятность того, что при извлечении случайным образом 4 карт из колоды 52 карты, все карты будут крести = '
    f'{round((probability(kresty_combinations, total_combinations) * 100), 2)} %')

# Для задачи "б" находим сначала вероятность того, что ни одна из карт не будет тузом,
# затем от 1 вычитаем полученную вероятность
no_ace_combinations = combinations(ace, (total - ace))

print(
    f'Вероятность того, что при извлечении случайным образом 4 карт из колоды 52 карты, среди них окажется хотя бы один туз = '
    f'{round(((1 - probability(no_ace_combinations, total_combinations)) * 100), 2)} %')
