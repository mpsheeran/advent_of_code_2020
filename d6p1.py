
if __name__ == "__main__":
    with open("d6input.txt") as input_file:
        groups = input_file.read().strip().split('\n\n')
        group_sets = [set(group) - {'\n'} for group in groups]
        lengths = [len(group_set) for group_set in group_sets]
        print(sum(lengths))
