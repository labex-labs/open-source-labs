# エラスティックネットの適合

これで適合させる作業を進めることができます。エラスティックネット推定器が中心化されていないことに気付かれ、渡したグラム行列が破棄されるのを防ぐために、中心化された設計行列を`fit`に渡す必要があります。ただし、スケーリングされた設計行列を渡すと、前処理コードが誤って再度スケーリングしてしまいます。また、正規化された重みを`fit`関数の`sample_weight`パラメータに渡します。

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
