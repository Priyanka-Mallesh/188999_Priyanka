import uuid
 
class Employee:
    def __init__(self, name, department, designation,gross_salary,tax,bonus,net_salary, employee_id=None):
        self.id = employee_id if employee_id else str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = net_salary
 
    # Convert a Employee objects to dictionary format
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary" : self.gross_salary,
            "tax" : self.tax,
            "bonus" : self.bonus,
            "net_salary" : self.net_salary
        }
 
    # Create a Employee object from dictionary
    @staticmethod
    def from_dict(data):
        return Employee(
           
            name=data['name'],
            department = data["department"],
            designation=data["designation"],
            employee_id=data["id"],
            gross_salary=data["gross_salary"],
            tax=data["tax"],
            bonus=data["bonus"],
            net_salary=data["net_salary"]
           
        )