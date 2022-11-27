import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:
        input_list = f.read().split(new_line)
    list_headers = input_list[0].split(delimiter)
    list_rows = [input_str.split(delimiter) for input_str in input_list[1:]]
    return [{list_headers[i]: list_dict[i] for i in range(len(list_headers))} for list_dict in list_rows]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
