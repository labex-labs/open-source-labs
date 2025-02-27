# Definiere NumberNormalizingVectorizer

Wir werden eine Klasse `NumberNormalizingVectorizer()` definieren, die von `TfidfVectorizer()` erbt, um einen Tokenizer zu erstellen, der die zuvor definierte Funktion `number_normalizer()` verwendet.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
