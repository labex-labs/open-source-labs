# DictVectorizer

Evaluaremos el `DictVectorizer`, que es un método que recibe diccionarios como entrada.

```python
from sklearn.feature_extraction import DictVectorizer
from time import time

t0 = time()
vectorizer = DictVectorizer()
vectorizer.fit_transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"hecho en {duration:.3f} s")
print(f"Encontrados {len(vectorizer.get_feature_names_out())} términos únicos")
```
