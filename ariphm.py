def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

exit_commands = ("выход", "q")

while True:
    result = None  # Сбрасываем перед каждой итерацией
    try:
        # Ввод первого числа
        raw1 = input("Введите первое число (или 'выход' / 'q'): ").strip().lower()
        if raw1 in exit_commands:
            print("Завершение работы")
            break
        num1 = float(raw1)

        # Ввод второго числа
        raw2 = input("Введите второе число (или 'выход' / 'q'): ").strip().lower()
        if raw2 in exit_commands:
            print("Завершение работы")
            break
        num2 = float(raw2)

        # Ввод команды
        command = input("Введите действие (+, -, *, /) или 'выход': ").strip().lower()
        if command == "выход":
            print("Завершение работы")
            break

       # Вычисление
        if command == "+":
          result = add(num1, num2)
        elif command == "-":
          result = substract(num1, num2)
        elif command == "*":
          result = multiply(num1, num2)
        elif command == "/":
          result = divide(num1, num2)
        else:
           print("Неизвестная команда. попробуйте снова. ")
           continue

        print(f"Рузультат: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")


