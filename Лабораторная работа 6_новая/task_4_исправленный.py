import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:
        input_list = f.read().split(new_line)
    list_headers = input_list[0].split(delimiter)
    list_rows = [input_str.split(delimiter) for input_str in input_list[1:]]
    list_output = []
    for list_dict in list_rows:
        dict_output = {}
        for i in range(len(list_headers)):
            dict_output[list_headers[i]] = list_dict[i]
        list_output.append(dict_output)
    return list_output


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
