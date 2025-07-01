my_list = [4, 8, 7, 4, 3, 6, 2, 1, 9]

check = False
for num in my_list:
    if num == 6:
        print("Found 6!!!")
        check = True
        break


if (check == False):
    print("6 not found!!!")
