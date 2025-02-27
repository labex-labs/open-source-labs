# Определение NumberNormalizingVectorizer

Мы определим класс `NumberNormalizingVectorizer()`, который наследуется от `TfidfVectorizer()`, чтобы создать токенизатор, который использует функцию `number_normalizer()`, определенную нами ранее.

```python
class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super().build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))
```
