# Zadanie 1. Z wykorzystaniem OOP zaproponuj implementację Employees System Project.
# Employees System Project ma być prostym projektem oparty na języku Python, który prezentuje
# wykorzystanie zasad programowania obiektowego (OOP). Obejmować ma trzy główne klasy: Employee,
# EmployeesManager i FrontendManager. System ma za zadanie zarządzać danymi i interakcją
# pracowników przy użyciu koncepcji OOP. Employees System Project powinien objemować trzy
# podstawowe klasy, z których każda służy odrębnemu celowi:
# 1. Employee - reprezentuje indywidualnego pracownika z następującymi atrybutami:
# • name: Imię i nazwisko pracownika.
# • age: Wiek pracownika.
# • salary: Wynagrodzenie pracownika.
# Klasa ma udostępniać metody pozwalające na reprezentację informacji o pracownikach, które zostały
# wprowadzone jako dane wejściowe.
# 2. EmployeesManager – klasa która jest odpowiedzialna za zarządzanie listą pracowników. Posiada
# nastepujące funkcjonalności:
# • dodanie nowego pracownika do listy,
# • wyświetlenie listy wszystkich istniejących pracowników,
# • usunięcie pracowników w określonym przedziale wiekowym,
# • wyszukanie pracownika według jego imienia i nazwiska,
# • aktualizacja wynagrodzenia pracownika według jego imienia i nazwiska.
# 3. FrontendManager - klasa zapewnia interfejs użytkownika do interakcji z EmployeesManager.
# Użytkownicy mogą wykonywać akcje takie jak:
# • Dodawanie nowych pracowników.
# • Wyświetlenie listy istniejących pracowników.
# • Usuwanie pracowników na podstawie przedziału wiekowego.
# • Aktualizacja wynagrodzeń pracowników według nazwiska.\

from FrontendManager import FrontendManager

if __name__ == "__main__":
    frontend_manager = FrontendManager()
    frontend_manager.run()
