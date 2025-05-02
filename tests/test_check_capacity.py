from run import check_capacity


def test_enough_capacity():
    """ Простой тест, когда вместимости хватает """
    max_capacity = 2
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-03"},
        {"name": "Bob", "check-in": "2025-04-03", "check-out": "2025-04-05"}
    ]
    assert check_capacity(max_capacity, guests) == True

def test_crossing_quests_with_enough_capacity():
    """ Есть пересечение по датам заезда и выезда, но вместимости хватает на всех"""
    max_capacity = 2
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-04"},
        {"name": "Bob", "check-in": "2025-04-02", "check-out": "2025-04-05"}
    ]
    assert check_capacity(max_capacity, guests) == True

def test_crossing_guests_with_no_enough_capacity():
    """ Есть пересечение по датам заезда и выезда. Мест не хватает на всех """
    max_capacity = 2
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-05"},
        {"name": "Bob", "check-in": "2025-04-02", "check-out": "2025-04-06"},
        {"name": "Charlie", "check-in": "2025-04-03", "check-out": "2025-04-07"}
    ]
    assert check_capacity(max_capacity, guests) == False

def test_check_in_and_check_out_in_one_day():
    """ Дата заезда и выезда совпадает """
    max_capacity = 1
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-02"},
        {"name": "Bob", "check-in": "2025-04-02", "check-out": "2025-04-03"}
    ]
    assert check_capacity(max_capacity, guests) == True

def test_all_guests_check_in_in_one_day():
    """ Все гости заезжают в один день """
    max_capacity = 3
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-05"},
        {"name": "Bob", "check-in": "2025-04-01", "check-out": "2025-04-06"},
        {"name": "Charlie", "check-in": "2025-04-01", "check-out": "2025-04-07"}
    ]
    assert check_capacity(max_capacity, guests) == True

def test_zero_capacity_with_quests():
    """ Нулевая вместимость гостиницы и гость, который хочет въехать """
    max_capacity = 0
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-02"}
    ]
    assert check_capacity(max_capacity, guests) == False

def test_more_guests_then_max_capacity():
    """ Гостей больше, чем вместимость гостиницы """
    max_capacity = 2
    guests = [
        {"name": "Alice", "check-in": "2025-04-01", "check-out": "2025-04-05"},
        {"name": "Bob", "check-in": "2025-04-02", "check-out": "2025-04-04"},
        {"name": "Charlie", "check-in": "2025-04-03", "check-out": "2025-04-06"}
    ]
    assert check_capacity(max_capacity, guests) == False

def test_many_guests_but_all_spaced_out():
    """ Гостей много, но все могут въехать """
    max_capacity = 1
    guests = [
        {"name": f"Guest{i}", "check-in": f"2025-04-{i:02d}", "check-out": f"2025-04-{i + 1:02d}"}
        for i in range(1, 30)
    ]
    assert check_capacity(max_capacity, guests) == True

def test_many_guests_in_same_date():
    """ Много гостей заезжают в один день, мест на всех не хватит"""
    max_capacity = 10
    guests = [
        {"name": f"Guest{i}", "check-in": "2025-04-01", "check-out": "2025-04-10"}
        for i in range(1, 12)
    ]
    assert check_capacity(max_capacity, guests) == False

