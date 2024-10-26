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
