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
