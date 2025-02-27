# Hashing de características

En este paso, aprenderemos a realizar el hashing de características utilizando la clase `FeatureHasher` en scikit-learn. El hashing de características es una técnica que mapea las características a un vector de longitud fija utilizando una función hash.

```python
from sklearn.feature_extraction import FeatureHasher

movies = [
    {'category': ['thriller', 'drama'], 'year': 2003},
    {'category': ['animation', 'family'], 'year': 2011},
    {'year': 1974},
]

hasher = FeatureHasher(input_type='string')
hashed_features = hasher.transform(movies).toarray()

print(hashed_features)
```
