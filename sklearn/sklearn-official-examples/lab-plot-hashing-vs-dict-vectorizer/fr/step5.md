# Comparaison avec des vectoriseurs de texte à usage spécifique

Nous allons comparer les méthodes précédentes avec `CountVectorizer` et `HashingVectorizer`.

```python
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer

t0 = time()
vectorizer = CountVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"terminé en {duration:.3f} s")
print(f"Trouvé {len(vectorizer.get_feature_names_out())} termes uniques")

t0 = time()
vectorizer = HashingVectorizer(n_features=2**18)
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"terminé en {duration:.3f} s")

t0 = time()
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(raw_data)
duration = time() - t0
print(f"terminé en {duration:.3f} s")
print(f"Trouvé {len(vectorizer.get_feature_names_out())} termes uniques")
```
