#!/usr/bin/python
"""
@staticmethod decorator is used to add static methods, that's shared commonly by all the instances
"""


class Employee:
    """ Employee class """

    emp_serial = 1001
    pf_serial = 101

    @staticmethod
    def _generate_pf_serial():
        pf_number = Employee.pf_serial
        Employee.pf_serial += 1
        return pf_number

    def __init__(self, name, dept):
        """ Parameterized constructor with default Arguments """
        self.name = name
        self.dept = dept
        # Can't access 'next_serial' like this!
        # self.emp_id = next_serial
        # next_serial += 1
        # Not readable! 'next_serial' shouldn't be part of the of an object!
        # self.emp_id = self.next_serial
        # self.next_serial += 1
        self.emp_id = Employee.emp_serial
        Employee.emp_serial += 1
        self.pf_number = Employee._generate_pf_serial()

    def __str__(self):
        return 'Employee({}, {}, {}, {})'.format(self.emp_id, self.name, self.dept, self.pf_number)


# Creating a Employee instance
print('------------------- Employee - Ravi ----------------------')
emp_ravi = Employee('Ravi', 'Data Engineering')
print(emp_ravi)
print()

# Creating a Data Science Employee instance
print('------------------- Employee - Roshith ---------------------')
emp_roshith = Employee('Roshith', 'Data Engineering')
print(emp_roshith)

