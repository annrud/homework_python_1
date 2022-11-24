print('Программа проверяет является ли день недели выходным днём.')
while True:
    try:
        day = int(input('Введите номер дня недели: '))
        if 1 <= day <= 7:
            print(
                'Да, это выходной день' if day == 6 or day == 7
                else 'Нет, это не выходной день'
            )
            break
        else:
            print('Введите число от 1 до 7!')
    except ValueError:
        print('Вы ввели не номер дня недели!')
