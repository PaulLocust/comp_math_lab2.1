
from functions import equations, systems
from io_handler import input_from_keyboard, input_from_file, output_to_screen, output_to_file
from nonlinear_equations.simple_iterations import simple_iteration_method
from validators import has_root, check_convergence_simple_iteration, choose_initial_guess
from plotting import plot_function


def solve_equation():
    print("\nВыберите уравнение:")
    for i, eq in enumerate(equations):
        print(f"{i + 1}. {eq['description']}")

    eq_index = int(input("Номер уравнения: ")) - 1
    equation = equations[eq_index]
    f = equation["function"]

    # Показываем график функции
    plot_function(f, -10, 10, title=f"График: {equation['description']}")

    print("\nВыберите метод:")
    print("1. Метод половинного деления")
    print("2. Метод секущих")
    print("3. Метод простой итерации")
    method_choice = input("Ваш выбор: ")

    print("\nВыберите способ ввода данных:")
    print("1. С клавиатуры")
    print("2. Из файла")
    input_method = input("Ваш выбор: ")

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
    out = input("Ваш выбор: ")

    if out == "1":
        output_to_screen(root, fval, iters)
    else:
        output_to_file(root, fval, iters)


def solve_system():
    print("\nВыберите систему:")
    for i, sys in enumerate(systems):
        print(f"{i + 1}. {sys['description']}")

    sys_index = int(input("Номер системы: ")) - 1
    system = systems[sys_index]
    funcs = system["functions"]
    jacobian = system["jacobian"]

    print("\nВыберите способ ввода данных:")
    print("1. С клавиатуры")
    print("2. Из файла")
    input_method = input("Ваш выбор: ")

    if input_method == "1":
        x0, y0, eps = input_from_keyboard(single=False)
    else:
        x0, y0, eps = input_from_file(single=False)

    root_vec, fval, iters = newton_method_system(funcs, jacobian, [x0, y0], eps)

    print("\nКуда вывести результат?")
    print("1. На экран")
    print("2. В файл")
    out = input("Ваш выбор: ")

    if out == "1":
        output_to_screen(root_vec, fval, iters)
    else:
        output_to_file(root_vec, fval, iters)


def main():
    print("Выберите тип задачи:")
    print("1. Нелинейное уравнение")
    print("2. Система нелинейных уравнений")

    mode = input("Ваш выбор: ")

    if mode == "1":
        solve_equation()
    elif mode == "2":
        solve_system()
    else:
        print("Неизвестный режим.")


if __name__ == "__main__":
    main()
