"""
This shows the usage of property decorators
Python @property is one of the built-in decorators.
The main purpose of any decorator is to change your class methods or attributes
in such a way so that the users need not make any additional changes in their code.
"""
import time


class Employee:
    """ Employee class """

    emp_serial = 1001

    @staticmethod
    def _generate_emp_serial():
        emp_serial = Employee.emp_serial
        Employee.emp_serial += 1
        return emp_serial

    def __init__(self, name, dept):
        """ Parameterized constructor with default Arguments """
        self.name = name
        self.dept = dept
        self.emp_id = Employee._generate_emp_serial()

    def __str__(self):
        return 'Employee({}, {}, {})'.format(self.emp_id, self.name, self.dept)

    def time_it(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            print(func.__name__ + " took " + str((end-start)*1000) + "mil sec")
            return result
        return wrapper

    def job(self):
        if self.dept == 'Data Engineering':
            return self.calc_square(range(1000))
        elif self.dept == 'HR':
            return self.calc_bonus(range(10000, 11000))
        else:
            return self.calc_cube(range(1000))

    @time_it
    def calc_square(self, numbers):
        print('{} is calculating squares,'.format(self.name))
        result = []
        for number in numbers:
            result.append(number * number)
        return result

    @time_it
    def calc_cube(self, numbers):
        print('{} is calculating cubes,'.format(self.name))
        result = []
        for number in numbers:
            result.append(number * number * number)
        return result

    @time_it
    def calc_bonus(self, emp_sal):
        print('Calculating employee bonus,')
        result = []
        for sal in emp_sal:
            result.append(sal * 0.1)
        return result


# Creating a Employee instance
print('------------------- Employee - Ravi ----------------------')
emp_ravi = Employee('Ravi', 'Data Engineering')
print(emp_ravi)
print(emp_ravi.job())
# print(emp_ravi.calc_cube(range(1000)))
# print(emp_ravi.calc_bonus(range(10000, 11000)))
print()

# Creating a Data Science Employee instance
print('------------------- Employee - Roshith ---------------------')
emp_roshith = Employee('Roshith', 'HR')
print(emp_roshith)
print(emp_roshith.job())





