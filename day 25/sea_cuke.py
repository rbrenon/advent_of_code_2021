from collections import defaultdict
from pprint import pprint


def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    sea_floor = defaultdict(list)
    for index, row in enumerate(raw_input):
        sea_floor[index] = [char for char in row]
    pprint(sea_floor)

    cant_step = 0
    steps = 0
    while cant_step < 2:
        steps += 1
        cant_step = 0
        step_right = find_cukes_to_move_right(sea_floor)
        if len(step_right) > 0:
            sea_floor = apply_step(sea_floor, step_right)
            # pprint(sea_floor)
        else:
            cant_step += 1
        step_down = find_cukes_to_move_down(sea_floor)
        if len(step_down) > 0:
            sea_floor = apply_step(sea_floor, step_down)
            # pprint(sea_floor)
        else:
            cant_step += 1
    print(steps)    # 563


def find_cukes_to_move_right(sea_floor: defaultdict) -> list:
    move_list = []
    for row_index, row in enumerate(sea_floor.items()):
        for col_index, element in enumerate(sea_floor[row_index]):
            if element == '>':
                next_col_index = (col_index+1) % (len(sea_floor[row_index]))
                if sea_floor[row_index][next_col_index] == ".":
                    move_list.append((row_index, col_index, row_index, next_col_index))
    # print(move_list)
    return move_list


def find_cukes_to_move_down(sea_floor: defaultdict) -> list:
    move_list = []
    for row_index, row in enumerate(sea_floor.items()):
        for col_index, element in enumerate(sea_floor[row_index]):
            if element == 'v':
                next_row_index = (row_index+1) % len(sea_floor)
                if sea_floor[next_row_index][col_index] == ".":
                    move_list.append((row_index, col_index, next_row_index, col_index))
    # print(move_list)
    return move_list


def apply_step(sea_floor: defaultdict, step_coords: list) -> defaultdict:
    for coords in step_coords:
        source_row, source_col, target_row, target_col = coords
        sea_floor[target_row][target_col] = sea_floor[source_row][source_col]
        sea_floor[source_row][source_col] = "."
    return sea_floor


if __name__ == "__main__":
    main()