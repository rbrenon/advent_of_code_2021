class LanternFish:
    number = 0

    def __init__(self, number):
        LanternFish.number += 1
        self.name = f"laternfish {self.number}"
        self.spawn_timer = number

    def __repr__(self):
        return self.name

    def model_one_day(self):
        self.spawn_timer -= 1
        if self.spawn_timer < 0:
            self.spawn_timer = 6
            new_fish = LanternFish(9)
            return new_fish


def main():
    with open("lanternfish.txt") as f:
        raw_list = f.readlines()

    raw_list = raw_list[0].split(",")
    fish_list = [int(element) for element in raw_list]

    fish_list = [3, 4, 3, 1, 2]
    lantern_fish_list = []

    for fish in fish_list:
        lantern_fish = LanternFish(fish)
        lantern_fish_list.append(lantern_fish)

    # print(lantern_fish_list)
    # print(len(lantern_fish_list))

    for day in range(25):
        print(f"now processing day {day}. current count = {LanternFish.number}.")
        for latern_fish in lantern_fish_list:
            new_lantern_fish = latern_fish.model_one_day()
            if new_lantern_fish is not None:
                lantern_fish_list.append(new_lantern_fish)

    print(LanternFish.number)


if __name__ == "__main__":
    main()
