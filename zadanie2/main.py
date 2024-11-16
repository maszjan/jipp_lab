# Zadanie 2. W oparciu o system z zadania 1 zmodyfikuj/rozszerz go o poniższe funkcjonalności:
# • logowanie do systemu – poprzez konto admin, hasło admin,
# • dane o pracownikach mają być przechowywane w plikach, format pliku dowolny txt, json,
# zewnętrzna baza,
# • dane maja być zapisywane do pliku,
# • wyświetlane dane mają być odczytywane z pliku,
# • każde zmiany/modyfikacje mają być aktualizowane w plikach
# • walidację danych.

from FrontendManager import FrontendManager

if __name__ == "__main__":
    frontend_manager = FrontendManager()
    frontend_manager.run()