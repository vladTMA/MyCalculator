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

result = None # Объявим result заранее до блока if

while True:
    command = input("Введите действие (+, -, *, /) или 'выход': ").strip().lower()
    if command == "выход":
       print("Завершение работы")
       break

    if command not in ("+", "-", "*", "/"):
       print("Неизвестная команда. попробуйте снова. ")
       continue

    try:
       num1 = float(input("Введите первое число: "))
       num2 = float(input("Введите второе число "))

       if command == "+":
          result = add(num1, num2)
       elif command == "-":
          result = substract(num1, num2)
       elif command == "*":
          result = multiply(num1, num2)
       elif command == "/":
          result = divide(num1, num2)

       print(f"Рузультат: {result}")
    except ValueError as e:
       print(f"Ошибка: {e}")


