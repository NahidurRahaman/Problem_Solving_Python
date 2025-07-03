student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

check = False
total_1, total_2 = 0, 0
for score in student_1:
    total_1 += score

    if (score < 40):
        print("Student 1 FAILED")
        check = True
        break

if (check == False):
    print("Average of Student 1 is: ", total_1 / len(student_1))


check = False
for score in student_2:
    total_2 += score

    if (score < 40):
        print("Student 2 FAILED")
        check = True
        break

if (check == False):
    print("Average of Student 2 is: ", total_2 / len(student_2))