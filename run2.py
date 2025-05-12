import sys

from collections import deque
from typing import List, Tuple


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def min_steps_to_collect_all_keys(data: List[str]) -> int:
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    data = [list(row) for row in data]

    # Находим стартовые позиции и все ключи
    robots_start_positions = []
    all_keys = set()

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@':
                robots_start_positions.append((r, c))
                data[r][c] = '.'  # Меняем @ на точку, чтобы робот мог пройти через своё начальное состояние
            elif data[r][c].islower():
                all_keys.add(data[r][c])

    total_keys = len(all_keys)
    if total_keys == 0:
        return 0  # если ключей нет, ответ 0

    # Создал очередь для состояний
    queue = deque()
    # Закидываем в очередь начальное состояние - позиции роботов, найденные ключи, кол-во шагов
    queue.append((tuple(robots_start_positions), set(), 0))

    # Множество посещенных состояний: (позиции_роботов, frozenset_ключей)
    visited = set()
    visited.add((tuple(robots_start_positions), frozenset()))

    # Направления движения для роботов
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        robots, collected_keys, steps = queue.popleft()
        for i in range(len(robots)):
            x, y = robots[i]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                cell = data[nx][ny]
                if cell == '#':
                    continue  # Упёрлись в стену
                if cell.isupper() and cell.lower() not in collected_keys:
                    continue  # Нашли дверь, но не можем открыть
                # Проверяем клетку на наличие ключа. Если ключ, то кладём его в мн-во найденных ключей
                new_keys = set(collected_keys)
                if cell.islower():
                    new_keys.add(cell)
                # Обновляем позиции роботов
                new_robots = list(robots)
                new_robots[i] = (nx, ny)
                new_robots_tuple = tuple(new_robots)
                # Сохраняем получившееся состояние
                state = (new_robots_tuple, frozenset(new_keys))
                if state in visited:
                    continue
                visited.add(state)
                # Если собрали все ключи, возвращаем ответ
                if len(new_keys) == total_keys:
                    return steps + 1

                queue.append((new_robots_tuple, new_keys, steps + 1))
    return 0

def main():
    data = get_input()
    result = min_steps_to_collect_all_keys(data)
    print(result)


if __name__ == '__main__':
    main()