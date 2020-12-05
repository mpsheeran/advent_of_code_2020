import pdb
from functools import reduce

class Skiier:
    def __init__(self, x_slope=3, y_slope=1):
        self.x = 0
        self.y = 0
        self.x_slope = x_slope
        self.y_slope = y_slope
        
        self.trees_encountered = 0
        self.course_complete = False
    def __repr__(self):
        return str(self.trees_encountered)
    
    def ski(self, ski_map: list) -> None:
        self.x = (self.x + self.x_slope) % (len(ski_map[0]))
        self.y += self.y_slope
        
        if self.y >= len(ski_map) - 1:
            self.course_complete = True
            return None
        else:
            if ski_map[self.y][self.x] == '#':
                self.trees_encountered += 1
        # print(f"({self.x},{self.y}): {ski_map[self.y][self.x]}")

with open("5_input.txt") as input_file:
    
    map_array = input_file.read().strip().split('\n')

    skiiers = [
        Skiier(*slope)
        for slope
        in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ]

    for skiier in skiiers:
        while not skiier.course_complete:
            skiier.ski(map_array)
    
    answer = reduce(lambda x, y: x*y, [skiier.trees_encountered for skiier in skiiers])
    print(answer)
    
