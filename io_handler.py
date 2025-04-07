def input_from_keyboard(single=True):
    print("\nВведите данные:")

    if single:
        a = float(input("Левая граница интервала a: "))
        b = float(input("Правая граница интервала b: "))
        eps = float(input("Точность (ε): "))
        return a, b, eps
    else:
        x0 = float(input("Начальное приближение x0: "))
        y0 = float(input("Начальное приближение y0: "))
        eps = float(input("Точность (ε): "))
        return x0, y0, eps


def input_from_file(single=True, filename='data/input.txt'):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if single:
                a = float(lines[0])
                b = float(lines[1])
                eps = float(lines[2])
                return a, b, eps
            else:
                x0 = float(lines[0])
                y0 = float(lines[1])
                eps = float(lines[2])
                return x0, y0, eps
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return input_from_keyboard(single)


def output_to_screen(root, f_val, iterations):
    print("\nРезультат:")
    print(f"Найденный корень/вектор: {root}")
    print(f"Значение функции в корне: {f_val}")
    print(f"Число итераций: {iterations}")


def output_to_file(root, f_val, iterations, filename='data/output.txt'):
    try:
        with open(filename, 'w') as file:
            file.write("Результат вычислений:\n")
            file.write(f"Найденный корень/вектор: {root}\n")
            file.write(f"Значение функции в корне: {f_val}\n")
            file.write(f"Число итераций: {iterations}\n")
        print(f"\n Результаты сохранены в файл: {filename}")
    except Exception as e:
        print(f" Ошибка при записи в файл: {e}")
        output_to_screen(root, f_val, iterations)
