if __name__ == "__main__":
    with open("day 1/day 1-input.txt") as f:
        base_numb = int(f.readline().strip())
        count = 0
        for line in f.readlines():
            new_numb = int(line.strip())
            if new_numb > base_numb:
                count += 1
            base_numb = new_numb
    print(f"number of increases: {count}")