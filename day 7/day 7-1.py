from functools import lru_cache
import sys
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())


def main():
    with open("submarines.txt") as f:
        raw_list = f.readlines()

    raw_list = raw_list[0].split(",")
    crab_subs = [int(element) for element in raw_list]
    # print(crab_subs)

    rendez_vous_low = min(crab_subs)
    rendez_vous_high = max(crab_subs)
    print(f"Points: {rendez_vous_low} --> {rendez_vous_high}")

    lowest_fuel = rendez_vous_high ** len(crab_subs)
    print(f"starting point for lowest fuel: {lowest_fuel}")

    for point in range(rendez_vous_low, rendez_vous_high):
        fuel = 0
        for sub in crab_subs:
            fuel += sum_to_zero(abs(sub - point))
        if fuel < lowest_fuel:
            lowest_fuel = fuel
        print(f"Fuel: {fuel}, Lowest Fuel: {lowest_fuel}")
    print(f"Overall Lowest Fuel Required: {lowest_fuel}")


@lru_cache(maxsize=None)
def sum_to_zero(number):
    if number <= 1:
        return number
    else:
        return number + sum_to_zero(number - 1)


if __name__ == "__main__":
    main()