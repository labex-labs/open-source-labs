# 특징 해싱

이 단계에서는 scikit-learn 의 `FeatureHasher` 클래스를 사용하여 특징 해싱을 수행하는 방법을 배웁니다. 특징 해싱은 해시 함수를 사용하여 특징을 고정 길이의 벡터로 매핑하는 기술입니다.

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
