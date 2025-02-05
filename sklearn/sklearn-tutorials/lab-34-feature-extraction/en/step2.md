# Feature hashing

In this step, we will learn how to perform feature hashing using the `FeatureHasher` class in scikit-learn. Feature hashing is a technique that maps features to a fixed-length vector using a hash function.

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
