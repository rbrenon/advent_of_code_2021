# In addition to horizontal position and depth, you'll also need to track a third value, aim,
# which also starts at 0. The commands also mean something entirely different than you first thought:
#
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.

def main():
    horizontal = 0
    vertical = 0
    aim = 0

    with open("day 2-input.txt") as f:
        for line in f.readlines():
            direction, value = line.strip().split(' ')
            value = int(value)
            if direction == "forward":
                horizontal += value
                vertical += aim * value
            elif direction == "down":
                aim += value
            elif direction == "up":
                aim -= value

    print(horizontal, vertical)
    print(horizontal * vertical)


if __name__ == "__main__":
    main()