def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, dict)):
        print('В numbers переданы неправильные данные')
        return None
    if len(numbers) == 0:
        return 0
    total_sum, incorrect_data = personal_sum(numbers)
    try:
        average_num = total_sum / (len(numbers) - incorrect_data)
        return average_num
    except ZeroDivisionError:
        return 0

# Тестовые примеры
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
