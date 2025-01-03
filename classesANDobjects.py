# Think like when you want to build a lot of houses with different colors
# for this we would need a lot of functions 
# instead we used classes to make it organized
# Do not forget classes start with uppercase letter to distinguish them from functions

# always call init function to initilaize the class
class Dog:
    def _init_(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' syas Bark!')

my_dog = Dog('Rover')
another_dog = Dog('Fluggy')

my_dog.speak()