import json
from datetime import datetime
from collections import defaultdict


def check_capacity(max_capacity: int, guests: list) -> bool:
    # Если гостей меньше, чем вместимость отеля, то точно всех разместим
    if max_capacity >= len(guests):
        return True

    # Заполняем словарь нулями
    in_and_out_events = defaultdict(int)
    for guest in guests:
        check_in = datetime.strptime(guest["check-in"], "%Y-%m-%d")
        check_out = datetime.strptime(guest["check-out"], "%Y-%m-%d")

        in_and_out_events[check_in] += 1
        in_and_out_events[check_out] -= 1

    guests_counter = 0
    for date in sorted(in_and_out_events.keys()):
        guests_counter += in_and_out_events[date]
        if guests_counter > max_capacity:
            return False
    return True

if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)