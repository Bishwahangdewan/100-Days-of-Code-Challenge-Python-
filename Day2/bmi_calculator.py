# program to calculate BMI calculator
# Formula for bmi calculator bmi = weight/(height)*(height)

height = float(input("Enter your height in m "))
weight = float(input("Enter your weight in kg "))

bmi = int(weight/(height**2))

print("Your BMI is " + str(bmi))



