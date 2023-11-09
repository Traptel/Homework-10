def check_sum_of_two_numbers(numbers, amount):
    """
    Перевіряє чи є в списку два числа сума яких дорівнює переданому числу

    :param numbers: Список чисел
    :param amount: ціле число
    :return: True, якщо є два числа, сума яких рівна числу, в іншому випадку False
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == amount:
                return True
    return False


list_1 = [1, 2, 3, 4, 5]
num_1 = 6
list_2 = [6, 7, 8, 9, 10]
num_2 = 1

if __name__ == "__main__":
    result_1 = check_sum_of_two_numbers(list_1, num_1)
    print(f"Результат першого прикладу: {result_1}")
    result_2 = check_sum_of_two_numbers(list_2, num_2)
    print(f"Результат другого прикладу: {result_2}")
