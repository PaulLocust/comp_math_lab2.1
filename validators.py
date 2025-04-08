import numpy as np


def validate_interval(f, a, b, steps=1000):
    """
    Проверяет:
    - f(a)*f(b) < 0 (смена знака → корень)
    - только один корень на интервале
    """
    if a >= b:
        print("Левая граница должна быть меньше правой.")
        return False

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print(" На интервале нет смены знака ⇒ возможно, нет корня.")
        return False

    # Дополнительно: поиск количества смен знака
    x = np.linspace(a, b, steps)
    signs = np.sign(f(x))
    sign_changes = np.count_nonzero(np.diff(signs))

    if sign_changes > 1:
        print("На интервале несколько корней. Выберите меньший интервал.")
        return False

    return True


def has_root(f, a, b):
    """Упрощённая проверка наличия корня по смене знака"""
    try:
        return f(a) * f(b) < 0
    except:
        return False


def choose_initial_guess(f, a, b):
    """
    Выбирает точку с наименьшим значением |f(x)| между a и b.
    Подходит как приближение.
    """
    x_vals = np.linspace(a, b, 100)
    f_vals = np.abs([f(x) for x in x_vals])
    min_index = np.argmin(f_vals)
    return x_vals[min_index]
