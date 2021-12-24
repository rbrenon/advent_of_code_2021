import re


def view_map(ocean_map: list):
    count_gt_1 = 0
    for index, level in enumerate(ocean_map):
        for element in ocean_map[index]:
            if element > 1:
                count_gt_1 += 1
        # print(ocean_map[index])
    print(f"Count greater than 1 = {count_gt_1}")


def plot_vent(coord_list: list, ocean_map: list) -> list:
    coord_count = 0
    for coord in coord_list:
        coords = re.split(r",|-|>| ", coord.strip())
        x1, y1 = int(coords[0]), int(coords[1])
        x2, y2 = int(coords[-2]), int(coords[-1])

        if x1 == x2:
            ocean_map = plot_horizontal(ocean_map, x1, y1, y2)
        elif y1 == y2:
            ocean_map = plot_vertical(ocean_map, x1, x2, y1)
        else:
            # print(f"diagonal line - {x1},{y1} -> {x2},{y2}")
            ocean_map = plot_diagonal(ocean_map, x1, x2, y1, y2)
        coord_count += 1
    print(coord_count)
    return ocean_map


def plot_diagonal(ocean_map: list, x1: int, x2: int, y1: int, y2: int) -> list:
    if x1 == y1 and x2 == y2:
        line_length = x1 - x2
        if line_length < 0:
            for point in range(abs(line_length) + 1):
                ocean_map[y1 + point][x1 + point] += 1
                # print(f"1.plotting {x1},{y1} -> {x2-point},{y2-point}")
        else:
            for point in range(line_length + 1):
                ocean_map[y2 + point][x2 + point] += 1
                # print(f"2.plotting {x1},{y1} -> {x2+point},{y2+point}")
    elif x1 == y2 and x2 == y1:
        line_length = x1 - y1
        if line_length < 0:
            for point in range(abs(line_length)+1):
                ocean_map[y2 + point][x2 - point] += 1
                # print(f"3.plotting {x1},{y1} -> {x2-point},{y2+point}")
        else:
            for point in range(line_length + 1):
                ocean_map[y1 + point][x1 - point] += 1
                # print(f"4.plotting {x1-point},{y1+point} -> {x2},{y2}")
    else:
        # print(f"5-6.diag input: {x1},{y1} -> {x2},{y2}")
        line_length = x1 - x2
        x_diff = x1 - x2
        y_diff = y1 - y2
        if x_diff < 0 < y_diff:
            for point in range(abs(line_length) + 1):
                ocean_map[y1 - point][x1 + point] += 1
                # print(f"5.plotting point: {x1+point}, {y1-point}")
        elif y_diff < 0 < x_diff:
            for point in range(abs(line_length) + 1):
                ocean_map[y1 + point][x1 - point] += 1
                # print(f"5.plotting point: {x1-point}, {y1+point}")
        elif x_diff < 0 and y_diff < 0:
            for point in range(abs(line_length) + 1):
                ocean_map[y1 + point][x1 + point] += 1
                print(f"5.plotting point: {x1 + point}, {y1 + point}")
        elif x_diff > 0 and y_diff > 0:
            for point in range(line_length +1):
                ocean_map[y2 + point][x2 + point] += 1
                # print(f"5.plotting point: {x2 + point}, {y2 + point}")
        else:
            print('scenario not covered')
            # for point in range(line_length + 1):
            #     ocean_map[y2 + point][x2 + point] += 1
            #     print(f"6.plotting point {x2+point},{y2+point}")
    return ocean_map


def plot_horizontal(ocean_map: list, x: int, y1: int, y2: int) -> list:
    line_height = y1 - y2
    if line_height < 0:
        for point in range(abs(line_height)+1):
            # print(f"plot x: {x}, y: {y1 + point}")
            ocean_map[y1 + point][x] += 1
    else:
        for point in range(line_height+1):
            # print(f"plot x: {x}, y: {y2 + point}")
            ocean_map[y2 + point][x] += 1
    return ocean_map


def plot_vertical(ocean_map: list, x1: int, x2: int, y: int) -> list:
    line_depth = x1 - x2
    # print(f"x1: {x1}, x2: {x2}, line depth: {line_depth}")
    if line_depth < 0:
        for point in range(abs(line_depth)+1):
            # print(f"plot x: {x1 + point}, y: {y}")
            ocean_map[y][x1 + point] += 1
    else:
        for point in range(line_depth+1):
            # print(f"plot x: {x2 + point}, y: {y}")
            ocean_map[y][x2 + point] += 1
    return ocean_map


def main():
    with open("input.txt") as f:
        coord_list = f.readlines()

    ocean_map = [[0 for _ in range(1000)] for _ in range(1000)]
    ocean_map = plot_vent(coord_list, ocean_map)

    view_map(ocean_map)


if __name__ == "__main__":
    main()

# 5-1
# 6908

# 5-2
# 7364
# 17527 - too low
