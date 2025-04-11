from employee import Employee
 
class Employee_manager(object):
    def __init__(self):
        self.data = []
 
    # Add new employee
    def add_employee(self, name, department, designation,gross_salary,tax,bonus,net_salary):
        emp = Employee(name, department, designation,gross_salary,tax,bonus,net_salary)
        self.data.append(emp)
        return emp
 
    # View all employees
    def get_all_employee(self):
        return self.data
 
    # Search employee by ID
    def search_employee(self, employee_id):
        for emp in self.data:
            if emp.id == employee_id:
                return emp
        print(" No employee found with that ID.")
        return None
 
    # Delete a employee by ID
    def delete_employee(self, employee_id):
        for emp in self.data:
            if emp.id == employee_id:
                self.data.remove(emp)
                return True
        return False
 
    # Load employee from a list of dictionaries
    def load_tasks(self, employee_dicts):
        self.data = [Employee.from_dict(td) for td in employee_dicts]
 
    # Convert employee to list of dictionaries
    def to_dict_list(self):
        return [emp.to_dict() for emp in self.data]
    
