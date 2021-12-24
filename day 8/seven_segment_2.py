'''
 0:(6)x    *1:    2:(5)   3:(5)x    *4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

 5:(5)   6:(6)x   *7:     *8:    9:(6)x
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''

from collections import defaultdict
from pprint import pprint


def main():
    with open("input.txt") as f:
        raw_input = f.readlines()

    display = defaultdict(dict)

    for index, row in enumerate(raw_input):
        digits = row.split("|")
        display[index]["signals"] = digits[0].split()
        display[index]["segments"] = digits[-1].split()
        display[index]["decoded"] = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], }

    #     row_sum = []
    for index, _ in enumerate(display.keys()):
        for val_index, element in enumerate(display[index]["signals"]):
            if len(display[index]["signals"][val_index]) == 2:
                display[index]["decoded"][1] = display[index]["signals"][val_index]
            elif len(display[index]["signals"][val_index]) == 4:
                display[index]["decoded"][4] = display[index]["signals"][val_index]
            elif len(display[index]["signals"][val_index]) == 3:
                display[index]["decoded"][7] = display[index]["signals"][val_index]
            elif len(display[index]["signals"][val_index]) == 7:
                display[index]["decoded"][8] = display[index]["signals"][val_index]

    answers = []

    for index, _ in enumerate(display.keys()):
        answer = ''
        for seg_index, element in enumerate(display[index]["segments"]):
            if len(element) == 2:
                answer += '1'
            elif len(element) == 4:
                answer += '4'
            elif len(element) == 3:
                answer += '7'
            elif len(element) == 7:
                answer += '8'
            elif len(element) == 5:
                if all(char in element for char in display[index]["decoded"][1]):
                    display[index]["decoded"][3] = element
                    answer += '3'
                else:
                    decode = [char for char in display[index]["decoded"][4]]
                    remove_from_decode = [el for el in display[index]["decoded"][1]]
                    for rm_char in remove_from_decode:
                        try:
                            decode.remove(rm_char)
                        except:
                            pass
                    if all(char in element for char in decode):
                        display[index]["decoded"][5] = element
                        answer += '5'
                    else:
                        display[index]["decoded"][2] = element
                        answer += '2'
            elif len(display[index]["segments"][seg_index]) == 6:
                if all(char in element for char in display[index]["decoded"][4]):
                    display[index]["decoded"][9] = element
                    answer += '9'
                elif all(char in element for char in display[index]["decoded"][1]):
                    display[index]["decoded"][0] = element
                    answer += '0'
                else:
                    display[index]["decoded"][6] = element
                    answer += '6'
        answers.append(answer)

    print(answers)

    final_answer = 0
    for answer in answers:
        final_answer += int(answer)

    print(final_answer)


if __name__ == "__main__":
    main()

# 9361 v 9391, 1625 v 1955


# 142153 too low
# 1226057 too high
# 940724
