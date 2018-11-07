import robot_api

go_down = ['DOWN']

go_up = ['UP',]

go_right = ['RIGHT']

go_left = ['LEFT']

go_down_five_times = go_down*5 
go_right_three_times = go_right*3 
go_left_two_times = go_left*2 
go_right_two_times = go_right*2
go_up_five_times = go_up*5
go_up_left_up = go_up + go_left + go_up
go_up_four_times = go_up*4


def first_room():
    map_for_first_room = []
    map_for_first_room = go_down_five_times + go_right_three_times + go_up + go_left_two_times + go_up + go_right_two_times + go_up + go_left_two_times + go_up + go_right_three_times 
    return map_for_first_room

def second_room():
    map_for_second_room = []
    map_for_second_room = go_right + go_down_five_times + go_right + go_up_five_times + go_right + go_down_five_times + go_right
    return map_for_second_room

def third_room(): 
    map_for_third_room = []
    map_for_third_room = go_right_two_times + go_up_left_up + go_right + go_up_left_up + go_right_three_times + go_down_five_times + go_right
    return map_for_third_room

def fourth_room():
    map_for_fourth_room = []
    map_for_fourth_room = go_right + go_up_five_times + go_right + go_down_five_times + go_right + go_up_four_times
    return map_for_fourth_room

def all_flat(map_for_first_room, map_for_second_room, map_for_third_room, map_for_fourth_room):
    map_for_all_flat = []
    map_for_all_flat = map_for_first_room + map_for_second_room + map_for_third_room + map_for_fourth_room
    return map_for_all_flat

def main(map_for_all_flat):
    room = robot_api.get_room_map()
    movement_history = run_robot(commands=map_for_all_flat, room_map=room)
    print_map(movement_history, room)


def run_robot(commands, room_map):
    command_deltas = { 
        'DOWN': (1, 0), 
        'RIGHT': (0, 1),
        'LEFT': (0, -1), 
        'UP': (-1, 0), 
    }
    current_position = robot_api.get_robot_position()
    movement_history = [current_position]
    for command in commands:
        delta = command_deltas[command]
        new_position = (current_position[0] + delta[0], current_position[1] + delta[1])
        if is_wall(new_position, room_map):
            continue  # Из-за этой команды мы врежемся в стенку. Проигнорируем её.

        movement_history.append(new_position)
        robot_api.send_delta_to_engine(delta)
        current_position = new_position
    return movement_history


def is_wall(position, ascii_map):
    map_array = turn_ascii_map_into_array(ascii_map)
    return map_array[position[0]][position[1]] == '█'


def print_map(movement_history, room_map):
    if not movement_history:
        print(room_map)
        return
    footprint_positions = movement_history[:-1]
    robot_position = movement_history[-1]
    map_with_footprints = get_map_with_footprints(footprint_positions, room_map)
    map_with_footprints_and_robot = get_map_with_robot(robot_position, map_with_footprints)
    print(map_with_footprints_and_robot)


def get_map_with_footprints(movement_history, room_map):
    footprint_mark = '·'
    return add_symbol_to_ascii_map(ascii_map=room_map, symbol=footprint_mark, points=movement_history)


def get_map_with_robot(robot_position, room_map):
    robot_mark = '◆'
    return add_symbol_to_ascii_map(ascii_map=room_map, symbol=robot_mark, points=[robot_position])


def add_symbol_to_ascii_map(ascii_map, symbol, points):
    map_array = turn_ascii_map_into_array(ascii_map)
    for point_x, point_y in points:
        map_array[point_x][point_y] = symbol
    return turn_array_into_ascii_map(map_array)


def turn_ascii_map_into_array(ascii_map):
    return [list(map_line) for map_line in ascii_map.split('\n') if map_line.strip()]


def turn_array_into_ascii_map(map_array):
    return '\n'.join([''.join(map_line) for map_line in map_array])

if __name__ == '__main__': 
    first_room()
    second_room()
    third_room()
    fourth_room()
    map_for_first_room = first_room()
    map_for_second_room = second_room()
    map_for_third_room = third_room()
    map_for_fourth_room = fourth_room()
    all_flat(map_for_first_room, map_for_second_room, map_for_third_room, map_for_fourth_room)
    map_for_all_flat = all_flat(map_for_first_room, map_for_second_room, map_for_third_room, map_for_fourth_room)
    main(map_for_all_flat)


