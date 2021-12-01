#Love Calculator

boy = input("Enter boy name ").lower()
girl = input("Enter girl name ").lower()

first_num = boy.count("t") + boy.count("r") + boy.count("u") + boy.count("e") + girl.count("t") + girl.count("r") + girl.count("u") + girl.count("e")
second_num = boy.count("l") + boy.count("o") + boy.count("v") + boy.count("e") + girl.count("l") + girl.count("o") + girl.count("v") + girl.count("e")

love_percentage = int(str(first_num) + str(second_num))

print(love_percentage)

if love_percentage < 10 or love_percentage > 90:
    print("CONGRATS!!!!!!!! You are meant to be with each other. ")
elif 40 < love_percentage < 50:
    print("Kuch huna sakcha . TRY GARDAI GARA LA !")
else:
    print("Lyyyyaaaaaaaaaaaaaaaaaaaaaaaa.......")

