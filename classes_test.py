# class Lamp:
#   def __init__(self, model: str, color: str):
#     self.model = model
#     self.color = color

#   def turn_on(self):
#     print(f"{self.model} is turned on")
  
#   def turn_off(self):
#     print(f"{self.model} is turned off")

#   def discription(self):
#     print(f"Lamp {self.model} ({self.color})")


# red_lamp = Lamp("ABC123", "Red")
# red_lamp.turn_on()
# red_lamp.turn_off()
# red_lamp.discription()

# red_lamp.color = "Blue & Violet"
# print(id(red_lamp.discription()))

# blue_lamp = Lamp("DEF456", "Blue")
# blue_lamp.turn_on()
# blue_lamp.turn_off()
# print(id(blue_lamp.discription()))

#############################################################

# class Fruit:
#   def __init__(self, name):
#     self._name = name

#   @property
#   def name(self):
#     print("The fruit name: ", self._name)
#     return self._name

#   @name.setter
#   def name(self, value):
#     print(f"{self._name} is now the {value}")
#     self._name = value

# furit_name = Fruit("Apple")
# furit_name.name

# furit_name.name = "Orange"


#############################################################

# class Car:
#   def __init__(self, name, model, color):
#     self.name = name
#     self.model = model
#     self.color = color

#   def __repr__(self):
#     return f"{self.name}, {self.model}, {self.color}"

#   def __eq__(self, other):
#     return self.__dict__ == other.__dict__

# if __name__ == "__main__":
#     car1 = Car("Ford", "Galaxy", "Blue")
#     car2 = Car("Ford", "Galaxy", "Red")
#     print(car1)
#     print(car2)

#     print(car1 == car2)


#############################################################

# class Animal:
#   def __init__(self, name):
#     self.name = name

#   def eat(self):
#     print(f"{self.name} is eating")

#   def sleeping(self):
#     print(f"{self.name} is sleeping")

# class Cat(Animal):
#   def __init__(self, name, weight):
#     super().__init__(name)
#     self.weight = weight

#   def meow(self):
#     print(f"{self.name} is meowing")


# animal1 = Animal("Cat")
# animal1.eat()

#############################################################

