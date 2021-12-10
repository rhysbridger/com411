class Human:

  MAX_ENERGY = 100

  def __init__(self):

    self.name = "Human"
    self.energy = Human.MAX_ENERGY
    self.age = 0
    Human.eat += 1
    Human.move -= 1

  def MAX_ENERGY(self):
    print(Human.MAX_ENERGY)

  def display(self):
    print(f"I am {self.name}")

  def MAX_ENERGY(self):
      print(Human.MAX_ENERGY)

  def __repr__(self):
    return f'human(name={self.name}, age={self.age})'

if (__name__ == "__main__"):
  human = Human()
  human.display()

