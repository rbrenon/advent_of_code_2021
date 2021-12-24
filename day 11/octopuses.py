

def main():
    with open("testinput.txt") as f:
        raw_input = f.read().splitlines()
        # print(raw_input)

    octi = []

    for row_index, row in enumerate(raw_input):
        octi.append([])
        for element in row:
            octi[row_index].append(int(element))

    for step in range(10):
        print(f"step number: {step}")
        for row in octi:
            print(row)
        octi = take_one_step(octi)
        octi = check_for_flashes(octi)


def take_one_step(octi: list) -> list:
    for row_index, row in enumerate(octi):
        for column_index, element in enumerate(octi):
            # element
            octi[row_index][column_index] += 1
    return octi


def check_for_flashes(octi: list):
    flashes = 0
    for row_index, row in enumerate(octi):
        for column_index, element in enumerate(row):
            # element
            if octi[row_index][column_index] > 9:
                print(f"{element}: {row_index}, {column_index}")
                octi[row_index][column_index] = 0
                flashes += 1
    print(f"flashes = {flashes}")
    return octi


def increment_surrounding(octi: list, row_index: int, column_index: int) -> list:
    octi = increment(octi, row_index - 1, column_index)
    # upper-right
    octi = increment(octi, row_index - 1, column_index + 1)
    # right
    octi = increment(octi, row_index, column_index + 1)
    # lower-right
    octi = increment(octi, row_index + 1, column_index + 1)
    # below
    octi = increment(octi, row_index + 1, column_index)
    # lower-left
    octi = increment(octi, row_index + 1, column_index - 1)
    # left
    octi = increment(octi, row_index + 1, column_index)
    # upper-left
    octi = increment(octi, row_index - 1, column_index - 1)
    return octi


def increment(octi: list, row: int, col: int) -> list:
    try:
        octi[row][col] += 1
    except:
        pass
    return octi


if __name__ == "__main__":
    main()
