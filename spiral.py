# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
# Make a spiral (size >= 5)
# Here is my solution, took about 3,5 hours
# No hints, no google

# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000

# Should return this:
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

def spiralize(size):
    # создаю болванку: массив нужного размера из нулей  
    line = [0 for _ in range(size)]
    sample = [line for _ in range(size)]
    # Создаю курсор и храню его в словаре с двумя ключами: номер списка (вверх-вниз) и номер элемента (влево-вправо)
    cursor = {'line': 0, 'column': 0, 'direction': 'right'}
    
    def spiral_walk_and_draw(cursor):
        # read current state
        line, column, direction = cursor['line'], cursor['column'], cursor['direction']
        # replace initial zero with this value:
        sample[line][column] = 1
        # now move cursor
        if direction = 'right':
            # perimeter lap
            try:             
                next_item = sample[line][column + 1]
            except IndexError:
                change_direction(cursor)
            else:
                cursor['column'] += 1
                # subsequet laps
                try:
                    next_next_item = sample[line][column + 2]
                    if next_next_item = 1:
                        change_direction(cursor)
                except IndexError:
                    pass
        
        elif direction = 'down':
            # perimeter lap
            try:
                next_item = sample[line + 1][column]
            except IndexError:
                change_direction(cursor)
            else:
                cursor['line'] += 1
                # subsequet laps
                try:
                    next_next_item = sample[line + 2][column]
                    if next_next_item == 1:
                        change_direction(cursor)
                except IndexError:
                    pass            
  
        elif direction = 'left':
            try:
                next_next_item = sample[line][column - 2]
                is_enough_this_way = (next_next_item == 1 or line == 0)
                if is_enough_this_way:
                    change_direction(cursor)
                else:
                    cursor['column'] -= 1
            except IndexError:
                    pass
     
        elif direction = 'up':
            try:
                next_next_item = sample[line - 2][column]
                is_enough_this_way = (next_next_item == 1 or line == 0)
                if is_enough:
                    change_direction(cursor)
                else:
                    cursor['line'] -= 1
            except IndexError:
                    pass
  

     def change_direction(cursor):
        shifts = {
            'right': 'down',
            'down': 'left',
            'left': 'up',
            'up': 'right'
        }
        previous_dir = cursor['dir']
        new_dir = shifts[previous_dir]
        cursor['dir'] = new_dir
    
    # Рисую линию, начиная с верхней левой точки
    # Механика поворота направо, меняю нули на единицы на своем пути
    while True:
        spiral_walk_and_draw(cursor)
        if cursor['direction'] = 'STOP':
            break
     
    # болванка изменена "на месте", теперь это спираль из матриц!
    spiral = sample
    return spiral
