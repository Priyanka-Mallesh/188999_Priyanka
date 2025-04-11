import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from employee_manager import Employee_manager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = Employee_manager(storage_file="test_employees.pkl")

    def test_add_employee(self):
        emp = self.manager.add_employee("priya", "semicon", "a1", 600000, 8000, 4000)
        self.assertEqual(emp.name, "priya")
        self.assertEqual(len(self.manager.employees), 1)

def test_find_by_id(self):
        emp = self.manager.add_employee("manju", "business", "Analyst", "55000", "5000", "2000", "52000")
        found = self.manager.find_by_id(emp.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "manju")
 
def test_delete_employee(self):
        emp = self.manager.add_employee("priyanka", "Support", "software", "40000", "3000", "1000", "38000")
        result = self.manager.delete_employee(emp.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all_employee()), 0)

if __name__ == "__main__":
    unittest.main()