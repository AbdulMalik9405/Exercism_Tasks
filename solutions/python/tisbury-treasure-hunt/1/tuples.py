"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    else:
        return False

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record) == True:
        return (azara_record + rui_record)
    else:
        return "not a match"

def clean_up(combined_record_group):
    ReportStr = ""
    for i in (combined_record_group):
        Report = (i[0],i[2],i[3],i[4])
        ReportStr += f"{Report}\n"
    return ReportStr