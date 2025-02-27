# Определение функций предварительной обработки

Токеном может быть слово, часть слова или что угодно, находящееся между пробелами или символами в строке. Здесь мы определяем функцию, которая извлекает токены с использованием простого регулярного выражения (regex), которое соответствует Unicode-символам, составляющим слово. Это включает в себя большинство символов, которые могут быть частью слова на любом языке, а также цифры и нижнее подчеркивание:

```python
import re

def tokenize(doc):
    """Extract tokens from doc.

    This uses a simple regex that matches word characters to break strings
    into tokens. For a more principled approach, see CountVectorizer or
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

Мы определяем дополнительную функцию, которая подсчитывает (частоту) появления каждого токена в заданном документе. Она возвращает словарь частот, который будет использоваться векторизаторами.

```python
from collections import defaultdict

def token_freqs(doc):
    """Extract a dict mapping tokens from doc to their occurrences."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```
