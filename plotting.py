import numpy as np
import matplotlib.pyplot as plt


def plot_function(f, a, b, title="График функции"):
    """Построение графика одиночной функции"""
    x = np.linspace(a, b, 500)
    y = f(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.7)
    plt.grid(True)
    plt.legend()
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


def plot_system(f1, f2, x_range=(-5, 5), y_range=(-5, 5), title="Графики системы"):
    """Построение графиков двух уравнений системы"""
    x = np.linspace(*x_range, 500)
    y = np.linspace(*y_range, 500)
    X, Y = np.meshgrid(x, y)

    try:
        Z1 = f1(X, Y)
        Z2 = f2(X, Y)

        plt.figure(figsize=(8, 6))
        cs1 = plt.contour(X, Y, Z1, levels=[0], colors='blue', linewidths=2, label='f1(x, y)=0')
        cs2 = plt.contour(X, Y, Z2, levels=[0], colors='red', linewidths=2, label='f2(x, y)=0')

        # Создаём легенду вручную
        lines = [
            plt.Line2D([0], [0], color='blue', label='f1(x, y) = 0'),
            plt.Line2D([0], [0], color='red', label='f2(x, y) = 0'),
        ]
        plt.legend(handles=lines)

        plt.grid(True)
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    except Exception as e:
        print(f"Ошибка при построении графика системы: {e}")
