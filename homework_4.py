print(
    '''
Программа показывает диапазон возможных координат точек (x и y)
по заданному номеру четверти координатной плоскости.
'''
)
while True:
    try:
        quarter_number = int(
            input('Введите номер координатной четверти (1, 2, 3 или 4): ')
        )
        if quarter_number < 1 or quarter_number > 4:
            print('Вы ввели не номер координатной плоскости!')
        elif quarter_number == 1:
            print('Диапазон возможных координат: x > 0, y > 0')
            break
        elif quarter_number == 2:
            print('Диапазон возможных координат: x < 0, y > 0')
            break
        elif quarter_number == 3:
            print('Диапазон возможных координат: x < 0, y < 0')
            break
        else:
            print('Диапазон возможных координат: x > 0, y < 0')
            break
    except ValueError:
        print('Вы ввели не номер координатной плоскости!')
