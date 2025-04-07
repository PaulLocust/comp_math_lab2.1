MAX_ITERS = 50_000


def secant_method(f, a, b, epsilon=1e-5, max_iters=MAX_ITERS, log=True):
    """
    Метод секущих для нахождения корня уравнения f(x) = 0 на отрезке [a, b].

    :param f: функция
    :param a: левая граница
    :param b: правая граница
    :param epsilon: точность
    :param max_iters: макс. число итераций
    :param log: логирование шагов
    :return: (корень, значение функции, число итераций)
    """
    fa, fb = f(a), f(b)

    if abs(fa) < epsilon:
        return a, fa, 0
    if abs(fb) < epsilon:
        return b, fb, 0

    for i in range(1, max_iters + 1):
        if fb - fa == 0:
            print("Ошибка: деление на ноль в методе секущих.")
            return None, None, i

        x = b - fb * (b - a) / (fb - fa)

        fx = f(x)

        if log:
            print(f"{i}: x = {x:.6f}, f(x) = {fx:.6g}, |x - b| = {abs(x - b):.6g}")

        if abs(fx) < epsilon or abs(x - b) < epsilon:
            return x, fx, i

        a, fa = b, fb
        b, fb = x, fx

    print("Достигнуто максимальное число итераций.")
    return b, fb, max_iters
