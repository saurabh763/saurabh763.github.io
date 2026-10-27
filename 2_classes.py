
# Constructor with Arguments

class Dog:
    species = "GS"

    def __init__(self, age=2):
        self.age = age

    def eat(self):
        print("hungry right now.")

    def bark(self):
        print(self.age)
        print("says woof!")

a = Dog()
a.bark()










# class Dog:
#     species = "GS"

#     def __init__(self, name="tom", age=2):
#         self.dog_name = name
#         self.age = age
#         self.is_hungry = True

#     def bark(self):
#         print(f"{self.dog_name} says woof!")

#     def eat(self):
#         if self.is_hungry:
#             print(f"{self.dog_name} is eating...")
#             self.is_hungry = False
#         else:
#             print(f"{self.dog_name} is not hungry right now.")
#             self.is_hungry = True


# my_dog = Dog()
# print(f"My dog's name is {my_dog.dog_name} and he is {my_dog.age} years old.")

# my_dog.bark()
# my_dog.eat()
# my_dog.eat()
# my_dog.eat()




# class Dog:
#     def __init__(self, name="tom", age=2):
#         self.dog_name = name
#         self.age = age
#         self.is_hungry = True

#     def bark(self):
#         print(f"{self.dog_name} says woof!")

#     def eat(self):
#         if self.is_hungry:
#             print(f"{self.dog_name} is eating...")
#             self.is_hungry = False
#         else:
#             print(f"{self.dog_name} is not hungry right now.")
#             self.is_hungry = True


# a = Dog()
# a.bark()

# your_dog = Dog("tuffy", 3)
# your_dog.bark()
# your_dog.eat()
# your_dog.eat()
# a.eat()


