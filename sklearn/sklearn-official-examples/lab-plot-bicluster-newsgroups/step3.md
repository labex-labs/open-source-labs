# Define NumberNormalizingVectorizer

We will define a class `NumberNormalizingVectorizer()` that inherits from `TfidfVectorizer()` to build a tokenizer that uses the `number_normalizer()` function we defined earlier.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
