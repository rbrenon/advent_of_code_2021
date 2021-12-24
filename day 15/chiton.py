

def main():
    with open("testinput.txt") as file:
        raw_input = file.read().splitlines()

    chitons = {index: [int(element) for element in row] for index, row in enumerate(raw_input)}
    # print(chitons)

    index = 0
    risk_level = chitons[0][index]
    next_move = None
    for key in chitons.keys():
        next_key = key
        while next_key == key:
            next_key, index, risk_value = find_lowest_risk_move(chitons, key, index)
            risk_level += risk_value
            print(f"chitons[{key}][{index}] = {chitons[key][index]}. Risk: {risk_value}, Total Risk: {risk_level}")
    print(chitons)

def find_lowest_risk_move(chitons: dict, key: int, index: int):
    # check below unless at bottom
    down = chitons[key+1][index] if key < len(chitons)-1 else 10
    # check left unless at 0 element
    left = chitons[key][index-1] if index > 0 else 10
    # check right unless at end of array
    right = chitons[key][index+1] if index < len(chitons[key])-1 else 10

    lowest_risk = min(left, right, down)
    if down == lowest_risk:
        chitons[key + 1][index] = 10
        key += 1
    elif left == lowest_risk:
        chitons[key][index - 1] = 10
        index -= 1
    elif right == lowest_risk:
        chitons[key][index + 1] = 10
        index += 1

    # print(min(left, right, down))
    # print(left, right, down)
    return key, index, lowest_risk


if __name__ == "__main__":
    main()