# 特征哈希

在这一步中，我们将学习如何使用 scikit-learn 中的`FeatureHasher`类执行特征哈希。特征哈希是一种使用哈希函数将特征映射到固定长度向量的技术。

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
