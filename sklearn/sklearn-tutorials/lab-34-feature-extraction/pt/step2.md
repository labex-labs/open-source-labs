# Hashing de Características

Neste passo, aprenderemos a realizar hashing de características utilizando a classe `FeatureHasher` na biblioteca scikit-learn. O hashing de características é uma técnica que mapeia características para um vetor de comprimento fixo utilizando uma função hash.

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
