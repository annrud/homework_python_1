print(
    '''
Программа проверяет истинность утверждения: 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
)
predicate = True
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not(not (x and y and z) == (not x or not y or not z)):
                predicate = False
                break
print('Высказывание верно.' if predicate else 'Высказывание не верно.')
