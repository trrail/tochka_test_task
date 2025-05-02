import json
from datetime import datetime


def check_capacity(max_capacity: int, guests: list) -> bool:
    if max_capacity >= len(guests):
        return True
    dates = {}
    for guest in guests:
        check_in = datetime.strptime(guest["check-in"], "%Y-%m-%d")
        check_out = datetime.strptime(guest["check-out"], "%Y-%m-%d")
        if dates.get(check_in) is None:
            dates[check_in] = 0
        if dates.get(check_out) is None:
            dates[check_out] = 0
        dates[check_in] += 1
        dates[check_out] -= 1

    counter = 0
    for date in sorted(dates.keys()):
        counter += dates[date]
        if counter > max_capacity:
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