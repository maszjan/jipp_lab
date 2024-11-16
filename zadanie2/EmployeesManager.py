import json
from Employee import Employee

class EmployeesManager:
    def __init__(self, filename='employees.json'):
        self.filename = filename
        self.employees = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.employees = [Employee(**emp) for emp in data]
        except FileNotFoundError:
            self.employees = []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump([emp.__dict__ for emp in self.employees], file)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_data()

    def display_employees(self):
        for employee in self.employees:
            print(employee)

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_data()

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def update_salary_by_name(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
            self.save_data()
            return True
        return False