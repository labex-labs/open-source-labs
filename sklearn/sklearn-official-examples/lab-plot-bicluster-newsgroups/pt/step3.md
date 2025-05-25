# Definir NumberNormalizingVectorizer

Definiremos uma classe `NumberNormalizingVectorizer()` que herda de `TfidfVectorizer()` para construir um tokenizador que utiliza a função `number_normalizer()` definida anteriormente.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
