# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

def main():
    horizontal = 0
    vertical = 0

    with open("day 2-input.txt") as f:
        for line in f.readlines():
            direction, value = line.strip().split(' ')
            value = int(value)
            if direction == "forward":
                horizontal += value
            elif direction == "down":
                vertical += value
            elif direction == "up":
                vertical -= value

    print(horizontal, vertical)
    print(horizontal * vertical)


if __name__ == "__main__":
    main()