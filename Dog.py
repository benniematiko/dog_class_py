class Dog:
  def __init__(self, name,age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age

  def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")


  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")


  def bark(self):
    return "barks"

class SledDog(Dog): # Inherits from Dog
    def __init__(self, name, age, pull_strength):
        """Initialize attributes of the parent class, then add specific ones."""
        super().__init__(name, age)
        self.pull_strength = pull_strength

    def pull_sled(self):
        """A unique behavior only for SledDogs."""
        print(f"{self.name} is pulling the sled with {self.pull_strength}kg of force!")

    # You can also 'override' a parent method
    def bark(self):
        print(f"{self.name} gives an icy, majestic howl!")


# Create a SledDog instance
my_husky = SledDog('Balto', 6, 50)

# 1. Accessing inherited methods (from Dog)
my_husky.sit() 

# 2. Accessing specialized methods (from SledDog)
my_husky.pull_sled()

# 3. Accessing the overridden method
my_husky.bark()