from timeit import default_timer as timer

def main():
    with open("lanternfish.txt") as f:
        raw_fish = [int(element) for element in f.read().strip().split(",")]

    lanternfish = [raw_fish.count(age) for age in range(9)]

    for day in range(256):
        lanternfish.append(lanternfish.pop(0))
        lanternfish[6] += lanternfish[8]

    print(f"{sum(lanternfish)}")


if __name__ == "__main__":
    start = timer()
    main()
    end = timer()

    print(1632779838045)
    print(f"time: {end - start}")