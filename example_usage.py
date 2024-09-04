from turkish_nlp_toolkit import TurkishNLP

def main():
    # Initialize the toolkit
    nlp = TurkishNLP()

    print("Enhanced Turkish Language Processing Toolkit Example Usage\n")

    # Vowel harmony checking
    words = ["kitap", "gelmek", "otobüs", "kalem", "bilgisayar", "çiçek"]
    print("Vowel Harmony Check:")
    for word in words:
        is_harmonic = nlp.check_vowel_harmony(word)
        print(f"  Is '{word}' vowel harmonic? {is_harmonic}")
    print()

    # Pluralization
    singulars = ["elma", "kalem", "ağaç", "gül", "köpek", "su", "kitap"]
    print("Pluralization:")
    for singular in singulars:
        plural = nlp.pluralize(singular)
        print(f"  Plural of '{singular}': {plural}")
    print()

    # Tokenization
    sentences = [
        "Merhaba, nasılsınız?",
        "Türkçe doğal dil işleme harika!",
        "Bu toolkit çok kullanışlı.",
        "Ali'nin kitabı masada.",
        "İstanbul'da güzel bir gün."
    ]
    print("Tokenization:")
    for sentence in sentences:
        tokens = nlp.tokenize(sentence)
        print(f"  Original: '{sentence}'")
        print(f"  Tokens: {tokens}")
    print()

    # Accent removal
    accented_texts = ["şeker çörek", "öğrenci", "ılık su", "güneş ışığı"]
    print("Accent Removal:")
    for text in accented_texts:
        plain_text = nlp.remove_accents(text)
        print(f"  Original: '{text}'")
        print(f"  Without accents: '{plain_text}'")
    print()

    # Stemming
    words_to_stem = ["kitaplar", "geleceğim", "arkadaşlarımla", "evden", "okulda", "güzellik"]
    print("Stemming:")
    for word in words_to_stem:
        stemmed = nlp.stem(word)
        print(f"  Original: '{word}'")
        print(f"  Stemmed: '{stemmed}'")
    print()

    # Spell checking
    misspelled_words = ["cok", "guzel", "turkce", "ogretmen", "ogrenci"]
    print("Spell Checking:")
    for word in misspelled_words:
        corrected, was_corrected = nlp.spell_check(word)
        if was_corrected:
            print(f"  '{word}' corrected to '{corrected}'")
        else:
            print(f"  '{word}' is correctly spelled")
    print()

if __name__ == "__main__":
    main()
