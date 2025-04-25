# 特徴ハッシュ

このステップでは、scikit-learn の`FeatureHasher`クラスを使って特徴ハッシュを行う方法を学びます。特徴ハッシュは、ハッシュ関数を使って特徴を固定長のベクトルにマッピングする手法です。

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
