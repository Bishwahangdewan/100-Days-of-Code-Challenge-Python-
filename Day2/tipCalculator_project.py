#Tip calculator project

#take the bill as an input , also take how many people to split and the tip percentage
#to calculate what each has to pay = (bill/split) * %tip

bill = float(input("Enter your bill "))
split = float(input("How many people to split the bill? "))
tip = float(input("How much tip do you want to give? 10 , 12 or 15? "))

# first calculate % of total bill and add that as tip to the bill
# total bill is then split by no of people

tip_money = (tip/100) * bill
total_bill = bill + tip_money
pay = total_bill/split

print(f"You should pay ${round(pay,2)}")
