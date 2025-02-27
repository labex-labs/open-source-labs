# Laden von Features aus Dictionaries

In diesem Schritt werden wir lernen, wie man Features aus Dictionaries mit der Klasse `DictVectorizer` in scikit-learn lädt.

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
