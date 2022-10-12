list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

p = 0
for i in range(1, len(list_numbers)):
    if list_numbers[i] > list_numbers[p]:
        p = i
    else:
        continue
list_numbers[p], list_numbers[-1] = [list_numbers[-1], list_numbers[p]]

print(list_numbers)
