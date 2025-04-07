import numpy as np
import numdifftools as nd

MAX_ITERS = 50_000


def newton_method_system(F, x0, eps=1e-5, max_iters=MAX_ITERS, log=True):
    """
    Метод Ньютона для систем нелинейных уравнений.

    :param F: функция-система, возвращающая np.array([f1(x, y), f2(x, y)])
    :param x0: начальное приближение (список или np.array)
    :param eps: точность
    :param max_iters: макс. число итераций
    :param log: логировать итерации
    :return: (решение, значение функции, число итераций)
    """
    x = np.array(x0, dtype=float)
    jacobian_func = nd.Jacobian(F)

    for i in range(1, max_iters + 1):
        J = jacobian_func(x)      # Якобиан
        Fx = F(x)                 # Значения функций

        if np.linalg.norm(Fx, ord=2) < eps:
            return x, Fx, i

        try:
            delta = np.linalg.solve(J, -Fx)  # Решение J * delta = -F(x)
        except np.linalg.LinAlgError:
            print("Якобиан вырожден. Метод Ньютона невозможен.")
            return None, None, i

        x_new = x + delta

        if log:
            print(f"{i}: x = {x}, F(x) = {Fx}, ||delta|| = {np.linalg.norm(delta):.6g}")

        if np.linalg.norm(delta, ord=2) < eps:
            return x_new, F(x_new), i

        x = x_new

    print("Достигнуто максимальное число итераций.")
    return x, F(x), max_iters
