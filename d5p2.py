import pdb
from math import floor, ceil
from functools import reduce

# input: string of form FBFBBFFRLR
# where F means "front", B means "back", L means "left", and R means "right"
def convert_bsp_string_to_seat(bsp_string: str) -> tuple:
    
    row_bsp_string = bsp_string[0:7]
    col_bsp_string = bsp_string[7:10]
    # print(f"{row_bsp_string},{col_bsp_string}")

    row = recurse_bsp_string(
        bsp_string=row_bsp_string,
        minimum=0,
        maximum=127
    )

    col = recurse_bsp_string(
        bsp_string=col_bsp_string,
        minimum=0,
        maximum=7
    )

    return (row, col)


def recurse_bsp_string(bsp_string:str, minimum:int, maximum:int) -> int:
    # print(f"{bsp_string} : {minimum},{maximum}")
    
    is_top = bsp_string[0] in ['B', 'R']
    
    #guard condition
    if len(bsp_string) == 1:
        return maximum if is_top else minimum

    else:
        return recurse_bsp_string(
            bsp_string=bsp_string[1:],
            minimum=minimum if not is_top else ceil((maximum + minimum) / 2),
            maximum=maximum if is_top else floor((maximum + minimum) / 2)
            # THIS PART GAVE ME HELL. CEILING? FLOOR? WHO KNOWS
        )

# multiply the row by 8, then add the column. 
def convert_seat_to_seat_id(seat: tuple) -> int:
    return seat[0] * 8 + seat[1]


class BoardingPass():
    def __init__(self, bsp_string: str=None, row: int=None, col: int=None):
        if row is not None and col is not None:
            self.row, self.col = (row, col)
            
        elif bsp_string:
            self.row, self.col = convert_bsp_string_to_seat(
                bsp_string=bsp_string
                )
        else:
            self.row, self.col = (None, None)
        
        self.seat_id = convert_seat_to_seat_id(
            seat=(self.row, self.col)
        )
        
        
    # def __init__(self, ):
    #     self.row = row
    #     self.col = col
    #     self.seat_id = convert_seat_to_seat_id(
    #         seat=(self.row, self.col)
    #     )
    #     return

    def __repr__(self):
        return f"{self.seat_id}: {self.col},{self.row}"
    def __lt__(self, other):
        return (self.col < other.col) or ((self.col == other.col) and self.row < other.row)
    def __gt__(self, other):
        return (self.col > other.col) or ((self.col == other.col) and self.row > other.row)
    def __eq__(self, other):
        return (self.col == other.col) and (self.row == other.row)
    def __le__(self, other):
        return (self == other) or (self < other)
    def __ge__(self, other):
        return (self == other) or (self > other)
    def __ne__(self, other):
        return not (self == other)

if __name__ == "__main__":
    with open("d5input.txt") as input_file:
        seat_string_list = input_file.read().strip().split('\n')
    
    boarding_passes = sorted([
        BoardingPass( bsp_string=seat_string )
        for seat_string
        in seat_string_list
    ])

    
    for index, curr_pass in enumerate(boarding_passes):
        if index > 0:
            previous_pass = boarding_passes[index - 1]
            if index + 1 < len(boarding_passes):
                next_pass = boarding_passes[index + 1]
                if (previous_pass.row + 1 < curr_pass.row):
                    my_seat = BoardingPass(
                        row = curr_pass.row - 1,
                        col = curr_pass.col
                    )
                
    print(my_seat)
