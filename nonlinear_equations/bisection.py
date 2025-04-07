
def bisection_method(f, a, b, epsilon=1e-5, max_iters=1000, log=True):
    """
    Метод половинного деления (бисекции) для нахождения корня уравнения f(x) = 0 на интервале [a, b].

    :param f: функция f(x)
    :param a: левая граница интервала
    :param b: правая граница интервала
    :param epsilon: требуемая точность
    :param max_iters: максимальное число итераций
    :param log: вывод логов итераций
    :return: (корень, значение функции в корне, число итераций)
    """
    if f(a) * f(b) >= 0:
        print("Условие f(a) * f(b) < 0 не выполняется. Метод невозможен.")
        return None, None, 0

    for i in range(1, max_iters + 1):
        c = (a + b) / 2
        fc = f(c)

        if log:
            print(f"{i}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6e}")

        if abs(fc) < epsilon or abs(b - a) < epsilon:
            return c, f(c), i

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Достигнуто максимальное число итераций.")
    return (a + b) / 2, f((a + b) / 2), max_iters