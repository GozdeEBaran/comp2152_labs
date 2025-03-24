class Person:
    # constructor
    def _init_(self, p_name, p_age, p_height):
        print("Constructing the person object")
        # __ before name makes the property private
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I am Public"

    # getter for name: version 1
    @property
    def name(self):
        return self.__name
        
    # setter for name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def _del_(self):
        print("The garbage collector is automatically destroying the person object")

# version 1
person1 = Person("Mark", 20, 6)
print("The name of the person is: " + str(person1.name))

person1.name = "Alfred"
print("The name of the person is: " + str(person1.name))

print("Public " + str(person1.public_prop))