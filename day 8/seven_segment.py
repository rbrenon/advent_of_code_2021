#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# 1 is the only digit that uses two segments
# 4 is the only digit that uses four segments
# 7 is the only digit that uses three segments
# 8 is the only digit that uses seven segments

# In the output values, how many times do digits 1, 4, 7, or 8 appear?


def main():
    with open("input.txt") as f:
        raw_input = f.readlines()

        ones, fours, sevens, eights = 0, 0, 0, 0

    for row in raw_input:
        digits = row.split("|")[-1].strip()
        segments = digits.split()
        for segment in segments:
            distinct_chars = set(segment)
            no_dist_chars = len(distinct_chars)
            print(segment, no_dist_chars)
            if no_dist_chars == 2:
                ones += 1
            elif no_dist_chars == 4:
                fours += 1
            elif no_dist_chars == 3:
                sevens += 1
            elif no_dist_chars == 7:
                eights += 1
            else:
                print("unknown segment")

    print(
        f"ones: {ones}, "
        f"fours: {fours}, "
        f"sevens: {sevens}, "
        f"eights: {eights},"
        f"sum of known chars: {ones + fours + sevens + eights}"
    )


if __name__ == "__main__":
    main()
