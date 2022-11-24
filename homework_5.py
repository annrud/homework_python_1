print(
    '''
Программа принимает на вход координаты двух точек и 
находит расстояние между ними в 2D пространстве.
'''
)
while True:
    try:
        x1, y1 = (float(i) for i in input(
            'Введите через пробел координаты точки A (x,  y): '
        ).split())
        x2, y2 = (float(i) for i in input(
            'Введите через пробел координаты точки B (x,  y): '
        ).split())
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        print(f'Расстояние между точками = {round(distance, 3)}')
    except ValueError:
        print('Неверный ввод!')
