
print("program has started")
character=str(input("Please enter a standard character"))
print(character)
if len(character) == 1:
    number = ord(character)
    print(f"the ascii code for {character} is {number}!")
print ("program ended")