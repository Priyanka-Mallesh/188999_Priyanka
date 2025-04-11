import os
from employee_manager import Employee_manager
from storage import Storage

def main():
    # Initialize manager and storage with a Pickle file
    storage_file = "employee.pkl"
    manager = Employee_manager()
    storage = Storage(filepath=storage_file)

    # Load existing data from the Pickle file
    if os.path.exists(storage_file):
        print("Loading existing employee data")
        manager.load_tasks(storage.load())
        print(f"Loaded {len(manager.data)} employees successfully")
    else:
        print("No existing data found. Starting fresh.")

    while True:
        print("\n--- Employee Management System ---")
        print("1. Add a New Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete an Employee")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")
            gross_salary = float(input("Enter Gross Salary: "))
            tax = float(input("Enter Tax Amount: "))
            bonus = float(input("Enter Bonus Amount: "))
            net_salary = gross_salary - tax + bonus  # Calculate net salary

            emp = manager.add_employee(name, department, designation, gross_salary, tax, bonus, net_salary)
            print(f"Employee added successfully! ID: {emp.id}")

        elif choice == "2":
            employees = manager.get_all_employee()
            if not employees:
                print("No employees found.")
            else:
                print("\n--- Employee List ---")
                for emp in employees:
                    print(f"ID: {emp.id}, Name: {emp.name}, Department: {emp.department}, "
                          f"Designation: {emp.designation}, Gross Salary: {emp.gross_salary}, "
                          f"Tax: {emp.tax}, Bonus: {emp.bonus}, Net Salary: {emp.net_salary}")

        elif choice == "3":
            employee_id = input("Enter Employee ID to Search: ")
            emp = manager.search_employee(employee_id)
            if emp:
                print(f"Employee Found: ID: {emp.id}, Name: {emp.name}, Department: {emp.department}, "
                      f"Designation: {emp.designation}, Gross Salary: {emp.gross_salary}, "
                      f"Tax: {emp.tax}, Bonus: {emp.bonus}, Net Salary: {emp.net_salary}")
            else:
                print("No employee found with that ID.")

        elif choice == "4":
            employee_id = input("Enter Employee ID to Delete: ")
            success = manager.delete_employee(employee_id)
            print("Employee deleted successfully!" if success else "Employee not found.")

        elif choice == "5":
            # Save data to the Pickle file before exiting
            storage.save(manager.to_dict_list())
            print("Data saved successfully. Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
