import numpy as np


# НЕЛИНЕЙНЫЕ УРАВНЕНИЯ

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


# СИСТЕМЫ НЕЛИНЕЙНЫХ УРАВНЕНИЙ

# Система 1:
# sin(y) + 2x - 2 = 0
# y + cos(x - 1) - 0.7 = 0

def system1_funcs(vars):
    x, y = vars
    return np.array([
        np.sin(y) + 2 * x - 2,
        y + np.cos(x - 1) - 0.7
    ])


# Система 2:
# x^2 + y^2 - 1 = 0
# x - y = 0

def system2_funcs(vars):
    x, y = vars
    return np.array([
        x ** 2 + y ** 2 - 1,
        x - y
    ])


systems = [
    {
        "description": "Система 1: sin(y) + 2x = 2, y + cos(x - 1) = 0.7",
        "functions": system1_funcs,
    },
    {
        "description": "Система 2: x² + y² = 1, x = y",
        "functions": system2_funcs,
    },
]
