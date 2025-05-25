# DictVectorizer

Vamos avaliar o `DictVectorizer`, que é um método que recebe dicionários como entrada.

```python
from sklearn.feature_extraction import DictVectorizer
from time import time

t0 = time()
vectorizer = DictVectorizer()
vectorizer.fit_transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"feito em {duration:.3f} s")
print(f"Encontrados {len(vectorizer.get_feature_names_out())} termos únicos")
```
