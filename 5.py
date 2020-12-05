import pdb

class Skiier:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.trees_encountered = 0
        self.course_complete = False
    
    def ski(self, ski_map: list) -> None:
        self.x = (self.x + 3) % (len(ski_map[0]))
        self.y += 1
        
        if self.y >= len(ski_map) - 1:
            self.course_complete = True
            return None
        else:
            if ski_map[self.y][self.x] == '#':
                self.trees_encountered += 1
        print(f"({self.x},{self.y}): {ski_map[self.y][self.x]}")

with open("5_input.txt") as input_file:
    
    map_array = input_file.read().strip().split('\n')

    ski_dude = Skiier()

    while not ski_dude.course_complete:
        ski_dude.ski(map_array)
    
    print(ski_dude.trees_encountered)
