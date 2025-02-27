# Feature Hashing

In diesem Schritt werden wir lernen, wie man Feature Hashing mit der Klasse `FeatureHasher` in scikit-learn durchführt. Feature Hashing ist eine Technik, die Features mithilfe einer Hash-Funktion auf einen Vektor fester Länge abbildet.

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
