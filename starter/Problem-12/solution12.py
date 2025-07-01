list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

freq_item = {}
for item in list1:
    if item in freq_item:
        freq_item[item] += 1
    else:
        freq_item[item] = 1

sum_common = 0
common_items = []
for item in list2:
    if item in freq_item:
        common_items.append(item)
        sum_common += item


print(f"The common items are: {common_items}")
print(f"The sum of common items is: {sum_common}")
