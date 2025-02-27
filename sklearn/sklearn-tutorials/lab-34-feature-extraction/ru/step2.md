# Хеширование признаков

В этом шаге мы научимся выполнять хеширование признаков с использованием класса `FeatureHasher` в scikit-learn. Хеширование признаков - это техника, которая сопоставляет признаки с вектором фиксированной длины с использованием хеш-функции.

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
