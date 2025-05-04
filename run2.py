import sys

import collections


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]

def min_steps_to_collect_all_keys(data) -> int:
    return 0

def main():
    data = get_input()
    result = min_steps_to_collect_all_keys(data)
    print(result)


if __name__ == '__main__':
    main()