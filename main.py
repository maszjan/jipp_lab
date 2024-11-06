from collections import deque
from functools import reduce

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
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path

        if node not in visited:
            for neighbour in graph.get(node,[]):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)

    return None

graph = {
    '1': ['2', '3', '5'],
    '2': ['1', '3', '4', '5'],
    '3': ['1', '2', '4'],
    '4': ['2', '3', '5'],
    '5': ['1', '2', '4'],
}

print (bfs(graph, '1', '4'))

#   Zadanie 3 Optymalizacja Rozmieszczenia Zadań (Proceduralne i Funkcyjne)
#   Masz N zadań do wykonania, każde zadanie ma przypisany czas wykonania oraz nagrodę za jego
#   ukończenie. Twoim celem jest zaplanowanie kolejności wykonywania zadań, aby zminimalizować
#   całkowity czas oczekiwania na ich wykonanie i zmaksymalizować zysk. Zaimplementuj rozwiązanie przy
#   użyciu programowania proceduralnego oraz funkcyjnego.
#   Wymagania:
#       • Proceduralnie: Stwórz listę zadań i użyj pętli do sortowania i optymalizacji ich kolejności, aby
#         zminimalizować całkowity czas oczekiwania.
#       • Funkcyjnie: Użyj funkcji wyższego rzędu (sorted, map, reduce) do manipulacji listą zadań, aby
#         osiągnąć optymalne rozwiązanie.
#       • Program powinien zwrócić optymalną kolejność zadań oraz całkowity czas oczekiwania.


class Task:
    def __init__(self, execution_time, reward):
        self.execution_time = execution_time
        self.reward = reward

    def __repr__(self):
        return f"Task(czas_wykonania={self.execution_time}, nagroda={self.reward})"


example_tasks = [
    Task(3, 50),
    Task(1, 20),
    Task(2, 30),
    Task(5, 60),
    Task(4, 40)
]


def optimize_tasks_procedural(tasks):
    tasks.sort(key=lambda task: task.execution_time)

    total_waiting_time = 0
    current_time = 0
    for task in tasks:
        current_time += task.execution_time
        total_waiting_time += current_time

    return tasks, total_waiting_time





def optimize_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task.execution_time)

    total_waiting_time = reduce(lambda acc, task: acc + task.execution_time, sorted_tasks, 0)

    return sorted_tasks, total_waiting_time



optimized_tasks_procedural, total_waiting_time_procedural = optimize_tasks_procedural(example_tasks.copy())
print("Proceduralne podejście:")
print("Optymalna kolejność zadań:", optimized_tasks_procedural)
print("Całkowity czas oczekiwania:", total_waiting_time_procedural)

optimized_tasks_functional, total_waiting_time_functional = optimize_tasks_functional(example_tasks.copy())
print("\nFunkcyjne podejście:")
print("Optymalna kolejność zadań:", optimized_tasks_functional)
print("Całkowity czas oczekiwania:", total_waiting_time_functional)



#       Zadanie 4: Problem Optymalizacji Zasobów – Algorytm Plecakowy (Proceduralne i Funkcyjne) Masz ograniczoną pojemność plecaka oraz listę przedmiotów,
#       z których każdy ma określoną wagę i wartość. Celem jest wybranie przedmiotów tak, aby zmaksymalizować łączną wartość w plecaku, nie przekraczając jego pojemności.
#       Problem ten wymaga implementacji algorytmu plecakowego (knapsack problem) przy użyciu zarówno podejścia proceduralnego, jak i funkcyjnego.
#       Wymagania:
#           • Proceduralnie: Użyj podejścia dynamicznego (programowanie dynamiczne) do rozwiązania problemu.
#           • Funkcyjnie: Zaimplementuj algorytm w stylu funkcyjnym z naciskiem na funkcje rekurencyjne oraz mapowanie.
#           • Program powinien zwracać maksymalną wartość oraz listę przedmiotów, które powinny zostać wybrane do plecaka.


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item(waga={self.weight}, wartość={self.value})"

items = [
    Item(2, 3),
    Item(3, 4),
    Item(4, 5),
    Item(5, 8)
]

max_capacity = 5

def knapsack_procedural(items, max_capacity):
    n = len(items)
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            if items[i-1].weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1].weight] + items[i-1].value)
            else:
                dp[i][w] = dp[i-1][w]

    w = max_capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w -= items[i-1].weight

    return dp[n][max_capacity], selected_items

def knapsack_functional(items, max_capacity):
    def knapsack_recursive(n, w):
        if n == 0 or w == 0:
            return 0
        if items[n-1].weight > w:
            return knapsack_recursive(n-1, w)
        else:
            return max(knapsack_recursive(n-1, w), knapsack_recursive(n-1, w-items[n-1].weight) + items[n-1].value)

    def get_selected_items(n, w):
        if n == 0 or w == 0:
            return []
        if items[n-1].weight > w:
            return get_selected_items(n-1, w)
        else:
            if knapsack_recursive(n-1, w) > knapsack_recursive(n-1, w-items[n-1].weight) + items[n-1].value:
                return get_selected_items(n-1, w)
            else:
                return get_selected_items(n-1, w-items[n-1].weight) + [items[n-1]]

    max_value = knapsack_recursive(len(items), max_capacity)
    selected_items = get_selected_items(len(items), max_capacity)
    return max_value, selected_items


max_value_procedural, selected_items_procedural = knapsack_procedural(items, max_capacity)
print("Proceduralne podejście:")
print("Maksymalna wartość:", max_value_procedural)
print("Wybrane przedmioty:", selected_items_procedural)

max_value_functional, selected_items_functional = knapsack_functional(items, max_capacity)
print("\nFunkcyjne podejście:")
print("Maksymalna wartość:", max_value_functional)
print("Wybrane przedmioty:", selected_items_functional)