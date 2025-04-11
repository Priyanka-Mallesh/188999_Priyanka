import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        emp = Employee("Priyanka", "semicon", "Manager", 500000, 5000, 2000)
        self.assertEqual(emp.name, "Priyanka")
        self.assertEqual(emp.department, "semicon")
        self.assertEqual(emp.designation, "Manager")
        self.assertEqual(emp.net_salary, 470000)
def test_to_dict(self):
        emp = Employee("Ganesh", "Bfarm", "S", "500000", "10000", "3000", "50000")
        data = emp.to_dict()
        self.assertEqual(data["name"], "Ganesh")
 
def test_from_dict(self):
        data = {
            "employee_id": "123",
            "name": "Test",
            "department": "Admin",
            "designation": "Officer",
            "gross_salary": "70000",
            "tax": "7000",
            "bonus": "3000",
            "net_salary": "66000"
        }
        emp = Employee.from_dict(data)
        self.assertEqual(emp.id, "123")
        self.assertEqual(emp.name, "Test")
if __name__ == "__main__":
    unittest.main()