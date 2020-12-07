import pdb

# input: string of form FBFBBFFRLR
# where F means "front", B means "back", L means "left", and R means "right"
def convert_bsp_string_to_seat(bsp_string: str) -> tuple:
    # TODO
    return (None, None)

# multiply the row by 8, then add the column. 
def convert_seat_to_seat_id(seat: tuple) -> int:
    # TODO
    return 0


class BoardingPass():
    def __init__(self, bsp_string: str):
        self.seat_tuple = convert_bsp_string_to_seat(
            bsp_string=bsp_string
            )
        self.seat_id = convert_seat_to_seat_id(
            seat=self.seat_tuple
        )
    def __repr__(self):
        return str(self.seat_id)



if __name__ == "__main__":
    with open("d5input.txt") as input_file:
        seat_string_list = input_file.read().strip().split('\n')
    
    boarding_passes = [
        BoardingPass( bsp_string=seat_string )
        for seat_string
        in seat_string_list
    ]
    
    pdb.set_trace()
        
