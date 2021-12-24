from collections import Counter

def main():
    with open("input.txt") as file:
        raw_input = file.readlines()

    polymer = [char for char in raw_input[0].strip()]
    # print(polymer)

    insertion_rules = []
    for line in raw_input:
        if " -> " in line:
            line = line.split("->")
            rule_pair = line[0].strip()
            insert = line[1].strip()
            insertion_rules.append((rule_pair, insert))
    # print(insertion_rules)
    print(polymer)

    for step in range(10):
        polymer_inserts = []
        for rule in insertion_rules:
            first_char = rule[0][0]
            second_char = rule[0][1]
            for index, char in enumerate(polymer):
                if char == first_char and index < len(polymer) - 1:
                    if polymer[index + 1] == second_char:
                        polymer_inserts.append((index + 1, rule[1]))

        polymer_inserts = sorted(polymer_inserts)
        for index, insert_value in enumerate(polymer_inserts):
            polymer.insert(index + insert_value[0], insert_value[1])

        print(f"Step: {step}, Length: {len(polymer)}")


    # counts = {item: polymer.count(item) for item in polymer}
    # print(counts)
    # print(max(counts.values()) - min(counts.values()))

    counter = Counter(polymer)
    print(counter)
    print(max(counter.values())-min(counter.values()))


if __name__ == "__main__":
    main()
