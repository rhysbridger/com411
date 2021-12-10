class Robot:

  # A class attribute
  MAX_ENERGY = 10

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old.'

  # An initialiser (special instance method)
  def __init__(self, name = "Robot"):

    # An instance attribute
    self.name = name
    self.age = 0
    self.energy = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old.'

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()


