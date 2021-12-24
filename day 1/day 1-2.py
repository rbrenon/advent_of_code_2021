

if __name__ == "__main__":
    measurements = []
    with open("day 1/day 1-input.txt") as f:
        for line in f.readlines():
            measurement = int(line.strip())
            measurements.append(measurement)

    begin_num = 0
    end_num = 3

    base_sum = sum(measurements[begin_num:end_num])

    count = 0

    for numb in measurements:
        begin_num += 1
        end_num += 1
        new_sum = sum(measurements[begin_num:end_num])
        if new_sum > base_sum:
            count += 1
        base_sum = new_sum
    print(count)