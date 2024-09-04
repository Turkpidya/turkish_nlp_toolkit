import re
import unicodedata

class TurkishNLP:
    def __init__(self):
        self.vowels = set('aeıioöuüAEIİOÖUÜ')
        self.front_vowels = set('eiöüEİÖÜ')
        self.back_vowels = set('aıouAIOU')
        self.consonants = set('bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ')
        self.turkish_alphabet = self.vowels.union(self.consonants)

    def check_vowel_harmony(self, word):
        vowels = [char for char in word if char in self.vowels]
        if len(vowels) <= 1:
            return True
        
        if vowels[0] in self.front_vowels:
            return all(v in self.front_vowels for v in vowels[1:])
        else:
            return all(v in self.back_vowels for v in vowels[1:])

    def pluralize(self, word):
        exceptions = {
            "su": "sular",
            "ne": "neler",
        }
        if word in exceptions:
            return exceptions[word]

        last_vowel = next((char for char in reversed(word) if char in self.vowels), None)
        
        if not last_vowel:
            return word + 'ler'  # Default to 'ler' if no vowels found
        
        suffix = 'lar' if last_vowel in 'aıou' else 'ler'
        
        # Handle words ending with a vowel
        if word[-1] in self.vowels:
            return word + suffix
        
        # Handle words ending with 'k'
        if word[-1] == 'k':
            return word[:-1] + 'ğ' + suffix
        
        return word + suffix

    def tokenize(self, text):
        # Improved tokenization for Turkish
        pattern = r'\w+|[^\w\s]'
        tokens = re.findall(pattern, text)
        
        # Handle Turkish-specific cases
        result = []
        for i, token in enumerate(tokens):
            if token == "'":
                if i > 0 and i < len(tokens) - 1:
                    # Combine possessive suffixes with the word
                    result[-1] += token + tokens[i+1]
                    next(tokens, None)  # Skip the next token
                else:
                    result.append(token)
            else:
                result.append(token)
        
        return result

    def remove_accents(self, text):
        nfkd_form = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

    def stem(self, word):
        suffixes = [
            'lar', 'ler', 'lık', 'lik', 'luk', 'lük',
            'cı', 'ci', 'cu', 'cü', 'çı', 'çi', 'çu', 'çü',
            'un', 'ün', 'ın', 'in',
            'dan', 'den', 'tan', 'ten',
            'a', 'e', 'ı', 'i',
            'da', 'de', 'ta', 'te',
            'nda', 'nde',
            'dan', 'den', 'tan', 'ten',
            'ndan', 'nden',
            'la', 'le',
            'ca', 'ce',
            'im', 'ım', 'um', 'üm',
            'sin', 'sın', 'sun', 'sün',
            'iz', 'ız', 'uz', 'üz',
            'siniz', 'sınız', 'sunuz', 'sünüz',
            'lar', 'ler',
            'dır', 'dir', 'dur', 'dür', 'tır', 'tir', 'tur', 'tür',
        ]
        
        for suffix in suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                return word[:-len(suffix)]
        return word

    def spell_check(self, word):
        common_mistakes = {
            'ğ': 'g', 'Ğ': 'G',
            'ç': 'c', 'Ç': 'C',
            'ş': 's', 'Ş': 'S',
            'ı': 'i', 'İ': 'I',
            'ö': 'o', 'Ö': 'O',
            'ü': 'u', 'Ü': 'U',
        }
        
        corrected_word = word
        for correct, mistake in common_mistakes.items():
            corrected_word = corrected_word.replace(mistake, correct)
        
        if corrected_word != word:
            return corrected_word, True  # Word was corrected
        return word, False  # No correction needed

# Example usage
if __name__ == "__main__":
    nlp = TurkishNLP()

    # Test vowel harmony
    print(nlp.check_vowel_harmony("kitap"))  # True
    print(nlp.check_vowel_harmony("gelmek"))  # True
    print(nlp.check_vowel_harmony("kağıt"))  # True
    print(nlp.check_vowel_harmony("otobüs"))  # False

    # Test pluralization
    print(nlp.pluralize("kitap"))  # kitaplar
    print(nlp.pluralize("ağaç"))  # ağaçlar
    print(nlp.pluralize("köpek"))  # köpekler
    print(nlp.pluralize("su"))  # sular

    # Test tokenization
    print(nlp.tokenize("Merhaba, nasılsınız? Ali'nin kitabı var."))

    # Test accent removal
    print(nlp.remove_accents("şeker çörek"))  # seker corek

    # Test stemming
    print(nlp.stem("kitaplar"))  # kitap
    print(nlp.stem("geleceğim"))  # gelecek

    # Test spell checking
    print(nlp.spell_check("cok"))  # ('çok', True)
    print(nlp.spell_check("guzel"))  # ('güzel', True)
