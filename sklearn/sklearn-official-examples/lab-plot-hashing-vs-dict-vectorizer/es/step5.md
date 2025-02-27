# Comparación con vectorizadores de texto con fines especiales

Compararemos los métodos anteriores con el `CountVectorizer` y el `HashingVectorizer`.

```python
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer

t0 = time()
vectorizer = CountVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"hecho en {duration:.3f} s")
print(f"Encontrados {len(vectorizer.get_feature_names_out())} términos únicos")

t0 = time()
vectorizer = HashingVectorizer(n_features=2**18)
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"hecho en {duration:.3f} s")

t0 = time()
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"hecho en {duration:.3f} s")
print(f"Encontrados {len(vectorizer.get_feature_names_out())} términos únicos")
```
