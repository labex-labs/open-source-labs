# DictVectorizer

Мы проведем бенчмарк `DictVectorizer`, который является методом, принимающим словари в качестве входных данных.

```python
from sklearn.feature_extraction import DictVectorizer
from time import time

t0 = time()
vectorizer = DictVectorizer()
vectorizer.fit_transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"done in {duration:.3f} s")
print(f"Found {len(vectorizer.get_feature_names_out())} unique terms")
```
