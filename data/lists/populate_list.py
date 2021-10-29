def directions():
    directions = ["move forward", "move backwards", "turn left", "turn right"]
    return directions

def menu():
    print("please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{[index]}: {dirs[index]}.")
    index = int(input())
    return dirs[index]

def run():
    route = []
    print("working out escape route")
    for count in range(5):
        route.append(menu())
    print(f"Escape route {route}")



if __name__ == "__main__":
    run()

