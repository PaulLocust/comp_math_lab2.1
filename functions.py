import numpy as np


# ===== НЕЛИНЕЙНЫЕ УРАВНЕНИЯ =====

def f1(x):
    return x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38


def f2(x):
    return np.cos(x) - x


def f3(x):
    return np.exp(x) + x


equations = [
    {
        "description": "x³ + 4.81x² - 17.37x + 5.38",
        "function": f1,
    },
    {
        "description": "cos(x) - x",
        "function": f2,
    },
    {
        "description": "exp(x) + x",
        "function": f3,
    }
]


# ===== СИСТЕМЫ НЕЛИНЕЙНЫХ УРАВНЕНИЙ =====

# Система 1:
# x^2 + y^2 - 1 = 0
# x - y = 0

def system1_funcs(vars):
    x, y = vars
    return np.array([
        x ** 2 + y ** 2 - 1,
        x - y
    ])


# Система 2:
# sin(x + y) - x = 0
# y - cos(x) = 0

def system2_funcs(vars):
    x, y = vars
    return np.array([
        np.sin(x + y) - x,
        y - np.cos(x)
    ])


systems = [
    {
        "description": "Система 1: x² + y² = 1, x = y",
        "functions": system1_funcs,
    },
    {
        "description": "Система 2: sin(x + y) = x, y = cos(x)",
        "functions": system2_funcs,
    }
]
