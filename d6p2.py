import pdb 
from functools import reduce

if __name__ == "__main__":
    with open("d6input.txt") as input_file:
        input_by_group = input_file.read().strip().split('\n\n')

        intersected_group_answer_sets = [
            reduce(
                lambda x,y: x.intersection(y),
                [ set(entry) for entry in group_input.split('\n') ]
            )
            for group_input
            in input_by_group 
        ]

        lengths = [len(group_set) for group_set in intersected_group_answer_sets]

        print(sum(lengths))
