

def main():
    with open("input.txt") as f:
        raw_data = f.readlines()

    vent_array = [[int(element) for element in element.strip()] for element in raw_data]
    # print(vent_array)
    # print(len(vent_array[0]), vent_array[0][0], vent_array[0][1], vent_array[1][0], len(vent_array))

    low_point = []
    for row_index, row_val in enumerate(vent_array):
        for col_index, col_val in enumerate(row_val):
            value = vent_array[row_index][col_index]
            try:
                right = vent_array[row_index][col_index+1]
            except IndexError:
                right = 99
            try:
                below = vent_array[row_index+1][col_index]
            except IndexError:
                below = 99
            try:
                left = vent_array[row_index][col_index-1]
            except IndexError:
                left = 99
            try:
                above = vent_array[row_index-1][col_index]
            except IndexError:
                above = 99

            if value < min(right, below, left, above):
                low_point.append(value+1)

            print(f"val: {value}, r: {right}, b: {below}, l: {left}, a: {above}")

    print(sum(low_point))


def find_basin(row:int, column:int) -> int:
    basin_size = 0


if __name__ == "__main__":
    main()