# GRADING PROGRAM

student_scores = {
    "harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grade = {}

for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grade[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grade[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] < 80:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fair"

print(student_grade)