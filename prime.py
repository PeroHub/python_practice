import random

x = random.randrange(1, 30)
print(x)


player = 0
count = 7
while x != player:
    player = int(input("Make a guess: "))
    count = count + 1
    player = player + 1

    if player > count:
        print("You loose")



    elif player > x:
        print("Calm down BUDDY, you guess is TOO high")
        print("")

    elif player < x:
        print("Step up MAN, you guess is too LOW")
        print("")

    else:
        print("You got it man....One bottle for YOU!!")  
        print("") 




