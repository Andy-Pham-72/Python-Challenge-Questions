# @property

class Employee:
    def __init__(self, name, new_salary):
        self._salary = new_salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid salary")
        self._salary = new_salary

if __name__ == '__main__':
    emp = Employee("Andy Pham", 50000)

    # accessing the "property"
    print(emp.salary)

    # @salary.setter
    emp.salary = 60000
    print(emp.salary)
    # raise error
    emp.salary = -1000