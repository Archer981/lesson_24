# Напишите регулярное выражение и вставьте вместо 'regular_value'.
#  Проверить, что строка input_str содержит python
# Не изменяйте, пожалуйста, название функции

import re


def snake_checker(input_str):
    regex = re.compile(r"python")
    m = regex.search(input_str)
    return bool(m)


if __name__ == "__main__":
    value = "I'm learning python "
    print(value, snake_checker(value))  # Ожидаем True
    value = "I'm learning"
    print(value, snake_checker(value))  # Ожидаем False
    value = "python is awesome"
    print(value, snake_checker(value))  # Ожидаем True
