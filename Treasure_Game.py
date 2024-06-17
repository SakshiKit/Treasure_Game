print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

q1 = (input("You're at a cross road. Where do you want to go? Type left or right"))
print(q1)
if q1 == "left":
    q2 =(input('You came to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.'))
    if q2 == "wait":
        q3=(input("you arrive at the island unharmed.there is a house with three doors.one red one yellow and one blue. which colour do you chose?"))
        if q3 == "yellow":
            print("You found the treasure you win")
        elif q3 == "red":
            print("its a room full of fire. game over")
        elif q3 == " blue":
            print("its a room of beasts. game over")
        else:
            print("you choose a door that doesnt exit")
    else:
        print("you get attacked by an angry trout. game over")
else:
    print("you fell into a hole. game over")


