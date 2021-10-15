print("Program has started!")

code = int(input("please enter an ascii code(between 32 and 126)"))
print(code)
if code >= 32 or code <=126:
    print(f"the character represented by the ascii code {code} is {chr(code)}")
    if code <32 or code >126:
        print("this numbers are not in this ascii's range")
print("This program has ended")