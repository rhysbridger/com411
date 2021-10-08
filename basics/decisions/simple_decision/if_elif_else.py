direction=str(input("Towards which direction should I paint (up, down, left or right)?"))
print(direction)
print()
if direction == "up":
    print("i am painting in an upwards direction")
elif direction == "down":
    print("i am painting in an downwards direction")
elif direction == "left":
    print("i am painting to the left")
elif direction == "right":
    print("i am painting to the right")
else:
    print("i do not understand!")

