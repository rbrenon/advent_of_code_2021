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


def main():
    output = []
    with open("input.txt") as f:
        input = f.readlines()
    bits = len(input[0].strip())
    for bit in range(bits):
        zeros, ones = 0, 0
        for line in input:
            val = int(line[bit].strip())
            if val == 1:
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            output.append(1)
        else:
            output.append(0)
        # print(zeros, ones, output)
    output_string = "".join(str(el) for el in output)

    gamma = int(output_string, 2)
    print(gamma)

    epsilon_output =[]
    for bit in output:
        if bit == 1:
            epsilon_output.append(0)
        else:
            epsilon_output.append(1)

    print(output)
    print(epsilon_output)
    epsilon_string = "".join(str(el) for el in epsilon_output)
    epsilon = int(epsilon_string,2)
    print(epsilon)

    print(epsilon*gamma)



if __name__ == "__main__":
    main()