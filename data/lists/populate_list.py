def directions():
    directions = ["move forward", "move backwards", "turn left", "turn right"]
    return directions

def menu():
    response = int(input("please select a direction:"))
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{[index]}: {dirs[index]}.")
        print(response)

def run():
   menu()


if __name__ == "__main__":
    run()

