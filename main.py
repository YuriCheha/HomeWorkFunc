# def authorization(username, password,max_attempts=3, message='Система заблокирована. Повторите попытку через 5 минут'):
#     attempts = -1
#     username = input('Введите имя пользователя: ')
#     password = input('Введите пароль: ')
#     while attempts < max_attempts:
#         if username == 'Cheha Yury' and password == 'sacra136':
#             print('Доступ разрешен')
#             return True
#         else:
#             attempts += 1
#             print(f"Неверный логин или пароль. Осталось попыток: {max_attempts - attempts}")
#             return False
# total = authorization(username, password)
# print(total)

# def author_info(**kwargs):
#     full_name = kwargs.get('full_name', '')
#     birth_date = kwargs.get('birth_date', '')
#     death_date = kwargs.get('death_date', '')
#     description = kwargs.get('description', '')
#
#     if full_name:
#         initials = ''.join([name[0] + '.' for name in full_name.split()])
#         print(f'{initials} {full_name.split()[-1]} ({birth_date} - {death_date}) {description}')
#     else:
#         print('Информация об авторе отсутствует')
# author_info(full_name='Иван Сергеевич Тургенев', birth_date='28 октября 1818', death_date='22 августа 1883', description='русский писатель и общественный деятель')
# print(author_info())

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