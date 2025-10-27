"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    return False

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record) == True:
        return (azara_record + rui_record)
    return "not a match"

def clean_up(combined_record_group):
    report_str = ""
    for i in (combined_record_group):
        report = (i[0],i[2],i[3],i[4])
        report_str += f"{report}\n"
    return report_str