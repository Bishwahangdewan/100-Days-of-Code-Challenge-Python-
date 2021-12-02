# Treasure Map

row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

map = [row1,row2,row3]

print("The Treasure Map ")
print(f"{row1} \n{row2} \n{row3}")

pos = input("Where do you want to put the treasure? ")

pos_arr = list(pos)

map[int(pos_arr[0])-1][int(pos_arr[1])-1] = 'X'

print("Your Treasure Map ")
print(f"{row1} \n{row2} \n{row3}")

