# DictVectorizer

Nous allons évaluer `DictVectorizer`, qui est une méthode qui reçoit des dictionnaires en entrée.

```python
from sklearn.feature_extraction import DictVectorizer
from time import time

t0 = time()
vectorizer = DictVectorizer()
vectorizer.fit_transform(token_freqs(d) for d in raw_data)
duration = time() - t0
print(f"terminé en {duration:.3f} s")
print(f"Trouvé {len(vectorizer.get_feature_names_out())} termes uniques")
```
