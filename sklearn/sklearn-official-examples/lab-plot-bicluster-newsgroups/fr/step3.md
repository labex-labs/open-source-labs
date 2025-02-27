# Définir NumberNormalizingVectorizer

Nous allons définir une classe `NumberNormalizingVectorizer()` qui hérite de `TfidfVectorizer()` pour construire un tokenizer qui utilise la fonction `number_normalizer()` que nous avons définie précédemment.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
