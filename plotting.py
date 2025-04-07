import numpy as np
import matplotlib.pyplot as plt


def plot_function(f, a, b, title="График функции"):
    """Построение графика одиночной функции"""
    x = np.linspace(a, b, 500)
    y = f(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"f(x)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_system(funcs, x_range=(-5, 5), y_range=(-5, 5), title="Графики системы"):
    """
    Построение графиков двух уравнений системы нелинейных уравнений.

    :param funcs: список из одной функции, которая возвращает массив значений
    :param x_range: диапазон значений для оси X
    :param y_range: диапазон значений для оси Y
    :param title: заголовок графика
    """
    # Создаем сетку для значений x и y
    x = np.linspace(x_range[0], x_range[1], 500)
    y = np.linspace(y_range[0], y_range[1], 500)
    X, Y = np.meshgrid(x, y)

    try:
        # Создаем массивы Z1 и Z2 для значений функции
        Z1 = np.zeros(X.shape)
        Z2 = np.zeros(Y.shape)

        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                x_val = X[i, j]
                y_val = Y[i, j]
                # Вычисляем результат для этой точки с помощью функции system1_funcs
                Z = funcs([x_val, y_val])
                Z1[i, j] = Z[0]  # Значение первого уравнения
                Z2[i, j] = Z[1]  # Значение второго уравнения

        plt.figure(figsize=(8, 6))

        plt.contour(X, Y, Z1, levels=[0], colors='blue', linewidths=2)

        plt.contour(X, Y, Z2, levels=[0], colors='red', linewidths=2)

        # Оформление графика
        plt.grid(True)
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")

        # Добавляем легенду
        lines = [
            plt.Line2D([0], [0], color='blue', label=r'$f_1(x, y) = 0$'),
            plt.Line2D([0], [0], color='red', label=r'$f_2(x, y) = 0$'),
        ]
        plt.legend(handles=lines)

        plt.show()

    except Exception as e:
        print(f"Ошибка при построении графика системы: {e}")
