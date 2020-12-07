import pdb
import re
from functools import reduce

validation_regex_dict = {
    "byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
    "iyr": re.compile(r"^(201[0-9]|2020)$"),
    "eyr": re.compile(r"^(202[0-9]|2030)$"),
    "hgt": re.compile(r"^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$"),
    "hcl": re.compile(r"^#[0-9|a-f]{6}$"),
    "ecl": re.compile(r"(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)"),
    "pid": re.compile(r"^\d{9}$"),
    "cid": re.compile(r".*"),
}


class Passport:
    def __init__(self, raw_text: str="") -> None:
        self.field_list = self.process_text(raw_text)
        self.field_dict = {
            field.split(':')[0]:field.split(':')[1] ##TODO: split only once. this sucks.
            for field
            in self.field_list
        }
        self.validity = self.are_fields_valid() & self.is_data_valid()
    
    def are_fields_valid(self) -> bool:
        required_fields = {"byr", "iyr", "eyr", "hgt","hcl" ,"ecl" ,"pid",}
        fields_possessed = set((self.field_dict.keys()))
        return fields_possessed.issuperset(required_fields)

    def is_data_valid(self) -> bool:
        return reduce(
            lambda x, y: x & y,
            [
                True if validation_regex_dict[ field[0] ].search( field[1] )
                else False
                for field
                in self.field_dict.items()
            ]
        )

    def process_text(self, raw_text: str):
        return re.split('[\n ]', raw_text)

with open("d4p1_input.txt") as input_file_stream:
    # assumptions: string of passport data delimited by two adjacent newlines
    passport_raw_text_list = input_file_stream.read().strip().split('\n\n')

    passports = [
        Passport(raw_text)
        for raw_text
        in passport_raw_text_list
    ]

    print(len(list(filter(lambda x: x.validity, passports))))
