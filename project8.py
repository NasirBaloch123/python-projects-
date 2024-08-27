import string
def analyze_text(input_text):
    analysis = {
        'word_count': {},
        'sentence_count': 0,
        'average_word_length': 0.0
    }

    text_no_punct = input_text.translate(str.maketrans('', '', string.punctuation))
    words = text_no_punct.split()
    for word in words:
        word_lower = word.lower()
        if word_lower in analysis['word_count']:
            analysis['word_count'][word_lower] += 1
        else:
            analysis['word_count'][word_lower] = 1

    analysis['sentence_count'] = input_text.count('.') + input_text.count('!') + input_text.count('?')

    if words:
        total_word_length = sum(len(word) for word in words)
        analysis['average_word_length'] = total_word_length / len(words)
    return analysis

input_text = str(input("Enter a Sentence"))
result = analyze_text(input_text)
print(result)
