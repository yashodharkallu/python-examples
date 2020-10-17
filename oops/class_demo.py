#!/usr/bin/python
"""
Everything in Python is object, e.g. a.__add__(b) and a + b
__init__  : Object initialized using
Object initialisation is controlled by an instance method with the name __init__ and which is also generally called as a Constructor.
Any attributes set under the init() constructor will be instantiated at the time of instance creation.
instance_attr is an instance attribute defined inside the constructor.
"""


class Employee:
    """ Employee class """

    def __init__(self, name, dept):
        """ Parameterized constructor with default Arguments """
        print('__init__ function got called!')
        self.name = name
        self.dept = dept


# Creating a Employee instance
print('------------------- Employee - Ravi ----------------------')
emp_ravi = Employee('Ravi', 'IT')
print('Employee({}, {})'.format(emp_ravi.name, emp_ravi.dept))

# Overriding employee object attributes
emp_ravi.name = "Ravi Kiran"
emp_ravi.dept = "Data Engineering"
print('Employee({}, {})'.format(emp_ravi.name, emp_ravi.dept))
print()

# Creating another Employee instance
print('------------------- Employee - Roshith ---------------------')
emp_roshith = Employee('Roshith', 'Data Engineering')
print(emp_roshith)
print('Employee({}, {})'.format(emp_roshith.name, emp_roshith.dept))
print()

print('Models: {} = {}, {} = {}'.format(emp_ravi.name, emp_ravi.dept, emp_roshith.name, emp_roshith.dept))
print('Models: {0.name} = {0.dept}, {1.name} = {1.dept}'.format(emp_ravi, emp_roshith))
