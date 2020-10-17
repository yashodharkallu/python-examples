from datetime import datetime


class Employee:
    """ Employee class """

    emp_serial = 1001
    pf_serial = 101

    @staticmethod
    def _generate_pf_serial():
        pf_number = Employee.pf_serial
        Employee.pf_serial += 1
        return pf_number

    @classmethod
    def _generate_emp_serial(cls):
        emp_serial = cls.emp_serial
        cls.emp_serial += 1
        return emp_serial


    def __init__(self, name, dept):
        """ Parameterized constructor with default Arguments """
        self.name = name
        self.dept = dept
        self.emp_id = Employee._generate_emp_serial()
        self.pf_number = Employee._generate_pf_serial()

    @classmethod
    def create_emp_dummy(cls):
        return cls(None, None)

    @classmethod
    def create_emp_data_scientist(cls, name, dept='Data Science'):
        return cls(name, dept)

    def __str__(self):
        return 'Employee({}, {}, {}, {})'.format(self.emp_id, self.name, self.dept, self.pf_number)


# Creating an Employee instance
print('------------------- Employee - Ravi ----------------------')
emp_ravi = Employee('Ravi', 'Data Engineering')
print(emp_ravi)
print()

# Creating an Employee instance without name and dept
print('------------------- Employee - Without Name and Dept ---------------------')
emp_dummy = Employee.create_emp_dummy()
print(emp_dummy)
print()

# Creating an Employee instance without name and dept
print('------------------- Employee - Data Scientist ---------------------')
emp_roshith = Employee.create_emp_data_scientist('Ravi')
print(emp_roshith)
print()
