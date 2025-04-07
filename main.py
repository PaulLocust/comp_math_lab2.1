
from functions import equations, systems
from io_handler import input_from_keyboard, input_from_file, output_to_screen, output_to_file
from nonlinear_equations.simple_iterations import simple_iteration_method
from nonlinear_equations.bisection import bisection_method
from nonlinear_equations.secant import secant_method
from nonlinear_systems.newton import newton_method_system
from plotting import plot_function, plot_system
from validators import has_root, choose_initial_guess


def solve_equation():
    print("\nВыберите уравнение:")
    for i, eq in enumerate(equations):
        print(f"{i + 1}. {eq['description']}")

    # Защищаем ввод от ошибок преобразования в число
    while True:
        try:
            eq_index = int(input("Номер уравнения: ")) - 1
            if eq_index < 0 or eq_index >= len(equations):
                print("Неверный номер уравнения. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

    equation = equations[eq_index]
    f = equation["function"]

    # Показываем график функции на [-10, 10]
    plot_function(f, -10, 10, title=f"График: {equation['description']}")

    print("\nВыберите метод:")
    print("1. Метод половинного деления")
    print("2. Метод секущих")
    print("3. Метод простой итерации")

    # Защищаем ввод метода
    while True:
        method_choice = input("Ваш выбор: ")
        if method_choice in ["1", "2", "3"]:
            break
        else:
            print("Неверный выбор метода. Пожалуйста, выберите 1, 2 или 3.")

    print("\nВыберите способ ввода данных:")
    print("1. С клавиатуры")
    print("2. Из файла")

    # Защищаем ввод способа ввода данных
    while True:
        input_method = input("Ваш выбор: ")
        if input_method in ["1", "2"]:
            break
        else:
            print("Неверный выбор способа ввода. Пожалуйста, выберите 1 или 2.")

    if input_method == "1":
        a, b, eps = input_from_keyboard(single=True)
    else:
        a, b, eps = input_from_file(single=True)

    if not has_root(f, a, b):
        print("На этом интервале нет корня или их несколько.")
        return

    if method_choice == "1":
        root, fval, iters = bisection_method(f, a, b, eps)
    elif method_choice == "2":
        root, fval, iters = secant_method(f, a, b, eps)
    elif method_choice == "3":
        x0 = choose_initial_guess(f, a, b)
        root, fval, iters = simple_iteration_method(f, x0, a, b, eps)
    else:
        print("Неизвестный метод.")
        return

    print("\nКуда вывести результат?")
    print("1. На экран")
    print("2. В файл")

    # Защищаем выбор вывода результата
    while True:
        out = input("Ваш выбор: ")
        if out in ["1", "2"]:
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

    if out == "1":
        output_to_screen(root, fval, iters)
    else:
        output_to_file(root, fval, iters)


def solve_system():
    print("\nВыберите систему:")
    for i, sys in enumerate(systems):
        print(f"{i + 1}. {sys['description']}")

    # Защищаем ввод от ошибок и проверяем, что индекс находится в допустимом диапазоне
    while True:
        try:
            sys_index = int(input("Номер системы: ")) - 1
            if sys_index < 0 or sys_index >= len(systems):
                print(f"Неверный номер системы. Пожалуйста, введите число от 1 до {len(systems)}.")
                continue
            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

    system = systems[sys_index]
    funcs = system["functions"]  # funcs теперь это список функций
    # Показываем график системы
    plot_system(funcs, x_range=(-5, 5), y_range=(-5, 5))  # Передаем список функций

    print("\nВыберите способ ввода данных:")
    print("1. С клавиатуры")
    print("2. Из файла")

    # Защищаем ввод способа ввода данных
    while True:
        input_method = input("Ваш выбор: ")
        if input_method in ["1", "2"]:
            break
        else:
            print("Неверный выбор способа ввода. Пожалуйста, выберите 1 или 2.")

    if input_method == "1":
        x0, y0, eps = input_from_keyboard(single=False)
    else:
        x0, y0, eps = input_from_file(single=False)

    # Передаем систему функций и начальное приближение
    root_vec, fval, iters = newton_method_system(funcs, [x0, y0], eps)

    print("\nКуда вывести результат?")
    print("1. На экран")
    print("2. В файл")

    # Защищаем выбор вывода результата
    while True:
        out = input("Ваш выбор: ")
        if out in ["1", "2"]:
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

    if out == "1":
        output_to_screen(root_vec, fval, iters)
    else:
        output_to_file(root_vec, fval, iters)


def main():
    while True:
        print("\nВыберите тип задачи:")
        print("1. Нелинейное уравнение")
        print("2. Система нелинейных уравнений")
        print("3. Выход")

        mode = input("Ваш выбор: ")

        if mode == "1":
            solve_equation()
        elif mode == "2":
            solve_system()
        elif mode == "3":
            print("Выход из программы.")
            break
        else:
            print("Неизвестный режим.")


if __name__ == "__main__":
    main()
