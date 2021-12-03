# take marks from input and print the highest

student_marks = input("Enter the marks of the students ")
marks = student_marks.split()

highest = 0

for mark in marks:
    if int(mark) > highest:
        highest = int(mark)

print(f"Highest mark is {highest}")
