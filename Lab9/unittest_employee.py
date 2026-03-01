"""
Ian Martinez
Lab 9, Unit Testing
Feb 26, 2026
"""

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee("Peter", "Parker", 80000)

    def test_emailemployee(self):
        self.assertEqual(
            self.employee1.emailemployee,
            "Peter.Parker@email.com"
        )

    def test_fullname(self):
        self.assertEqual(
            self.employee1.fullname,
            "Peter Parker"
        )

    def test_apply_raise(self):
        self.assertEqual(self.employee1.salary, 80000)
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.salary, 84000)

    def test_email_updates_when_name_changes(self):
        self.employee1.firstname = "Miles"
        self.assertEqual(
            self.employee1.emailemployee,
            "Miles.Parker@email.com"
        )


if __name__ == "__main__":
    unittest.main()