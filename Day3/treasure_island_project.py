#Treasure Island Game Project

print("---WELCOME TO TREASURE ISLAND . YOUR MISSION IS TO FIND THE TREASURE ---")

print("As soon as you enter the island you see that there are two paths ahead of you.")
print("The one of the left is a muddy road  and one on the right is a cave ")
choice1 = input("Which one do you choose? Type 'left' to go left and 'right' to go right.")

if choice1 == 'left':
    print("You take the muddy road and arrive in front of a river bank.")
    choice2 = input("Do you want to cross the river('swim') or wait for some time('wait')? ")

    if choice2 == 'swim':
        print("As you start to cross the river the fast river streams push you towards the waterfall . You Die! ")
    else:
        print("You wait for some time . Soon a boat comes and you pass the river through that boat.")
        print("As you go ahead you find yourself in front of 3 doors")
        choice3 = input("Which door do you want to take?? Red Yellow or Blue? ")

        if choice3 == 'red':
            print("As soon as you open the door , you see the treasure guardian who fires a shot and kills you. You die")
        elif choice3 == 'blue':
            print("As soon as you open the door , you awaken the Dragon. The dragon from nowhere burns the entire island. You die")
        else:
            print("You find yourself in front of the treasure ! You Win")

else:
    print("You enter inside the cave only to be eaten by a lion. You Die! ")


print("-----GAME OVER----")