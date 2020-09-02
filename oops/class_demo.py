#!/usr/bin/python
"""
Everything in Python is object, e.g. a.__add__(b) and a + b
__init__  : Object initialized using
Object initialisation is controlled by an instance method with the name __init__ and which is also generally called as a Constructor.
Any attributes set under the init() constructor will be instantiated at the time of instance creation.
instance_attr is an instance attribute defined inside the constructor.
"""


class Student:
    """ Student class """
    standard = '10th'

    def __init__(self, id=0, name=None):
        """ Parameterized constructor with default Arguments """
        print('Calling __init__()')
        self.id = id
        self.name = name
        self.bigdata = False

    def knows_bigdata(self):
        self.bigdata = True

    def show_details(self):
        print("Student({}, {}, {}, {})".format(self.id, self.name, self.standard, self.bigdata))


# Creating a student with default's
student1 = Student()
student1.show_details()

# Setting student object attributes
student1.id = 101
student1.name = "Kalpesh"
student1.show_details()

# Creating a student by passing initial values
student2 = Student(102, 'Roshith')
student2.show_details()

print('Models: {} = {}, {} = {}'.format(student1.id, student1.name, student2.id, student2.name))
print('Models: {0.id} = {0.name}, {1.id} = {1.name}'.format(student1, student2))
student2.knows_bigdata()
print('{} knows Big Data: {}'.format(student2.name, student2.bigdata))
student2.python = True
print('{} knows Python: {}'.format(student2.name, student2.python))
# AttributeError: 'Student' object has no attribute 'python'
# print('{} knows Python: {}'.format(student1.name, student1.python))
print('{} in {} standard'.format(student1.name, student1.standard))
student2.standard = '9th'
print('{} in {} standard'.format(student2.name, student2.standard))
