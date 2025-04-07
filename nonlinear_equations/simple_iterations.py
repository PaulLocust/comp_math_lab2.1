import numpy as np

# Константа для вычисления производных
dx = 1e-5
MAX_ITERS = 50_000


def derivative(f, x, h=dx):
    """
    Численное вычисление производной с помощью конечных разностей.
    :param f: функция, производную которой нужно вычислить
    :param x: точка, в которой вычисляется производная
    :param h: шаг для вычисления производной
    :return: значение производной в точке x
    """
    return (f(x + h) - f(x)) / h


def check_convergence_simple_iteration(f, left, right):
    """
    Проверка условия сходимости метода простой итерации на интервале.
    :param f: функция, для которой ищем корень
    :param left: левая граница интервала
    :param right: правая граница интервала
    :return: True если метод сходится, False если нет
    """
    # Вычисление максимальной производной на интервале
    max_derivative = max(abs(derivative(f, left)), abs(derivative(f, right)))

    if max_derivative >= 1:
        print(f"Условие сходимости не выполнено: |f'(x)| >= 1 на интервале [{left}, {right}]")
        return False

    print(f"Максимальная производная на интервале: {max_derivative}")
    return True


def simple_iteration_method(f, phi, left, right, epsilon, decimal_places, log=False):
    """
    Решение уравнения методом простой итерации.
    :param f: функция, для которой ищем корень
    :param phi: функция преобразования x = phi(x)
    :param left: левая граница интервала
    :param right: правая граница интервала
    :param epsilon: точность
    :param decimal_places: количество знаков после запятой
    :param log: флаг логирования
    :return: объект Result с корнем, значением функции в корне и количеством итераций
    """
    # Проверка сходимости метода
    if not check_convergence_simple_iteration(f, left, right):
        return None

    # Итерационный процесс
    x = (left + right) / 2  # Начальное приближение
    iteration = 0

    while True:
        iteration += 1
        x_prev = x
        x = phi(x)  # Следующее приближение

        if log:
            print(f'{iteration}: xk = {x_prev:.4f}, f(xk) = {f(x_prev)}, '
                  f'xk+1 = 𝜑(𝑥𝑘) = {x:.4f}, |xk - xk+1| = {abs(x - x_prev):}')

        # Условие завершения
        if abs(x - x_prev) <= epsilon and abs(f(x)) <= epsilon:
            break

        if iteration >= MAX_ITERS:
            print(f"Достигнуто максимальное количество итераций {MAX_ITERS}")
            break

    return Result(x, f(x), iteration, decimal_places)
