#program to take age as an input and show how many days weeks and years left before end

age = int(input("What is your age? "))

age_left = 90 - age

days_left = 365 * age_left
months_left = 12 * age_left
weeks_left = 52 * age_left

print(f"You have {days_left} days left , {months_left} months left and {weeks_left} weeks left before you die")
