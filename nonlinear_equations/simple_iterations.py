import numdifftools as nd
import numpy as np

MAX_ITERS = 50_000


def check_convergence_simple_iteration(f, phi, a, b):
    """
    Проверка сходимости по |phi'(x)| < 1 на [a, b]
    """
    dphi = nd.Derivative(phi)
    max_derivative = max(abs(dphi(a)), abs(dphi(b)))

    if max_derivative >= 1:
        print(f"Метод простой итерации может не сойтись: |phi'(x)| >= 1 на [{a}, {b}]")
        return False

    print(f"Метод сходится: max|phi'(x)| = {max_derivative:.6f}")
    return True


def simple_iteration_method(f, x0, a=None, b=None, epsilon=1e-5, max_iters=MAX_ITERS, log=True):
    """
    Метод простой итерации. Автоматически строит phi(x) = x - λ*f(x).
    :param f: функция
    :param x0: начальное приближение
    :param a: левая граница (для оценки сходимости)
    :param b: правая граница (для оценки сходимости)
    :param epsilon: точность
    :param max_iters: макс. количество итераций
    :param log: логирование итераций
    :return: (корень, значение функции в корне, число итераций)
    """
    print(x0, "= x0!")
    # Оценим производную f в x0
    df = nd.Derivative(f)
    try:
        lambda_ = 1.0 / df(x0)
    except ZeroDivisionError:
        print("Ошибка: производная равна 0, невозможно построить phi(x)")
        return None, None, 0

    # Построим phi(x)
    phi = lambda x: x - lambda_ * f(x)

    # Проверим сходимость (если есть границы)
    if a is not None and b is not None:
        if not check_convergence_simple_iteration(f, phi, a, b):
            return None, None, 0

    # Итерации
    x = x0
    for i in range(1, max_iters + 1):
        x_new = phi(x)

        if log:
            print(f"{i}: x = {x:.6f}, f(x) = {f(x):.6g}, |x_new - x| = {abs(x_new - x):.6g}")

        if abs(x_new - x) < epsilon and abs(f(x_new)) < epsilon:
            return x_new, f(x_new), i

        x = x_new

    print("Достигнуто максимальное число итераций.")
    return x, f(x), max_iters