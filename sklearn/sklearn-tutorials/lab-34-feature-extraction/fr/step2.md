# Hachage des caractéristiques

Dans cette étape, nous allons apprendre à effectuer l'hachage des caractéristiques à l'aide de la classe `FeatureHasher` dans scikit-learn. L'hachage des caractéristiques est une technique qui projette les caractéristiques sur un vecteur de longueur fixe à l'aide d'une fonction de hachage.

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
