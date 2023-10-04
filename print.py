from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверка коректности числа."""
    if your_number <= 0:
        return False
    numb = CalculateSquareRoot(your_number)

    print(f'Мы вычислили квадратный корень из введённого '
          f'вами числа. Это будет: {numb}')


calc(25.5)