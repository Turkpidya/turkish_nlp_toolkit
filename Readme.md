# Enhanced Turkish Language Processing Toolkit

This toolkit provides advanced natural language processing functions for Turkish, including:

- Vowel harmony checking
- Pluralization (with special case handling)
- Tokenization (improved for Turkish-specific cases)
- Accent removal
- Stemming
- Basic spell checking

It can be useful for developers working with Turkish text or learning about Turkish language features.

## Features

1. **Vowel Harmony Checking**: Determine if a word follows Turkish vowel harmony rules.
2. **Pluralization**: Add the appropriate plural suffix to Turkish words, handling special cases.
3. **Tokenization**: Split Turkish text into tokens, properly handling possessive suffixes and punctuation.
4. **Accent Removal**: Remove diacritical marks from Turkish text.
5. **Stemming**: Extract the stem of Turkish words by removing common suffixes.
6. **Spell Checking**: Detect and correct common spelling mistakes in Turkish words.

## Usage

```python
from turkish_nlp_toolkit import TurkishNLP

# Initialize the toolkit
nlp = TurkishNLP()

# Check vowel harmony
word = "kitap"
is_harmonic = nlp.check_vowel_harmony(word)
print(f"Is '{word}' vowel harmonic? {is_harmonic}")

# Pluralize a word
singular = "elma"
plural = nlp.pluralize(singular)
print(f"Plural of '{singular}': {plural}")

# Tokenize a sentence
sentence = "Ali'nin kitabı masada."
tokens = nlp.tokenize(sentence)
print(f"Tokens: {tokens}")

# Remove accents
accented_text = "şeker çörek"
plain_text = nlp.remove_accents(accented_text)
print(f"Without accents: {plain_text}")

# Stem a word
word = "kitaplar"
stemmed = nlp.stem(word)
print(f"Stem of '{word}': {stemmed}")

# Spell check
misspelled = "cok"
corrected, was_corrected = nlp.spell_check(misspelled)
if was_corrected:
    print(f"'{misspelled}' corrected to '{corrected}'")
else:
    print(f"'{misspelled}' is correctly spelled")
```

## Installation

Clone this repository and install the required dependencies:

```
git clone https://github.com/yourusername/turkish-nlp-toolkit.git
cd turkish-nlp-toolkit
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
