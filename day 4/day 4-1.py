

class CreateBoard:
    board_no = 0
    def __init__(self, board_input):
        self.board_no = CreateBoard.board_no
        self.board = {
            "B": [],
            "I": [],
            "N": [],
            "G": [],
            "O": []
        }
        CreateBoard.board_no += 1
        for index, letter in enumerate(["B","I","N","G","O"]):
            for element in range(index, len(board_input), 5):
                self.board[letter].append(board_input[element])

    def update_board(self, number: int):
        for key in self.board.keys():
            for index, value in enumerate(self.board[key]):
                if value == number:
                    # print(value)
                    self.board[key].pop(index)
                    self.board[key].insert(index, "x")

                    if self.check_for_winning_column(key) or self.check_for_winning_row(index):
                        self.calculate_winner(number)
                        # print(f"winner: {self.board}")
                        return True

    def check_for_winning_column(self, key):
        if all(element == "x" for element in self.board[key]):
            return True

    def check_for_winning_row(self, index):
        for row in range(5):
            row_values = []
            for key in self.board.keys():
                row_values.append(self.board[key][row])
            if all(element == "x" for element in row_values):
                return True

    def calculate_winner(self, number):
        remaining_sum = 0
        for letter in ["B","I","N","G","O"]:
            for value in self.board[letter]:
                if not value == "x":
                    remaining_sum += value
        print(f"board number: {self.board_no} - remaining sum: {remaining_sum} * number: {number} = {remaining_sum*number}")


def main():
    bingo_board_input_array = []
    with open("day 4/boards.txt") as f:
        for line in f.readlines():
            if line == "\n":
                pass
            else:
                line = line.split()
                for element in line:
                    bingo_board_input_array.append(int(element))

    bingo_boards = []
    for board in range(len(bingo_board_input_array)//25):
        bingo_array = []
        for element in range(25):
            bingo_array.append(bingo_board_input_array.pop(0))

        bingo_boards.append(CreateBoard(bingo_array))
    # print(bingo_boards)

    number_draw = []
    with open("day 4/numbers.txt") as f:
        for line in f.readlines():
            if line == "\n":
                pass
            else:
                line = line.split(",")
                for element in line:
                    number_draw.append(int(element))
    # print(number_draw)

    for _, number in enumerate(number_draw):
        for index, bingo_board in enumerate(bingo_boards):
            winner = bingo_board.update_board(number)
            if winner:
                bingo_boards.pop(index)
                if len(bingo_boards) == 1:

                    exit()


        # input = [68, 73, 98, 51, 49, 82, 56, 87, 64, 8, 46, 7, 21, 38, 30, 66, 5, 86, 97, 74, 60, 63, 76, 55, 39]


if __name__ == "__main__":
    main()