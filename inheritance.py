#Udacity - Programming Foundations with Python
#
#Assignment - Sample program to experiment with inheritance.

class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys

billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.num_of_toys)

