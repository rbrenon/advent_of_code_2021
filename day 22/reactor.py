import re
import itertools
from collections import defaultdict


def main():
    with open("testinput.txt") as file:
        raw_input = file.read().splitlines()

    reactor_core = defaultdict()

    for line_no, line in enumerate(raw_input):
        line = re.split(" |,|\.\.|=", line)

        core_control = line[0]
        core_coords = (line[2:4], line[5:7], line[8:10])
        core_count = 0

        if (
                150 >= int(core_coords[0][0])
                and int(core_coords[0][1]) >= -150
                and 150 >= int(core_coords[1][0])
                and int(core_coords[1][1]) >= -150
                and 150 >= int(core_coords[2][0])
                and int(core_coords[2][1]) >= -150
        ):
            x_start = int(core_coords[0][0])
            x_end = int(core_coords[0][1]) + 1
            y_start = int(core_coords[1][0])
            y_end = int(core_coords[1][1]) + 1
            z_start = int(core_coords[2][0])
            z_end = int(core_coords[2][1]) + 1

            if core_control == "on":
                for x, y, z in itertools.product(
                        range(x_start, x_end), range(y_start, y_end), range(z_start, z_end)
                ):
                    xyz = str(x) + str(y) + str(z)
                    reactor_core[xyz] = 'on'
            elif core_control == "off":
                for x, y, z in itertools.product(
                        range(x_start, x_end), range(y_start, y_end), range(z_start, z_end)
                ):
                    xyz = str(x) + str(y) + str(z)
                    reactor_core[xyz] = 'off'
            else:
                print("not found")
        # pprint(f"{reactor_core} - total length = {len(reactor_core)}")

    print(
        f"total on = {sum(on=='on' for on in reactor_core.values())}, off = {sum(off=='off' for off in reactor_core.values())}"
    )


if __name__ == "__main__":
    main()

# 564253 too low
# 565681 too low
