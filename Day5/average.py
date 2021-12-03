# take list od heights as input from the user and print the avg

student_height = input("Enter the height of students ")
heights = student_height.split()

total_height = 0
total_students = 0

for height in heights:
    total_height += int(height)
    total_students += 1

average = round(total_height / total_students)

print(average)
