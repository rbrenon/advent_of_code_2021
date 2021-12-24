from pprint import pprint
import math


def main():
    basins = []
    for row_index, row_val in enumerate(vent_array):
        for col_index, col_val in enumerate(row_val):
            value = vent_array[row_index][col_index]
            if value in [-1, 9]:
                pass
            else:
                try:
                    right = vent_array[row_index][col_index+1]
                except IndexError:
                    right = 99
                try:
                    below = vent_array[row_index+1][col_index]
                except IndexError:
                    below = 99
                try:
                    if col_index > 0:
                        left = vent_array[row_index][col_index-1]
                    else:
                        raise IndexError
                except IndexError:
                    left = 99
                try:
                    if row_index > 0:
                        above = vent_array[row_index-1][col_index]
                    else:
                        raise IndexError
                except IndexError:
                    above = 99

                total_basin_size = 1
                for adjacent_value in [right, below, left, above]:
                    if adjacent_value < value:
                        # low_point.extend((row_index, col_index))
                        vent_array[row_index][col_index] = -1
                        total_basin_size += find_basin(row_index, col_index)
                if total_basin_size > 0:
                    print(f'basin size = {total_basin_size}')
                    basins.append(total_basin_size)

                # print(f"val: {value}, r: {right}, b: {below}, l: {left}, a: {above}")

    print(basins)
    top_basins = sorted(basins, reverse=True)[:3]
    print(*top_basins)
    tb_prod = math.prod(top_basins)
    print(tb_prod)
    # pprint(vent_array)


def find_basin(row: int, column: int) -> int:
    basin_size = 0
    try:  # look to right until hit a 9
        while vent_array[row][column + 1] < 9 and vent_array[row][column + 1] != -1:
            vent_array[row][column + 1] = -1
            basin_size += 1
            basin_size += find_basin(row, column + 1)
    except IndexError:
        right = 99
    try: # look down until find a 9
        while vent_array[row + 1][column] < 9 and vent_array[row + 1][column] != -1:
            vent_array[row + 1][column] = -1
            basin_size += 1
            basin_size += find_basin(row + 1, column)
    except IndexError:
        below = 99
    try:  # check left
        while column - 1 >= 0 and vent_array[row][column - 1] < 9 and vent_array[row][column - 1] != -1:
            vent_array[row][column - 1] = -1
            basin_size += 1
            basin_size += find_basin(row, column - 1)
    except IndexError:
        left = 99
    try:  # check above
        while row - 1 >= 0 and vent_array[row - 1][column] < 9 and vent_array[row - 1][column] != -1:
            vent_array[row - 1][column] = - 1
            basin_size += 1
            basin_size += find_basin(row - 1, column)
    except IndexError:
        above = 99
    return basin_size


if __name__ == "__main__":
    with open("input.txt") as f:
        raw_data = f.readlines()

    vent_array = [[int(element) for element in element.strip()] for element in raw_data]
    main()

# 1330560