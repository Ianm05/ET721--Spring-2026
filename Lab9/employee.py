"""
Ian Martinez
Lab 9, Unit Testing
Feb 26, 2026
"""

class Employee:
    # class property
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @property
    def emailemployee(self):
        return f"{self.firstname}.{self.lastname}@email.com"

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    # method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


# Local testing (outside the class)
if __name__ == "__main__":
    employee1 = Employee("Peter", "Parker", 80000)

    print(f"Employee = {employee1.fullname}")
    print(f"Employee email = {employee1.emailemployee}")
    print(f"Employee salary = {employee1.salary}")

    employee1.apply_raise()

    print(f"Employee salary after raise = {employee1.salary} per year")