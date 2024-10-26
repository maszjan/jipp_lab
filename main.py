from collections import deque

#   Zadanie 1. Problem Podziału Paczek (Prograowanie Proceduralne)
#       Mamy listę paczek o różnych wagach oraz maksymalną wagę, jaką może unieść kurier w jednym kursie.
#       Twoim zadaniem jest podzielić paczki na jak najmniejszą liczbę kursów, aby każda waga nie przekraczała
#       maksymalnej dozwolonej wagi. Program powinien korzystać z algorytmu zachłannego do optymalizacji
#       podziału paczek.
#       Wymagania:
#           • Napisz funkcję, która przyjmuje listę wag paczek i maksymalną wagę.
#           • Użyj pętli for i instrukcji warunkowych if, else do iteracyjnego podziału paczek.
#           • Program powinien zwracać minimalną liczbę kursów oraz listę paczek w każdym kursie.

def getMinimamalCoursesWithPackages(packagesWeightList, maxWeight):
    for package in packagesWeightList:
        if package > maxWeight:
            raise ValueError(f"Package {package} is larger than maximum weight {maxWeight}")
    sortedWeights = sorted(packagesWeightList, reverse=True)
    courses = []
    for weight in sortedWeights:
        isAdded = False
        for course in courses:
            if sum(course) + weight <= maxWeight:
                course.append(weight)
                isAdded = True
                break
        if not isAdded:
            courses.append([weight])
    return len(courses), courses


packages = [ 7, 5, 7, 8, 5, 3, 10, 10, 2, 7, 8, 3, 2, 13 ]
maxWeight = 20

coursesNumber, courses = getMinimamalCoursesWithPackages(packages, maxWeight)

# for i, course in enumerate(courses, 1):
#     print(f" Course {i}: {course} - Sum of weights {sum(course)}")

#   Zadanie 2. Wyznaczanie Najkrótszej Ścieżki (Programowanie Funkcyjne)
#   Stwórz program obliczający najkrótszą ścieżkę w grafie nieważonym przy użyciu algorytmu BFS
#   (Breadth-First Search). Implementacja powinna być zrealizowana przy użyciu programowania
#   funkcyjnego z naciskiem na niemutowalne struktury danych, funkcje lambda, i mapowanie.
#   Wymagania:
#         • Napisz funkcję BFS przy użyciu funkcyjnego podejścia z rekurencją lub funkcjami wyższego
#            rzędu.
#         • Zaimplementuj graf jako słownik (dict), gdzie klucz to wierzchołek, a wartość to lista sąsiednich
#           wierzchołków.
#         • Funkcja powinna przyjmować graf oraz wierzchołek początkowy i końcowy, zwracając
#           najkrótszą ścieżkę jako listę wierzchołków.


def bfs(graph, start, end):
    queue = deque([start])
    visited = set([start])
    predecessors = {start: None}

    while queue:
        node = queue.popleft()

        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = predecessors[node]
            path.reverse()
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                predecessors[neighbour] = node

    return None

exampleGraph = {
    'A': ['B', 'D'],
    'B': ['A', 'D', 'C'],
    'C': ['B', 'F'],
    'D': ['B', 'A', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E', 'C']
}

print (bfs(exampleGraph, 'F', 'B'))