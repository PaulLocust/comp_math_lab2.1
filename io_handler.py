def safe_float_input(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число (например, 2.5 или 2,5).")


def input_from_keyboard(single=True):
    print("\nВведите данные:")

    if single:
        a = safe_float_input("Левая граница интервала a: ")
        b = safe_float_input("Правая граница интервала b: ")
        eps = safe_float_input("Точность (ε): ")
        return a, b, eps
    else:
        x0 = safe_float_input("Начальное приближение x0: ")
        y0 = safe_float_input("Начальное приближение y0: ")
        eps = safe_float_input("Точность (ε): ")
        return x0, y0, eps


def input_from_file(single=True, filename='data/input.txt'):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Убираем пробелы и заменяем запятую на точку
            values = [float(line.strip().replace(',', '.')) for line in lines]

            if single:
                a, b, eps = values[0], values[1], values[2]
                return a, b, eps
            else:
                x0, y0, eps = values[0], values[1], values[2]
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
