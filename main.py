from functools import reduce


#     Zadanie 1. Analiza Tekstu i Transformacje Funkcyjne
#     Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji
#     analizy tekstu:
#       • Zlicza liczbę słów, zdań, i akapitów w tekście.
#       • Wyszukuje najczęściej występujące słowa, wykluczając tzw. stop words (np. "i", "a", "the"). w, i, o, a, z
#       • Transformuje wszystkie wyrazy rozpoczynające się na literę "a" lub "A" do ich odwrotności (np.
#         "apple" → "elppa").
#     Wskazówka: Użyj map(), filter(), i list składanych, aby przeprowadzać transformacje na tekście.

def text_analysis(text):
    stop_words = set(
        ["w", "i", "o", "a", "z", "the", "and", "to", "of", "in", "that", "it", "is", "was", "he", "for", "on", "are",
         "as", "with", "his", "they", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but",
         "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which",
         "she", "do", "how", "their", "if"])

    paragraphs = text.split('\n\n')
    sentences = reduce(lambda acc, para: acc + para.split('. '), paragraphs, [])
    words = reduce(lambda acc, sent: acc + sent.split(), sentences, [])

    num_paragraphs = len(paragraphs)
    num_sentences = len(sentences)
    num_words = len(words)

    filtered_words = list(filter(lambda word: word.lower() not in stop_words, words))
    word_frequencies = reduce(lambda acc, word: {**acc, word.lower(): acc.get(word.lower(), 0) + 1}, filtered_words, {})
    most_common_words = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)[:10]

    transformed_words = list(map(lambda word: word[::-1] if word.lower().startswith('a') else word, words))

    transformed_text = ' '.join(transformed_words)

    return {
        "Liczba akapitów:": num_paragraphs,
        "Liczba zdań:": num_sentences,
        "Liczba słów:": num_words,
        "Najczęściej występujące słowa": most_common_words,
        "Tekst po transformacji:": transformed_text
    }


text = """
ala ma kota

ala ma kota
agrafka
Artysta
ala ma kota
"""

print(text_analysis(text))

#   Zadanie 2: Walidacja i Przekształcenia Operacji na Macierzach
#   Stwórz system, który przyjmuje operacje na macierzach jako stringi i wykonuje je dynamicznie,
#   zapewniając jednocześnie walidację poprawności operacji:
#       • Operacje mogą obejmować dodawanie, mnożenie i transponowanie macierzy.
#       • System powinien sprawdzać poprawność operacji (zgodność wymiarów) i zwracać wynik w
#       postaci macierzy.
#       • Wykorzystaj eval() i exec() do wykonywania operacji na macierzach, a także funkcje
#       walidacyjne, które sprawdzają poprawność przed wykonaniem.
#   Wskazówka: Zaimplementuj walidację operacji i użyj funkcji funkcyjnych do przekształceń i obliczeń na
#   macierzach.

import numpy as np


def validate_addition(matrix1, matrix2):
    return matrix1.shape == matrix2.shape


def validate_multiplication(matrix1, matrix2):
    return matrix1.shape[1] == matrix2.shape[0]


def perform_operation(operation, matrix1=None, matrix2=None, axes=None):
    if operation == "add":
        if validate_addition(matrix1, matrix2):
            return matrix1 + matrix2
        else:
            raise ValueError("Dimensions do not match for addition.")
    elif operation == "multiply":
        if validate_multiplication(matrix1, matrix2):
            return np.dot(matrix1, matrix2)
        else:
            raise ValueError("Dimensions do not match for multiplication.")
    elif operation == "transpose":
        if axes is not None:
            return np.transpose(matrix1, axes=axes)
        else:
            return matrix1.T
    else:
        raise ValueError("Unsupported operation.")


def matrix_operation(input_string):
    try:
        operation, matrices = input_string.split(':')
        matrices = eval(matrices)

        matrices = [np.array(matrix) for matrix in matrices]

        if operation == "add":
            result = perform_operation("add", matrices[0], matrices[1])
        elif operation == "multiply":
            result = perform_operation("multiply", matrices[0], matrices[1])
        elif operation == "transpose":
            if len(matrices) > 1:
                axes = tuple(matrices[1])
                result = perform_operation("transpose", matrices[0], axes=axes)
            else:
                result = perform_operation("transpose", matrices[0])
        else:
            raise ValueError("Unsupported operation.")

        return result
    except Exception as e:
        return str(e)


input_string_add = "add: ([[1, 2], [3, 4]], [[5, 6], [7, 8]])"
input_string_multiply = "multiply: ([[1, 2], [3, 4]], [[5, 6], [7, 8]])"
input_string_transpose = "transpose: ([[1, 2], [3, 4]], (1, 0))"

print("Wynik dodawania:\n", matrix_operation(input_string_add))
print("Wynik mnożenia:\n", matrix_operation(input_string_multiply))
print("Wynik transponowania:\n", matrix_operation(input_string_transpose))


#     Zadanie 3. Dynamiczne Wyznaczanie Ekstremów w Niejednorodnych Danych
#     Napisz funkcję, która przyjmuje listę niejednorodnych danych (np. liczby, napisy, krotki, listy, słowniki) i
#     wykonuje dynamiczną analizę danych, aby:
#       • Zwrócić największą liczbę (lub wartość numeryczną) w danych.
#       • Zwrócić najdłuższy napis.
#       • Zwrócić krotkę o największej liczbie elementów.
#     Wskazówka: Użyj filter() do selekcji odpowiednich typów danych oraz map() do przekształceń na
#     elementach.

def dynamic_analysis(data_to_analyse):
    numerical_values = list(filter(lambda x: isinstance(x, (int, float)), data_to_analyse))
    max_number = max(numerical_values) if numerical_values else None

    strings = list(filter(lambda x: isinstance(x, str), data))
    longest_string = max(strings, key=len) if strings else None

    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    largest_tuple = max(tuples, key=len) if tuples else None

    return {
        "max_number": max_number,
        "longest_string": longest_string,
        "largest_tuple": largest_tuple
    }


data = [
    42, "hello", (1, 2, 3), [1, 2, 3, 4], {"key": "value"}, 3.14, "world", (1, 2), "Python", (1, 2, 3, 4, 5)
]

result = dynamic_analysis(data)
print("Największa liczba:", result["max_number"])
print("Najdłuższy napis:", result["longest_string"])
print("Krotka o największej liczbie elementów:", result["largest_tuple"])


#           Zadanie 4 Implementacja Złożonej Funkcji Matrycowej z Użyciem reduce()
#           Napisz program, który przyjmuje listę macierzy i łączy je w jedną za pomocą operacji zdefiniowanej
#           przez użytkownika (np. suma macierzy, iloczyn), korzystając z reduce(). Program powinien:
#               • Dynamicznie wywoływać różne operacje (np. sumowanie, mnożenie) na macierzach.
#               • Umożliwiać definiowanie niestandardowych operacji przez użytkownika.
#           Wskazówka: Wykorzystaj reduce() do łączenia macierzy oraz eval() do dynamicznej definicji operacji.


def validate_addition_matrix(matrix1, matrix2):
    return len(matrix1) == len(matrix2) and all(len(row) == len(matrix2[i]) for i, row in enumerate(matrix1))


def validate_multiplication_matrix(matrix1, matrix2):
    return len(matrix1[0]) == len(matrix2)


def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def perform_custom_operation(operation, matrix1, matrix2):
    return eval(
        f"[[matrix1[i][j] {operation} matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]")


def combine_matrices(matrices_to_combine, operation):
    if not matrices_to_combine:
        raise ValueError("Brak podanych macierzy.")

    if len(matrices_to_combine) == 1:
        return matrices_to_combine[0]

    if operation == "add":
        return reduce(lambda acc, matrix: add_matrices(acc, matrix) if validate_addition_matrix(acc, matrix) else acc,matrices_to_combine)
    elif operation == "multiply":
        return reduce(lambda acc, matrix: multiply_matrices(acc, matrix) if validate_multiplication_matrix(acc, matrix) else acc,matrices_to_combine)
    else:
        return reduce(lambda acc, matrix: perform_custom_operation(operation, acc, matrix) if validate_addition_matrix(acc, matrix) else acc, matrices_to_combine)


# Przykładowe użycie
matrices = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

operation_add = "add"
operation_multiply = "multiply"
operation_custom = "+"

print("Suma macierzy:\n", combine_matrices(matrices, operation_add))
print("Iloczyn macierzy:\n",
      combine_matrices(matrices[:2], operation_multiply))  # Tylko pierwsze dwie macierze do mnożenia
print("Niestandardowa operacja (dodawanie) na macierzach:\n", combine_matrices(matrices, operation_custom))


#               Zadanie 5. System Dynamicznego Generowania Kodów Python (Metaprogramowanie)
#               Napisz narzędzie, które generuje dynamicznie kod w Pythonie na podstawie szablonów i danych
#               wejściowych, a następnie uruchamia ten kod. Narzędzie powinno:
#                   • Przyjmować szablon kodu jako string (np. def funkcja(x): return x + 2).
#                   • Uzupełniać szablon o brakujące fragmenty kodu (np. zmienne, funkcje) w czasie działania.
#                   • Weryfikować poprawność generowanego kodu przed uruchomieniem.
#               Wskazówka: Wykorzystaj eval() i exec() w połączeniu z walidacją wejściową i generowaniem kodu z szablonów


def generate_code(template, context):
    """
    Generuje kod Pythona, wypełniając szablon podanym kontekstem.

    :param template: String reprezentujący szablon kodu.
    :param context: Słownik zawierający zmienne i funkcje do wypełnienia szablonu.
    :return: Wygenerowany kod jako string.
    """
    try:
        for key, value in context.items():
            if not isinstance(key, str):
                raise ValueError("Klucze w kontekście muszą być stringami.")

        code = template.format(**kontekst)

        compile(code, '<string>', 'exec')

        return code
    except Exception as e:
        return str(e)


def execute_code(code):
    """
    Wykonuje wygenerowany kod Pythona.

    :param code: String reprezentujący kod Pythona do wykonania.
    :return: Wynik wykonanego kodu.
    """
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return exec_globals
    except Exception as e:
        return str(e)


szablon = """
def dynamic_function(x):
    return x + {increment}

result = dynamic_function({value})
"""

kontekst = {
    "increment": 2,
    "value": 5
}

generated_code = generate_code(szablon, kontekst)
print("Wygenerowany kod:\n", generated_code)

execution_result = execute_code(generated_code)
print("Wynik wykonania:\n", execution_result.get('result'))