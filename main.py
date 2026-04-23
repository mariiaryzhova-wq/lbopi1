# Функція для обчислення факторіалу
def factorial(n):
    """Обчислює факторіал числа n."""
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних цілих чисел")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Приклад використання
if __name__ == "__main__":
    number = 5
    print(f"{number}! = {factorial(number)}")
    print(f"{number + 3}! = {factorial(number + 3)}")