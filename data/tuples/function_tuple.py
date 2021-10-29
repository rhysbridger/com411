def likelyhood():
    likelyhoods = [50, 38, 27, 99, 4]
    return min(likelyhoods), max(likelyhoods)

def run():
    probabilities = likelyhood()
    print(f"Minimum likelihood of falling: {probabilities[0]}%")
    print(f"Maximum likelihood of falling: {probabilities[1]}%")

if __name__ == "__main__":
  run()