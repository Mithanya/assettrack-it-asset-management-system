class EmployeeManager:
    """Manages employee related operations."""

    def __init__(self, db_manager):
        self.db = db_manager

    def add_employee(self, name, department, email, phone):
        """Adds a new employee to the database."""
        query = "INSERT INTO employees (employee_name, department, email, phone) VALUES (%s, %s, %s, %s)"
        success = self.db.execute_query(query, (name, department, email, phone))
        if success:
            print(f"Employee '{name}' added successfully.")

    def view_employees(self):
        """Retrieves and prints all employees."""
        query = "SELECT * FROM employees"
        employees = self.db.fetch_all(query)
        if not employees:
            print("No employees found.")
            return

        print("\n--- Employee List ---")
        for emp in employees:
            print(f"ID: {emp['employee_id']} | Name: {emp['employee_name']} | Dept: {emp['department']} | Email: {emp['email']} | Phone: {emp['phone']}")
