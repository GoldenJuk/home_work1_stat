# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры,
# которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

from functions import combinations, probability

total = 10
code = 3
attempt = 1

# Общее число комбинаций
total_combinations = combinations(code, total)

print(
    f'Вероятность того, что человек, не знающий код, откроет дверь с первой попытки = '
    f'{round((probability(attempt, total_combinations) * 100), 2)} %')
