# Загрузка признаков из словарей

В этом шаге мы научимся загружать признаки из словарей с использованием класса `DictVectorizer` в scikit-learn.

```python
from sklearn.feature_extraction import DictVectorizer

measurements = [
    {'city': 'Dubai', 'temperature': 33.},
    {'city': 'London', 'temperature': 12.},
    {'city': 'San Francisco', 'temperature': 18.},
]

vec = DictVectorizer()
features = vec.fit_transform(measurements).toarray()
feature_names = vec.get_feature_names_out()

print(features)
print(feature_names)
```
