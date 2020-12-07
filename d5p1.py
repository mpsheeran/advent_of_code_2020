import pdb
from math import floor, ceil
from functools import reduce

# input: string of form FBFBBFFRLR
# where F means "front", B means "back", L means "left", and R means "right"
def convert_bsp_string_to_seat(bsp_string: str) -> tuple:
    
    row_bsp_string = bsp_string[0:7]
    col_bsp_string = bsp_string[7:10]
    print(f"{row_bsp_string},{col_bsp_string}")

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
    print(f"{bsp_string} : {minimum},{maximum}")
    
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
    def __init__(self, bsp_string: str):
        self.seat_tuple = convert_bsp_string_to_seat(
            bsp_string=bsp_string
            )
        self.seat_id = convert_seat_to_seat_id(
            seat=self.seat_tuple
        )
        print(self)
    def __repr__(self):
        return f"{self.seat_id}: {self.seat_tuple}"


if __name__ == "__main__":
    with open("d5input.txt") as input_file:
        seat_string_list = input_file.read().strip().split('\n')
    
    boarding_passes = [
        BoardingPass( bsp_string=seat_string )
        for seat_string
        in seat_string_list
    ]

    print( max(
        [
            boarding_pass.seat_id
            for boarding_pass
            in boarding_passes
        ]
    ))
    # pdb.set_trace()
