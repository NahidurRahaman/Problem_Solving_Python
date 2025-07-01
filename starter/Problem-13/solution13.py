dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

for k in dict1:
    if k in dict2:
        print(f"Key: {k}, Value from dict1: {dict1[k]}, Value from dict2: {dict2[k]}")
    else:
        print(f"Key: {k}, Value from dict1: {dict1[k]}, Value from dict2: Not found!!!")
