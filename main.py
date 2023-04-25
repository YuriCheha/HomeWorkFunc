def login_attempts(func):
    def wrapper():
        attempts = 3
        while attempts > 0:
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if username == 'Cheha Yury' and password == 'sacra136':
                func()
                break
            else:
                attempts -= 1
                if attempts == 0:
                    print("Вы исчерпали все попытки. Попробуйте позже.")
                else:
                    print(f"Неверный логин или пароль. Осталось попыток: {attempts}")
    return wrapper
@login_attempts
def secret_function():
    print("Функция выполнена успешно")
print(secret_function())

def author_writer(sep='.', **kwargs):
    a = kwargs['name'][0]
    b = kwargs['patr'][0]
    surname = kwargs['surname']
    birth = kwargs['birth']
    death = kwargs['death']
    krt = kwargs['krt']
    return f'{a}{sep}{b}{sep}{surname} ({birth} - {death}) - {krt}'
print(author_writer(name='Александр', patr='Сергеевич', surname='Пушкин', birth='06.06.1799', death='10.01.1837',krt='Драматург, русский поэт'))

def count_numbers(*args):
    def get_digit_count(number):
        return len(str(number))
    two_digit_count = 0
    three_digit_count = 0
    for number in args:
        digit_count = get_digit_count(number)
        if digit_count == 2:
            two_digit_count += 1
        elif digit_count == 3:
            three_digit_count += 1

    print(f'Двузначных чисел: {two_digit_count}, трехзначных чисел: {three_digit_count}')
print(count_numbers(156, 456, 88888))
