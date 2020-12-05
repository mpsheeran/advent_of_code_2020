import pdb
from re import split as re_split

class Passport:
    def __init__(self, raw_text: str=""):
        self.field_list = self.process_text(raw_text)
        self.field_dict = {
            field.split(':')[0]:field.split(':')[1] ##TODO: split only once. this sucks.
            for field
            in self.field_list
        }
        self.validity = self.are_fields_valid() & self.is_field_data_valid()
    
    def are_fields_valid(self) -> bool:
        required_fields = {"byr", "iyr", "eyr", "hgt","hcl" ,"ecl" ,"pid",}
        fields_possessed = set((self.field_dict.keys()))
        return fields_possessed.issuperset(required_fields)

    def is_field_data_valid(self) -> bool:
        return False

    def process_text(self, raw_text: str):
        return re_split('[\n ]', raw_text)

with open("d4p1_input.txt") as input_file_stream:
    passport_raw_text_list = input_file_stream.read().strip().split('\n\n')
    passports = [Passport(raw_text) for raw_text in passport_raw_text_list]
    print(len(list(filter(lambda x: x.validity, passports))))
