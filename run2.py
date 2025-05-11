import sys

from collections import deque
from typing import List, Tuple


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def min_steps_to_collect_all_keys(grid: List[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    grid = [list(row) for row in grid]

    # Все ключи и стартовые позиции
    key_count = 0
    starts = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                starts.append((r, c))
                grid[r][c] = '.'  # заменяем на проходимое
            elif 'a' <= grid[r][c] <= 'z':
                key_count |= 1 << (ord(grid[r][c]) - ord('a'))

    all_keys = key_count  # Целевая битовая маска всех ключей
    queue = deque()

    # Изначальное состояние: позиции роботов + маска ключей
    visited = set()
    queue.append((tuple(starts), 0, 0))  # ((r1, r2, r3, r4), ключи, шаги)
    visited.add((tuple(starts), 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        robots, keys, steps = queue.popleft()

        for i in range(len(robots)):
            x, y = robots[i]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue
                cell = grid[nx][ny]
                if cell == '#':
                    continue
                if 'A' <= cell <= 'Z' and not (keys & (1 << (ord(cell.lower()) - ord('a')))):
                    continue

                new_keys = keys
                if 'a' <= cell <= 'z':
                    new_keys |= 1 << (ord(cell) - ord('a'))

                new_robots = list(robots)
                new_robots[i] = (nx, ny)
                new_robots_tuple = tuple(new_robots)

                state = (new_robots_tuple, new_keys)
                if state in visited:
                    continue
                visited.add(state)

                if new_keys == all_keys:
                    return steps + 1

                queue.append((new_robots_tuple, new_keys, steps + 1))

    return -1

def main():
    data = get_input()
    result = min_steps_to_collect_all_keys(data)
    print(result)


if __name__ == '__main__':
    main()