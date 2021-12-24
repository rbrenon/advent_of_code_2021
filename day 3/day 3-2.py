# Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:
#
# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
#
# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
# and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
# If 0 and 1 are equally common, keep values with a 0 in the position being considered.

# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
#
# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
#
# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
#
# So, the gamma rate is the binary number 10110, or 22 in decimal.
#
# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
# So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.


def common_bit(array: list, position: int, determine_equal: int) -> dict:
    ones, zeros = 0, 0
    for index, bit in enumerate(array):
        if bit[position] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        return dict(most=1, least=0)
    elif zeros > ones:
        return dict(most=0, least=1)
    else:
        return dict(most=1, least=0)


def reduce_array_elements(array: list, position: int, bit: int) -> list:
    new_array = []
    for element in array:
        if element[position] == str(bit):
            new_array.append(element)
    return new_array


def main():
    o2_list = [element.strip() for element in full_list]
    for bit_position in range(len(full_list[0])):
        common = common_bit(o2_list, bit_position, 1)
        print(common)
        o2_list = reduce_array_elements(o2_list, bit_position, common['most'])
        # print(o2_list)
        if len(o2_list) == 1:
            oxygen_generator = o2_list[0]
            o2 = int(oxygen_generator,2)
            break

    co2_list = [element.strip() for element in full_list]
    for bit_position in range(len(full_list[0])):
        common = common_bit(co2_list, bit_position, 0)
        print(common)
        co2_list = reduce_array_elements(co2_list, bit_position, common['least'])
        # print(co2_list)
        if len(co2_list) == 1:
            co2 = co2_list[0]
            co2 = int(co2,2)
            break

    print(f"co2: {co2} * o2: {o2} = {co2 * o2}")

if __name__ == "__main__":
    with open("input.txt") as f:
        full_list = f.readlines()
    main()