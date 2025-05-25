# Comparação com vetorizadores de texto de propósito específico

Vamos comparar os métodos anteriores com o `CountVectorizer` e o `HashingVectorizer`.

```python
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer

t0 = time()
vectorizer = CountVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"feito em {duration:.3f} s")
print(f"Encontrados {len(vectorizer.get_feature_names_out())} termos únicos")

t0 = time()
vectorizer = HashingVectorizer(n_features=2**18)
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"feito em {duration:.3f} s")

t0 = time()
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"feito em {duration:.3f} s")
print(f"Encontrados {len(vectorizer.get_feature_names_out())} termos únicos")
```
