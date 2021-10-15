# ask user what the book is like
print("What cover does this book have (soft/hard)?")
book = input()

# decide if the book is soft or hard
if book == "soft":

    # ask user is this book perfect-bound
    print("is this book perfect-bound (yes/no)?")
    bound = input()

    # decide if beep should play with toys or friend
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
else :
    print("no thank you!")