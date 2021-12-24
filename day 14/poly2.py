from collections import defaultdict


def main():
    insertion_rules = {}
    element_pairs = defaultdict(int)
    element_count = defaultdict(int)

    with open("input.txt") as file:
        raw_input = file.readlines()

    polymer = [char for char in raw_input[0].strip()]

    for line in raw_input:
        if " -> " in line:
            rule_pair, element = line.strip().split(" -> ")
            insertion_rules[rule_pair] = element

    for index, element in enumerate(polymer):
        if index < len(polymer) - 1:
            pair = element + polymer[index+1]
            element_pairs[pair] += 1
            element_count[polymer[index]] += 1
        else:
            element_count[polymer[index]] += 1

    for step in range(40):
        new_pairs = defaultdict(int)
        for pair in element_pairs:
            new_element = insertion_rules[pair]
            first_new_pair = pair[0] + new_element
            second_new_pair = new_element + pair[1]
            new_pairs[first_new_pair] += element_pairs[pair]
            new_pairs[second_new_pair] += element_pairs[pair]
            element_count[new_element] += element_pairs[pair]
        element_pairs = new_pairs

    print(element_count)

    print(max(element_count.values()) - min(element_count.values()))


if __name__ == "__main__":
    main()