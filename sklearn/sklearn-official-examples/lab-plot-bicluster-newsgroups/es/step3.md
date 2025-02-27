# Definir NumberNormalizingVectorizer

Definiremos una clase `NumberNormalizingVectorizer()` que hereda de `TfidfVectorizer()` para construir un tokenizador que use la función `number_normalizer()` que definimos anteriormente.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
