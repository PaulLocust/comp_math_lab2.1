import math

MAX_ITERS = 50_000


def newton_method_system(F, x0, eps=1e-5, max_iters=MAX_ITERS, log=True):
    """
    Метод Ньютона для систем нелинейных уравнений.

    :param F: функция-система, возвращающая список [f1(x, y), f2(x, y)]
    :param x0: начальное приближение (список)
    :param eps: точность
    :param max_iters: максимальное число итераций
    :param log: логировать итерации
    :return: (решение, значение функции, число итераций, вектор приращений)
    """
    x = x0[:]  # Начальное приближение

    for i in range(1, max_iters + 1):
        J = jacobian(F, x)  # Якобиан
        Fx = F(x)           # Значения функций
        norm_Fx = math.sqrt(sum(f**2 for f in Fx))  # Норма функции

        if norm_Fx < eps:
            return x, Fx, i, [0.0] * len(x)  # Нулевая дельта, если сходимость уже достигнута

        # Решаем систему J * delta = -F(x)
        try:
            delta = gaussian_elimination(J, [-f for f in Fx])
        except Exception as e:
            print("Ошибка при решении системы:", e)
            return None, None, i, None

        # Обновляем x
        x_new = [x[j] + delta[j] for j in range(len(x))]

        if log:
            print(f"{i}: x = {x}, F(x) = {Fx}, ||delta|| = {math.sqrt(sum(d**2 for d in delta)):.6g}, vector_delta = {delta}")

        # Проверка по норме дельты
        norm_delta = math.sqrt(sum(d**2 for d in delta))
        if norm_delta < eps:
            return x_new, F(x_new), i, delta

        x = x_new

    print("Достигнуто максимальное число итераций.")
    return x, F(x), max_iters, delta


def jacobian(F, x, h=1e-5):
    """
    Вычисление Якобиана для системы уравнений с помощью конечных разностей.
    :param F: функция-система, возвращающая список [f1(x, y), f2(x, y)]
    :param x: текущая точка
    :param h: шаг для вычисления частных производных
    :return: Якобиан (матрица)
    """
    n = len(x)
    jacobian_matrix = []
    for i in range(n):
        row = []
        x_perturbed = x[:]
        for j in range(n):
            x_perturbed[j] += h
            partial_derivative = (F(x_perturbed)[i] - F(x)[i]) / h
            row.append(partial_derivative)
            x_perturbed[j] = x[j]  # Возвращаем значение в исходное состояние
        jacobian_matrix.append(row)
    return jacobian_matrix


def gaussian_elimination(A, b):
    """
    Метод Гаусса для решения системы линейных уравнений.
    :param A: матрица коэффициентов
    :param b: вектор правых частей
    :return: решение системы
    """
    n = len(A)
    # Прямой ход
    for i in range(n):
        # Ищем максимальный элемент для устойчивости
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] -= A[j][i] * x[i]

    return x
