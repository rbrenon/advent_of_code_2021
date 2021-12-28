from statistics import median
from pprint import pprint

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    # part_1(raw_input)
    part_2(raw_input)


def part_1(raw_input: list) -> None:
    symbol_pairs = {"]": "[", ")": "(", ">": "<", "}": "{"}
    symbol_values = {"]": 57, ")": 3, ">": 25137, "}": 1197}
    symbol_list = []
    error_score = 0

    for row in raw_input:
        for element in row:
            if element in symbol_pairs.values():
                symbol_list.append(element)
            elif element in symbol_pairs.keys():
                if symbol_list[-1] == symbol_pairs.get(element):
                    symbol_list.pop(-1)
                else:
                    error_score += symbol_values[element]
                    break
        # print(symbol_list)
    print(f"Part 1: {error_score}")  # 311895


def part_2(raw_input: list) -> None:
    symbol_pairs = {"]": "[", ")": "(", ">": "<", "}": "{"}
    symbol_values = {"]": 57, ")": 3, ">": 25137, "}": 1197}
    symbol_list = []
    invalid_row = 0

    valid_rows = []
    for row_key, row_value in enumerate(raw_input):
        valid_row = True
        symbol_list = []
        for element in row_value:
            if element in symbol_pairs.values():
                symbol_list.append(element)
            elif element in symbol_pairs.keys():
                if symbol_list[-1] == symbol_pairs.get(element):
                    symbol_list.pop(-1)
                else:
                    valid_row = False
                    invalid_row += 1
                    break

        if valid_row:
            valid_rows.append(symbol_list)
    print(invalid_row)

    symbol_score = {"(": 1, "[": 2, "{": 3, "<": 4}

    row_scores = []
    for row in valid_rows:
        score = 0
        for symbol in reversed(row):
            score *= 5
            score += symbol_score[symbol]
        row_scores.append(score)


    list.sort(row_scores)
    pprint(f"Part 2: {list((index, score) for index, score in enumerate(row_scores))}")

    print(f"Median value = {median(row_scores)}")
    # 3308036587 - too high
    # 2904180541 - winner


if __name__ == "__main__":
    main()
