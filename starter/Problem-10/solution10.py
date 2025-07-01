data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
cleaned_list = []

for data in data_list:
    if type(data) == type(1) or type(data) == type(1.1):
        cleaned_list.append(data)


print(cleaned_list)