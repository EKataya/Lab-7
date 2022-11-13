import logging
# Работаем с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создаем файл для логирования
file_handler = logging.FileHandler("log.log")
# Создаем форматер, отображающий дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

while True:
    # Проверяем на ввод данных и вводим данные
    try:
        k = int(input('Введите координату клетки фигуры по горизонтали: '))
        if k > 8 or k < 0:
            print('Введены неверные данные. Попробуйте снова.')
            continue
        l = int(input('Введите координату клетки фигуры по вертикали: '))
        if l > 8 or l < 0:
            print('Введены неверные данные. Попробуйте снова.')
            continue
        m = int(input('Введите координату атакуемой клетки по горизонтали: '))
        if m > 8 or m < 0:
            print('Введены неверные данные. Попробуйте снова.')
            continue
        n = int(input('Введите координату атакуемой клетки по вертикали: '))
        if n > 8 or n < 0:
            print('Введены неверные данные. Попробуйте снова.')
            continue
        figure = int(input('''Выберите  фигуру, которую вы хотите использовать?
        1 -- Ферзь
        2 -- Ладья
        3 -- Слон
        4 -- Конь
        Ваш выбор: '''))
        if figure > 4 or figure < 0:
            print('Введены неверные данные. Попробуйте снова.')
            continue
    except ValueError:
        print('Введены неверные данные. Попробуйте снова.')
        continue

    # Проверяем на совпадение цвета
    if (k + l) % 2 == (m + n) % 2:
        print('Они одного цвета -', end=' ')
        if (k + l) % 2 == 0:
            print('белого')
        else:
            print('черного')
    else:
        print('Нет, они не одного цвета')

    # Расстояние по горизонтали и вертикали
    dx = abs(k - m)
    dy = abs(l - n)

    # Проверяем, угрожает ли фигура полю, а также делаем второй ход
    if figure == 1:     # Ферзь
        if k == m or l == n or dx == dy:
            print(f'Ферзь угрожает полю ({m}; {n})')
        else:
            print(f'Ферзь не угрожает полю ({m}; {n})')
            print(f'Чтобы за два хода попасть на поле, необходимо встать на поле ({m}; {l})')
    elif figure == 2:   # Ладья
        if k == m or l == n:
            print(f'Ладья угрожает полю ({m}; {n})')
        else:
            print(f'Ладья не угрожает полю ({m}; {n})')
            print(f'Чтобы за два хода попасть на  поле, необходимо встать на поле ({m}; {l})')
    elif figure == 3:   # Слон
        if dx == dy:
            print(f'Слон угрожает полю ({m}; {n})')
        else:
            print(f'Слон не угрожает полю ({m}; {n})')
            if (k + l) % 2 != (m + n) % 2:
                print(f'Слон никаким образом не может угрожать полю ({m}; {n})')
            else:  
                m0, n0, m1, n1 = m, n, 0, 0
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 += 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 -= 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 += 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 -= 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
    else:   # Конь
        if abs(dx - dy) == 1:
            print(f'Конь угрожает полю ({m}; {n})')
        else:
            print(f'Конь не угрожает полю ({m}; {n})')
    break
logger.info('Program done')

