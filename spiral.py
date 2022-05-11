def spiralize(size):
    # создаю болванку: массив нужного размера из нулей  
    line = [0 for _ in range(size)]
    sample = [line for _ in range(size)]
    # Создаю курсор и храню его в словаре с двумя ключами: номер списка (вверх-вниз) и номер элемента (влево-вправо)
    cursor = {'line': 0, 'column': 0, 'dir': 'right'}
    # Рисую линию с механика поворота направо, меняя нули на единицы в нужных местах
    
    # one lap trial
    while True:        
        sample[cursor['line']][cursor['column']] = 1
    try:
        # next element
    except IndexError:
        change_direction(cursor)
    else:
        if 

            
    def change_direction(cursor):
        map = {
            'right': 'down',
            'down': 'left',
            'left': 'up',
            'up': 'right'
        }
        previous_dir = cursor['dir']
        cursor['dir'] = map[previous_dir]
    
    
    
    return spiral
