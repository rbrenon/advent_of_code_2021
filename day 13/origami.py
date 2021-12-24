import pprint
from operator import itemgetter


def main(filename: str):
    coords, folds = parse_input(filename)
    # print(coords, "\n\n", folds)
    max_x = max(coords, key=itemgetter(0))[0] + 1
    max_y = max(coords, key=itemgetter(1))[1] + 1

    paper = [[0 for _ in range(max_x)] for _ in range(max_y)]

    for coord in coords:
        y = coord[0]
        x = coord[1]
        # print(x, y)
        paper[x][y] = 1
    # pprint.pprint(paper)

    for fold in folds:
        paper, max_x, max_y = fold_paper(paper, fold, max_x, max_y)
    # pprint.pprint(paper)


    dot_count = 0
    for row_index, _ in enumerate(paper):
        for col_index, element in enumerate(paper[row_index]):
            if element == 1:
                dot_count += 1
    print(dot_count)
    print(paper)




def fold_paper(paper: list, folds: list, max_x: int, max_y: int) -> list:
    # print(folds[0], folds[1])
    fold_at = folds[1]
    if folds[0] == 'y':
        for row_index, _ in enumerate(paper):
            for col_index, element in enumerate(paper[row_index]):
                if element == 1:
                    pass
                else:
                    mirror_x = col_index
                    mirror_y = (max_y - 1) - row_index
                    paper[row_index][col_index] = paper[mirror_y][mirror_x]
        while len(paper) > fold_at:
            paper.pop()
            max_y = len(paper)
    elif folds[0] == 'x':
        for row_index, _ in enumerate(paper):
            for col_index, element in enumerate(paper[row_index]):
                if element == 1:
                    pass
                else:
                    mirror_x = (max_x - 1) - col_index
                    mirror_y = row_index
                    paper[row_index][col_index] = paper[mirror_y][mirror_x]
            while len(paper[row_index]) > fold_at:
                paper[row_index].pop()
        max_x = len(paper[row_index])
    return paper, max_x, max_y


def parse_input(filename: str) -> list:
    coords, folds = [], []
    with open(filename) as f:
        for line in f.readlines():
            if len(line.strip().split(",")) == 2:
                line = line.strip().split(",")
                # print(line[0], line[1])
                x_coord = int(line[0])
                y_coord = int(line[1])
                coords.append((x_coord, y_coord))
            elif "fold" in line.split():
                line = line.strip().split("=")
                fold_axis = line[0][-1]
                fold_index = int(line[-1])
                folds.append((fold_axis, fold_index))

    return coords, folds


if __name__ == "__main__":
    main("input.txt")