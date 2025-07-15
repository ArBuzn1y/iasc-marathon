    # Функції

def hello_world():
    print("Hello, world!")
hello_world()
def greet(name="Гість"):
    print(f"Привіт, {name}!")
greet("Anna")
greet()
def square(n):
    return n * n
print("Квадрат 5:", square(5))
def add(a, b):
    return a + b
print("Сума 3 + 7:", add(3, 7))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Факторіал 5:", factorial(5))
def is_even(n):
    return n % 2 == 0
print("Число 4 парне?", is_even(4))
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
print_numbers(5)
def find_name(name, name_list):
    return name in name_list
print("Чи є 'Oleh' у списку?", find_name("Oleh", ["Anna", "Oleh", "Ivan"]))
def max_of_three(a, b, c):
    return max(a, b, c)
print("Максимум із 3, 7, 2:", max_of_three(3, 7, 2))
def reverse_string(s):
    return s[::-1]
print("Навпаки 'Привіт':", reverse_string("Привіт"))
def count_vowels(s):
    vowels = "аеєиіїоуюяAEIOUYaeiouy"
    return sum(1 for char in s if char in vowels)
print("Голосних у 'Hello world':", count_vowels("Hello world"))
def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0
print("Середнє з 2, 4, 6:", average(2, 4, 6))
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print("Інформація про користувача:")
def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()
print_user_info(name="Ivan", age=30, city="Lviv")
outer()