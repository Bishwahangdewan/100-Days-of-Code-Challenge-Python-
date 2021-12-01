# program to calculate BMI calculator
# Formula for bmi calculator bmi = weight/(height)*(height)

height = float(input("Enter your height in m "))
weight = float(input("Enter your weight in kg "))

bmi = round(weight/(height**2), 2)

if bmi < 18.5:
    print("Your BMI is " + str(bmi) + ".You are underweight")
elif bmi < 25:
    print("Your BMI is " + str(bmi) + ".You are Normal Weight")
elif bmi < 30:
    print("Your BMI is " + str(bmi) + ".You are overweight")
elif bmi < 35:
    print("Your BMI is " + str(bmi) + ".You are obese")
else:
    print("Your BMI is " + str(bmi) + ".You are clinically obese")
