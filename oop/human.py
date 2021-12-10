class Human:

  MAX_ENERGY = 100

  def __init__(self):

    self.name = "Human"
    self.energy = Human.MAX_ENERGY
    self.age = 0

  def MAX_ENERGY(self):
    print(Human.MAX_ENERGY)

  def display(self):
    print(f"I am {self.name}")

  def MAX_ENERGY(self):
      print(Human.MAX_ENERGY)

if (__name__ == "__main__"):
  human = Human()
  human.display()

