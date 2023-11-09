import random


def generate_matrix(lists_number=2, list_length=5):
    """
    Генерує 2 вимірний список з випадковими цілими значеннями від 0 до 200

    :param lists_number: Кількість списків у основному списку
    :param list_length: Довжина елементів у кожному списку
    :return: Згенерований 2 вимірний список
    """
    matrix = [[random.randint(0, 200) for _ in range(list_length)] for _ in range(lists_number)]
    return matrix


def print_matrix(matrix):
    """
    Друкує симетричну таблицю значень

    :param matrix: 2 вимірний список
    """
    for row in matrix:
        print("|".join(str(value).center(5) for value in row))
        print("-" * (6 * len(row)))


if __name__ == "__main__":
    matrix_1 = generate_matrix()
    print("Згенерований 2 вимірний список без параметрів:")
    print_matrix(matrix_1)

    matrix_2 = generate_matrix(3)
    print("Згенерований 2 вимірний список з одним параметром:")
    print_matrix(matrix_2)

    matrix_3 = generate_matrix(4, 6)
    print("Згенерований 2 вимірний список з двома параметрами:")
    print_matrix(matrix_3)
