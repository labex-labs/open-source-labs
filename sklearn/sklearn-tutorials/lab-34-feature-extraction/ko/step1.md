# 사전에서 특징 로드하기

이 단계에서는 scikit-learn 의 `DictVectorizer` 클래스를 사용하여 사전에서 특징을 로드하는 방법을 배웁니다.

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
