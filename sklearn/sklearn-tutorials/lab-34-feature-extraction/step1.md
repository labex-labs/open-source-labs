# Loading features from dicts

In this step, we will learn how to load features from dictionaries using the `DictVectorizer` class in scikit-learn.

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
