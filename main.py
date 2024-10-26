from functools import reduce
import numpy as np

#     Zadanie 1. Analiza Tekstu i Transformacje Funkcyjne
#     Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji
#     analizy tekstu:
#       • Zlicza liczbę słów, zdań, i akapitów w tekście.
#       • Wyszukuje najczęściej występujące słowa, wykluczając tzw. stop words (np. "i", "a", "the"). w, i, o, a, z
#       • Transformuje wszystkie wyrazy rozpoczynające się na literę "a" lub "A" do ich odwrotności (np.
#         "apple" → "elppa").
#     Wskazówka: Użyj map(), filter(), i list składanych, aby przeprowadzać transformacje na tekście.

def text_analysis(text):
    stop_words = set(["w", "i", "o", "a", "z", "the", "and", "to", "of", "in", "that", "it", "is", "was", "he", "for", "on", "are", "as", "with", "his", "they", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if"])

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

print("Addition Result:\n", matrix_operation(input_string_add))
print("Multiplication Result:\n", matrix_operation(input_string_multiply))
print("Transposition Result:\n", matrix_operation(input_string_transpose))
