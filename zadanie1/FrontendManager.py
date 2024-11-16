from EmployeesManager import EmployeesManager
from Employee import Employee

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def add_employee(self):
        name = input("Wprowadź imię i nazwisko: ")
        age = int(input("Wprowadź wiek: "))
        salary = float(input("Wprowadź wynagrodzenie: "))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)

    def display_employees(self):
        self.manager.display_employees()

    def remove_employees_by_age_range(self):
        min_age = int(input("Wprowadź minimalny wiek: "))
        max_age = int(input("Wprowadź maksymalny wiek: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)

    def update_salary_by_name(self):
        name = input("Wprowadź imię i nazwisko: ")
        new_salary = float(input("Wprowadź nowe wynagrodzenie: "))
        if self.manager.update_salary_by_name(name, new_salary):
            print("Wynagrodzenie zaktualizowane pomyślnie.")
        else:
            print("Nie znaleziono pracownika.")

    def run(self):
        while True:
            print("\n1. Dodaj pracownika")
            print("2. Wyświetl pracowników")
            print("3. Usuń pracowników na podstawie przedziału wiekowego")
            print("4. Zaktualizuj wynagrodzenie według nazwiska")
            print("5. Wyjdź")
            choice = input("Wprowadź swój wybór: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.display_employees()
            elif choice == '3':
                self.remove_employees_by_age_range()
            elif choice == '4':
                self.update_salary_by_name()
            elif choice == '5':
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")