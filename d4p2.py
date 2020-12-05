import pdb
import re
from functools import reduce

validation_regex_dict = {
    "byr": re.compile(r"^\d{4}$"),
    "iyr": re.compile(r"^\d{4}$"),
    "eyr": re.compile(r"^\d{4}$"),
    "hgt": re.compile(r"^(\d{2,3})(cm|in)$"),
    "hcl": re.compile(r"^#[0-9|a-f]{6}$"),
    "ecl": re.compile(r"(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)"),
    "pid": re.compile(r"^\d{9}$"),
    "cid": re.compile(r".*"),
}

class Passport:
    def __init__(self, raw_text: str=""):
        self.field_list = self.process_text(raw_text)
        self.field_dict = {
            field.split(':')[0]:field.split(':')[1] ##TODO: split only once. this sucks.
            for field
            in self.field_list
        }
        self.validity = self.are_fields_valid() #& self.is_data_valid()
    
    def are_fields_valid(self) -> bool:
        required_fields = {"byr", "iyr", "eyr", "hgt","hcl" ,"ecl" ,"pid",}
        fields_possessed = set((self.field_dict.keys()))
        return fields_possessed.issuperset(required_fields)

    def is_data_valid(self) -> bool:
        for field in self.field_dict.items():
            print(f"{field}: {validation_regex_dict[field[0]].search(field[1])}")


        [validation_regex_dict[item[0]].search(item[1]) for item in self.field_dict.items()] ## PLACEHOLDER

        # are_patterns_correct = reduce(
        #     lambda x: validation_regex_dict[x,
        #     self.field_dict
        #     )
        pass

    def process_text(self, raw_text: str):
        return re.split('[\n ]', raw_text)

with open("d4p1_input.txt") as input_file_stream:
    passport_raw_text_list = input_file_stream.read().strip().split('\n\n')
    passports = [Passport(raw_text) for raw_text in passport_raw_text_list]
    pdb.set_trace()
    print(len(list(filter(lambda x: x.validity, passports))))
